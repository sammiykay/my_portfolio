from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_thank_you_email(name, email, message):
    try:
        # Render the email content using a template
        email_content = render_to_string('email_template.html', {
            'name': name,
            'message': message
        })
        print('sam')
        print(email)
        # Create and send the email
        email_subject = "Thank You for Contacting Us!"
        email = EmailMessage(
            email_subject,
            email_content,
            'kayodeola47@gmail.com',  # Replace with your email
            [email]
        )
        email.content_subtype = 'html'  # Mark email content as HTML
        email.send()
        return True
    except Exception as e:
        return str(e)
    
