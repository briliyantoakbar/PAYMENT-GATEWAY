# importing the requests library
# import requests

# # api-endpoint
# URL = "	https://webhook.site/db3e034d-4afd-4e17-b5e3-f224ccd6e6c1"

# # location given here
# location = "delhi technological university"

# # defining a params dict for the parameters to be sent to the API
# PARAMS = {'address':location}

# # sending get request and saving the response as response object
# r = requests.get(url = URL)

# # extracting data in json format
# # data = r.json()
# print(r.headers)

# # extracting latitude, longitude and formatted address
# # of the first matching location
# latitude = data['results'][0]['geometry']['location']['lat']
# longitude = data['results'][0]['geometry']['location']['lng']
# formatted_address = data['results'][0]['formatted_address']

# # printing the output
# print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
# 	%(latitude, longitude,formatted_address))
import midtransclient
import midtransclient

# Create Snap API instance
snap = midtransclient.Snap(
    # Set to true if you want Production Environment (accept real transaction).
    is_production=True,
      server_key='Mid-server-LhAuiwUK7c1dQp8W_lmxtNWr'
)
# Build API parameter
param = {
    "transaction_details": {
        "order_id": "coub77ae2",
        "gross_amount": 20000
    }, "credit_card":{
        "secure" : True
    }
}
 
transaction = snap.create_transaction(param)
x=transaction["redirect_url"]
# x2=x+"#/gopay-qris"
print(transaction["redirect_url"])

while True:
    api_client = midtransclient.CoreApi(
    is_production=True,
    server_key='Mid-server-LhAuiwUK7c1dQp8W_lmxtNWr',
    client_key='Mid-client-Pr7pP47Gyd_7lXFG'
    )
    import midtransclient
    # This is just for very basic implementation reference, in production, you should validate the incoming requests and implement your backend more securely.

    # Initialize api client object
    # You can find it in Merchant Portal -> Settings -> Access keys

    # These are wrapper/implementation of API methods described on: https://api-docs.midtrans.com/#midtrans-api
    # get status of transaction that already recorded on midtrans (already `charge`-ed) 
    status_response = api_client.transactions.status('coub77ae2')
    # get transaction status of VA b2b transaction
    # statusb2b_response = api_client.transactions.statusb2b('tt-tranction-321')
    print(status_response)
# get transaction status of VA b2b transaction
# statusb2b_response = api_client.transactions.statusb2b('YOUR_ORDER_ID OR TRANSACTION_ID')

# # approve a credit card transaction with `challenge` fraud status
# approve_response = api_client.transactions.approve('YOUR_ORDER_ID OR TRANSACTION_ID')

# # deny a credit card transaction with `challenge` fraud status
# deny_response = api_client.transactions.deny('YOUR_ORDER_ID OR TRANSACTION_ID')

# # cancel a credit card transaction or pending transaction
# cancel_response = api_client.transactions.cancel('YOUR_ORDER_ID OR TRANSACTION_ID')

# # expire a pending transaction
# expire_response = api_client.transactions.expire('YOUR_ORDER_ID OR TRANSACTION_ID')

# refund a transaction (not all payment channel allow refund via API)
# param = {
#     "amount": 5000,
#     "reason": "Item out of stock"
# }
# refund_response = api_client.transactions.refund('t-tyty21',param)