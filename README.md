# Payment Mock (Adyen TAPI "Make a payment")

This repository contains a simple Flask-based mock of the Adyen POS TAPI "Make a payment" endpoint.

Files:
- `mock_server.py`: Flask app exposing `POST /payments` returning a mocked authorised response.
- `run_test.py`: Runs a local test using Flask's test client and prints the response.
- `openapi.yaml`: OpenAPI v3 description for the mock endpoint.
- `requirements.txt`: Python dependencies.

Quick test (from repository root):

```powershell
python -m pip install -r requirements.txt
python run_test.py
```

To run server manually:

```powershell
python mock_server.py
```
# Hello World

Run the script from PowerShell or any shell:

```powershell
python main.py
```
