# k={'status_code': '201', 'status_message': 'GoPay transaction is created', 'transaction_id': 'cb67903d-341d-47be-a66d-50bf12190cc6', 'order_id': '9274aaf3-cd82-4d6a-aafa-4277e0b0fcf5', 'merchant_id': 'G039902526', 'gross_amount': '12000.00', 'currency': 'IDR', 'payment_type': 'gopay', 'transaction_time': '2022-11-28 22:28:58', 'transaction_status': 'pending', 'fraud_status': 'accept', 'actions': [{'name': 'generate-qr-code', 'method': 'GET', 'url': 'https://api.sandbox.midtrans.com/v2/gopay/cb67903d-341d-47be-a66d-50bf12190cc6/qr-code'}, {'name': 'deeplink-redirect', 'method': 'GET', 'url': 'https://simulator.sandbox.midtrans.com/gopay/partner/app/payment-pin?id=8e9f04c8-f20d-4639-936f-777d38151dc7'}, {'name': 'get-status', 'method': 'GET', 'url': 'https://api.sandbox.midtrans.com/v2/cb67903d-341d-47be-a66d-50bf12190cc6/status'}, {'name': 'cancel', 'method': 'POST', 'url': 'https://api.sandbox.midtrans.com/v2/cb67903d-341d-47be-a66d-50bf12190cc6/cancel'}]}
# print(k["actions"][1]['url'])
import midtransclient
import datetime
snap = midtransclient.Snap()

import time
kondisi=True
coba= False
if(kondisi==True):
    snap = midtransclient.Snap(
            is_production=True,
            server_key='Mid-server-LhAuiwUK7c1dQp8W_lmxtNWr',
            client_key='Mid-client-Pr7pP47Gyd_7lXFG'
        )
    # Prepare parameter
    param = {
        "transaction_details": {
            "order_id": "po475123",
            "gross_amount": 2000
        }, "credit_card":{
            "secure" : True
        }
    }

    transaction = snap.create_transaction(param)

    transaction_redirect_url = transaction['redirect_url']
    print(transaction_redirect_url)
    time.sleep(20)
    coba=True
    print("Mulai Get")
    kondisi=False
    
if(coba==True):
        api_client = midtransclient.CoreApi(
        is_production=True,
        server_key='Mid-server-LhAuiwUK7c1dQp8W_lmxtNWr',
        client_key='Mid-client-Pr7pP47Gyd_7lXFG')
        status_response = api_client.transactions.status('po475123')
        print(status_response['transaction_status'])
        coba=False