import sys,os,random,hashlib, string 

def clr():

  os.system("clear")

  logo="""\033[1;94m

  _  _ ____ ____ ___  ____ ____ _  _ 

  |__| |___ |__| |  \ | __ |___ |\ | 

  |  | |___ |  | |__/ |__] |___ | \| 

  © \033[3;96mMogid Khan 

 \033[0;1m"""
 
  print(logo)

cyan="\x1B[1;96m"

green="\x1B[1;92m"

reset="\x1B[0;1m"

def line(title,text):

  return f"{cyan}{title} > {green}{text}{reset}"

def main():

  clr()

  connection_token=hashlib.md5(''.join(random.choices(string.ascii_letters+string.digits,k=random.randint(4,32))).encode()).hexdigest()

  session_id=f"nid={''.join(random.choices(string.ascii_letters+string.digits,k=12))};pid=Main;tid={random.randint(100,999)};nc={random.randint(0,9)};fc={random.randint(0,9)};bc={random.randint(0,9)};cid={connection_token}"

  print(f"""

  {line('NET HNI',random.randint(20000,50000))}

  {line('SIM HNI',random.randint(20000,50000))}

  {line('Device Group',random.randint(1000,9999))}

  {line('Session ID',session_id)}

  {line('Connection Token',connection_token)}

  """)

  input("  (?) Continue >")

while True:

  main()