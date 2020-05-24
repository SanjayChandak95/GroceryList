from django.core.mail import send_mail
from groceryList.settings import EMAIL_HOST_USER

def sentmail(email,confirmationLink):
    subject = 'Welcome to Grocery List App'
    message = 'Thank you for being a part of this app.  http://localhost:8080/confirmation/' + email + "+" + confirmationLink
    recepient = email
    try:
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    except Exception:
        print("Not Able to send mail.......")
