from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
def send_thank_you_email(name, email, message):
    context = {
            'name': name,
            'message': message,

        }

    # Load HTML template and generate email content
    html_content = render_to_string('email_template.html', context)  # This is the HTML template
    text_content = strip_tags(html_content)  # Strip HTML tags to create a plain text version

    # Prepare the email
    subject = 'Thank You for Contacting Us'
    from_email = 'kayodeola47@gmail.com'
    to_email = [email, from_email]  # Customer's email

    # Create the email with both HTML and plain text
    email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email.attach_alternative(html_content, "text/html")

    # Send the email
    email.send(fail_silently=False)




    # try:
    #     # Render the email content using a template
    #     email_content = render_to_string('email_template.html', )
    #     print('sam')
    #     print(email)
    #     # Create and send the email
    #     email_subject = "Thank You for Contacting Us!"
    #     email = EmailMessage(
    #         email_subject,
    #         email_content,
    #         'kayodeola47@gmail.com',  # Replace with your email
    #         [email]
    #     )
    #     email.content_subtype = 'html'  # Mark email content as HTML
    #     email.send()
    #     return True
    # except Exception as e:
    #     return str(e)
    
