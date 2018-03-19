from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe6a26c83d6b8342daef53baab045bb1c"
# Your Auth Token from twilio.com/console
auth_token  = "6fb86df5a1adad8fd094e83cc69322f1"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918449062704", 
    from_="+14432620277",
    body="Hello Raju!")

print(message.sid)
