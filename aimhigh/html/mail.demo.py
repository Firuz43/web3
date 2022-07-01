import smtplib
import asynchat
# with smtplib.SMT('smtp.gmail.com', 587) as smtp:

with smtplib.SMT('localhost ', 1025) as smtp:

    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()


    # smtp.login('fryusuf54@gmail.com', 'firuz1999')

    subject = 'Hello from Company'
    body = "Thank you for contacting us we will reply you as soon as possible"

    msg = f'Subject {subject}\n\n{body}'

    smtp.sendmail('fryusuf54@gmail.com', 'firuz1199@mail.ru', msg)