import json
from mock_server import app


def run():
    client = app.test_client()
    payload = {
        "merchantReference": "order-0001",
        "amount": {"currency": "EUR", "value": 1230},
        "paymentMethod": {"type": "card", "number": "4111111111111111"}
    }
    resp = client.post('/payments', json=payload)
    print('Status:', resp.status_code)
    print('Response JSON:')
    print(json.dumps(resp.get_json(), indent=2))

    # Perform a refund for the returned transaction
    resp_json = resp.get_json() or {}
    psp = resp_json.get('pspReference')
    refund_payload = {
        "transactionId": psp,
        "amount": {"currency": "EUR", "value": 1000},
        "reason": "customer_request"
    }
    r = client.post('/refunds', json=refund_payload)
    print('\nRefund Status:', r.status_code)
    print('Refund Response:')
    print(json.dumps(r.get_json(), indent=2))

    # Query the refund by id
    refund_json = r.get_json() or {}
    refund_id = refund_json.get('refundId')
    if refund_id:
        q = client.get(f'/refunds/{refund_id}')
        print('\nQuery Refund:', q.status_code)
        print(json.dumps(q.get_json(), indent=2))


if __name__ == '__main__':
    run()
