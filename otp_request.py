
# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACe6a26c83d6b8342daef53baab045bb1c"
auth_token = "6fb86df5a1adad8fd094e83cc69322f1"
client = Client(account_sid, auth_token)

message = client.messages("SM7c037683d6bf4a1a995c1bcdc84607ba").fetch()

print(message.body)
