from flask import Flask, request, jsonify
import uuid


app = Flask(__name__)


@app.route('/payments', methods=['POST'])
def payments():
    payload = request.get_json(silent=True) or {}
    merchant_ref = payload.get('merchantReference')
    amount = payload.get('amount')
    if amount.get('value') != 1200:
        print("Amount value is not 1200!")
        
    payment_method = payload.get('paymentMethod')

    response = {
        "pspReference": "MOCK-123456789",
        "resultCode": "Authorised",
        "merchantReference": merchant_ref,
        "amount": amount,
        "paymentMethod": payment_method,
        "authCode": "MOCKAUTH",
        "additionalData": {"mock": "true"}
    }

    return jsonify(response), 200


# Simple in-memory store for refunds (mock)
refunds_store = {}


@app.route('/refunds', methods=['POST'])
def create_refund():
    payload = request.get_json(silent=True) or {}
    transaction_id = payload.get('transactionId') or payload.get('pspReference') or payload.get('merchantReference')
    amount = payload.get('amount') or {}
    reason = payload.get('reason', 'requested')

    if not transaction_id:
        return jsonify({"error": "transactionId or pspReference required"}), 400

    refund_id = f"REF-{uuid.uuid4().hex[:12]}"
    refund = {
        "refundId": refund_id,
        "originalTransaction": transaction_id,
        "amount": amount,
        "reason": reason,
        "status": "REFUNDED",
        "pspReference": f"MOCK-RF-{uuid.uuid4().hex[:8]}"
    }

    refunds_store[refund_id] = refund
    return jsonify(refund), 200


@app.route('/refunds/<refund_id>', methods=['GET'])
def get_refund(refund_id):
    refund = refunds_store.get(refund_id)
    if not refund:
        return jsonify({"error": "refund not found"}), 404
    return jsonify(refund), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
