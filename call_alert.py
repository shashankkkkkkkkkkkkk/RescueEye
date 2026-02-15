from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER, TO_NUMBER

def make_call_alert():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    call = client.calls.create(
        twiml="""
        <Response>
            <Say>
                Emergency. Survivor detected by RescueEye system.
                Please respond immediately.
            </Say>
        </Response>
        """,
        from_=FROM_NUMBER,
        to=TO_NUMBER
    )

    print("📞 Call Triggered:", call.sid)
