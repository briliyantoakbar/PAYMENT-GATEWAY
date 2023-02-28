# import midtransclient
# # Create Core API instance
# GOPAY_PAYMENT_OPTION_TOKEN = '04ed77b7-5ad5-4ba5-b631-d72aa369c2f7'
# ACTIVE_ACCOUNT_ID = '6975fc98-8d44-490d-b50a-28d2810d6856'
# core_api = midtransclient.CoreApi(
#     is_production=True,
#     server_key='Mid-server-k_ZfB0iZykq28QPkKp07TUej',
#     client_key='Mid-client-RWjBuHE92zoracVA'
# )
# # Build API parameter
# param = {
#     "payment_type": "gopay",
#     "transaction_details": {
#         "gross_amount": 1244145,
#         "order_id": "hygy-t1",
#         "token": GOPAY_PAYMENT_OPTION_TOKEN,
#     },
#     "gopay": {
#       "account_id": ACTIVE_ACCOUNT_ID
#     }
# }
import midtransclient
import datetime

# Initialize core api client object
# You can find it in Merchant Portal -> Settings -> Access keys
core_api = midtransclient.CoreApi(
    is_production=True,
    server_key='Mid-server-LhAuiwUK7c1dQp8W_lmxtNWr',
    client_key='Mid-client-Pr7pP47Gyd_7lXFG'
    # is_production=False,
    # server_key='SB-Mid-server-jdslTONbVvrONwy77BIV9PRe',
    # client_key='SB-Mid-client-ztDc1KJnedAz6k5r'
)
param={
  "payment_type": "bri_epay",
  "transaction_details": {
    "order_id": "2014111702",
    "gross_amount": 11000
  },
  "item_details": [
    {
      "id": "1",
      "price": 11000,
      "quantity": 1,
      "name": "Mobil "
    }
  ],
  "customer_details" : {
    "first_name": "Andri",
    "last_name": "Litani",
    "email": "andri@litani.com",
    "phone": "081122334455"
  }
}
charge_response = core_api.charge(param)
print(charge_response)