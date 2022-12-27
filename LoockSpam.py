from include import SpamEmail
from config import System, Layout
from threading import Thread
if __name__ == '__main__':
    try:
        System.clear()
        Layout.banner()
        System.sleep(1)
        Layout.banner_main()
        response = Layout.cursor()
        if response == '01' or response == '1':
            System.clear()
            Layout.banner()
            print ('\033[0;33mTarget Email:\033[0;m')
            email_av = Layout.cursor()
            
            emails = SpamEmail.ReadJson('config/profile/Emails.json')
            passwords = SpamEmail.ReadJson('config/profile/Passwords.json')
            text = Layout.doc()
            title = 'LoockSpam'
            while True:
                msg = SpamEmail.WithMessage(title,text, emails[0],email_av)
                SpamEmail.EmailLogin(emails[0],passwords[0], msg)
                print (f'\033[0;32mEmail Enviado Para \033[0;31m {email_av}\033[0;m')
                
                msg2 = SpamEmail.WithMessage(title,text, emails[1],email_av)
                Thread(target=SpamEmail.EmailLogin,args=(emails[1],passwords[1], msg2, )).start()
                print (f'\033[0;32mEmail Enviado Para \033[0;31m {email_av}\033[0;m')
                
                msg3 = SpamEmail.WithMessage(title,text, emails[2],email_av)
                SpamEmail.EmailLogin(emails[2],passwords[2], msg3)
                print (f'\033[0;32mEmail Enviado Para \033[0;31m {email_av}\033[0;m')
                msg4 = SpamEmail.WithMessage(title,text, emails[3],email_av)
                SpamEmail.EmailLogin(emails[3],passwords[3], msg4)
                print (f'\033[0;32mEmail Enviado Para \033[0;31m {email_av}\033[0;m')
                msg5 = SpamEmail.WithMessage(title,text, emails[4],email_av)
                SpamEmail.EmailLogin(emails[4],passwords[4], msg5)
                print (f'\033[0;32mEmail Enviado Para \033[0;31m {email_av}\033[0;m')
                msg6 = SpamEmail.WithMessage(title,text, emails[5],email_av)
                SpamEmail.EmailLogin(emails[5],passwords[5], msg6)
                print (f'\033[0;32mEmail Enviado Para \033[0;31m {email_av}\033[0;m')
                msg7 = SpamEmail.WithMessage(title,text, emails[6],email_av)
                SpamEmail.EmailLogin(emails[6],passwords[6], msg7)
                print (f'\033[0;32mEmail Enviado Para \033[0;31m {email_av}\033[0;m')
        elif response == '02' or response == '2':
            info_tool = SpamEmail.ReadJson('config/profile/Creditos.json')
            System.clear()
            Layout.banner()
            print (f'''
    \033[0;33mAuthor: {info_tool[0]}\nVersão:{info_tool[3]}\nName: {info_tool[1]}\nGithub: {info_tool[2]}\033[0;m
               ''')
        else:
            System.clear()
            Layout.banner()
            print ('Exit Programming...')
    except:
        System.clear()
        System.sleep(1)
        print ('Error: 205')
          
           