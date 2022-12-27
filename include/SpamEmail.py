import email.message
import json
import smtplib

global msg
msg = None
def WithJsonEmails(lista):
    with open('config/profile/Emails.json', 'w') as f:
        json.dump(lista, f)
        
def WithJsonPasswords(lista):
    with open('config/profile/Passwords.json', 'w') as f:
        json.dump(lista, f)
        
def ReadJson(arq):
    with open(arq, 'r') as f:
        return json.load(f)


def WithMessage(title,text,gmail,hell):
    html = f''' <p>{text}</p> '''
    msg = email.message.Message()
    msg['Subject'] = title
    msg['From'] = gmail
    msg['To'] = hell
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(html)
    return msg
    
    
def EmailLogin(login, password, msg):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(login,password)
    s.sendmail(login, [msg['To']],msg.as_string().encode('utf-8'))
    
if __name__ == '__main__':
    pass
    