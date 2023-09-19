import random,string,os,sys
#SM-N980B [Samsung]
def generate_SM():
 
    uppercase_letter = random.choice(string.ascii_uppercase)
 
    three_digit_number = ''.join(random.choice(string.digits) for _ in range(3))
    second_uppercase_letter = random.choice(string.ascii_uppercase)
    model_code = f"SM-{uppercase_letter}{three_digit_number}{second_uppercase_letter}"
    return model_code
    
#RMX1829 [Realme]
def generate_rmx():
    random_digits = ''.join(random.choice(string.digits) for _ in range(4))
    randomized_string = "RMX" + random_digits
    return randomized_string
 
#CPH2022 [Oppo]
def generate_cph():
 
    random_digits = ''.join(random.choice(string.digits) for _ in range(4))
 
    randomized_string = "CPH" + random_digits
    return randomized_string
    
#LU2902 [LG]
def generate_lu():
 
 
    random_digits = ''.join(random.choice(string.digits) for _ in range(4))
 
    randomized_string = "LU" + random_digits
    return randomized_string
 
#LS902 [LG]
def generate_ls():
    random_digits = ''.join(random.choice(string.digits) for _ in range(3))
 
    randomized_string = "LS" + random_digits
    return randomized_string
 
#MS902 [LG]
def generate_ms():
 
    random_digits = ''.join(random.choice(string.digits) for _ in range(3))
 
    randomized_string = "MS" + random_digits
    return randomized_string
    
#GT-1920 []
def generate_gt1():
    #uppercase_letter = random.choice(string.ascii_uppercase)
    three_digit_number = ''.join(random.choice(string.digits) for _ in range(4))
    second_uppercase_letter = random.choice(string.ascii_uppercase)
    model_code = f"GT-{three_digit_number}{second_uppercase_letter}"
    return model_code
    
#GT-I2809
def generate_gt2():
    #uppercase_letter = random.choice(string.ascii_uppercase)
    three_digit_number = ''.join(random.choice(string.digits) for _ in range(4))
    second_uppercase_letter = random.choice(string.ascii_uppercase)
    model_code = f"GT-{second_uppercase_letter}{three_digit_number}"
    return model_code
    
#vivo 2027
def generate_vivo1():
 
    #uppercase_letter = random.choice(string.ascii_uppercase)
 
    three_digit_number = ''.join(random.choice(string.digits) for _ in range(4))
    second_uppercase_letter = random.choice(string.ascii_uppercase)
    model_code = f"vivo {three_digit_number}{second_uppercase_letter}"
    return model_code
 
#vivo X259L
def generate_vivo2():
    uppercase_letter = random.choice(string.ascii_uppercase)
    three_digit_number = ''.join(random.choice(string.digits) for _ in range(3))
    second_uppercase_letter = random.choice(string.ascii_uppercase)
    model_code = f"vivo {uppercase_letter}{three_digit_number}{second_uppercase_letter}"
    return model_code  
 
#Screen Clear
def clr():
  os.system("clear")
  logo="""\033[1;94m
  ___  ____ _  _ ____ ____ _  _ 
  |  \ |___ |  | | __ |___ |\ | 
  |__/ |___  \/  |__] |___ | \| 
  © \033[3;96mMogid Khan 
 \033[0;1m"""
  print(logo)
 
#Generator with loop
def makeDev(func, limit):
  current_directory=os.getcwd()+"/"
  save_file=current_directory+"Devices.txt"
  try:open(save_file,"w").write("")
  except:os.system("termux-setup-storage")
  for i in range(limit):
    d=func()
    open(save_file,"a").write(d+"\n")
  print(f" >> \033[1;92mSaved in {save_file} \033[0;1m")
 
#Main Function 
def main():
  clr()
  menu="""
  (1) SM-N980B
  (2) RMX1829
  (3) CPH2022
  (4) LU2902
  (5) LS902
  (6) MS902
  (7) GT-2929I
  (8) GT-I2809
  (9) vivo 2027
  (10) vivo X259L
  
  (?) Select > """
  x=int(input(menu))
  clr()
  limit=int(input(" (?) Limit > "))
  if x==1:makeDev(generate_SM,limit)
  elif x==2:makeDev(generate_rmx,limit)
  elif x==3:makeDev(generate_cph,limit)
  elif x==4:makeDev(generate_lu,limit)
  elif x==5:makeDev(generate_ls,limit)
  elif x==6:makeDev(generate_ms,limit)
  elif x==7:makeDev(generate_gt1,limit)
  elif x==8:makeDev(generate_gt2,limit)
  elif x==9:makeDev(generate_vivo1,limit)
  elif x==10:makeDev(generate_vivo2,limit)
  else:makeDev(generate_SM,limit)
  
  input(" (?) Continue > ")
 
#Infinite Loop 
while True:
  main()