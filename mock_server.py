from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/payments', methods=['POST'])
def payments():
    payload = request.get_json(silent=True) or {}
    merchant_ref = payload.get('merchantReference')
    amount = payload.get('amount')
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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
