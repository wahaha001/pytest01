import json
from mock_server import app


def run():
    client = app.test_client()
    payload = {
        "merchantReference": "order-0001",
        "amount": {"currency": "EUR", "value": 1000},
        "paymentMethod": {"type": "card", "number": "4111111111111111"}
    }
    resp = client.post('/payments', json=payload)
    print('Status:', resp.status_code)
    print('Response JSON:')
    print(json.dumps(resp.get_json(), indent=2))


if __name__ == '__main__':
    run()
