
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
        "order_id": "coub77a2",
        "gross_amount": 20000
    }, "credit_card":{
        "secure" : True
    }
}
 
transaction = snap.create_transaction(param)
x=transaction["redirect_url"]
# x2=x+"#/gopay-qris"
print(transaction["redirect_url"])
transaction_token1 = snap.create_transaction_token(param)
print(transaction_token1)
