
import midtransclient
# This is just for very basic implementation reference, in production, you should validate the incoming requests and implement your backend more securely.

# Initialize core api client object
# You can find it in Merchant Portal -> Settings -> Access keys
# snap = midtransclient.Snap(
#     is_production=False,
#     # server_key='YOUR_SERVER_KEY',
#     # client_key='YOUR_CLIENT_KEY'
#     server_key='SB-Mid-server-jdslTONbVvrONwy77BIV9PRe',
#     client_key='SB-Mid-client-ztDc1KJnedAz6k5r'
# )
# # Prepare parameter
# param = {
#     "transaction_details": {
#         "order_id": "test-transaction011",
#         "gross_amount": 20000
#     }, "credit_card":{
#         "secure" : True
#     }



# }

# transaction = snap.create_transaction(param)

# transaction_redirect_url = transaction['redirect_url']
# print(transaction_redirect_url)
core = midtransclient.CoreApi(
    is_production=True,
    # server_key='SB-Mid-server-jdslTONbVvrONwy77BIV9PRe',
    # client_key='SB-Mid-client-ztDc1KJnedAz6k5r'
    server_key='Mid-server-k_ZfB0iZykq28QPkKp07TUej',
    client_key='Mid-client-RWjBuHE92zoracVA'
)

# prepare CORE API parameter ( refer to: https://docs.midtrans.com/en/core-api/bank-transfer?id=sample-request-and-request-body ) charge bank_transfer parameter example
param = {
    "payment_type": "gopay",
    "transaction_details": {
        "gross_amount": 24000,
        "order_id": "tt-tranyyction-321",
    },
    "bank_transfer":{
        "bank": "bni"
    }
}

# charge transaction
charge_response = core.charge(param)
print('charge_response:')
print(charge_response)