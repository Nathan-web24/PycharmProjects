from twilio.rest import Client

TWILIO_SID = "AC3c1952838e332a6441a335fbda03c355"
TWILIO_AUTH_TOKEN = "c3daf729c3396d51195bce75529d6611"
TWILIO_VIRTUAL_NUMBER = "+12184603929"
TWILIO_VERIFIED_NUMBER = "+64273003411"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
