from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
i = 0
clear = lambda: os.system("cls")
from time import sleep
def serverMessage(message):
    print(f"[\u001b[36mSERVER\u001b[0m] {message}")
def instagramMessage(message):
    print(f"[\u001b[31mIN\u001b[33mS\u001b[32mT\u001b[36mA\u001b[34mG\u001b[19mR\u001b[31mAM\u001b[0m] {message}")
def errorMessage(message):
    print(f"[\u001b[31mERROR\u001b[0m] {message}")
options = Options()
#options.headless = True options=options
driver = None
driver = webdriver.Firefox(executable_path=r"C:\Users\Aron Kylebäck\Downloads\h\geckodriver.exe")
#while i <= 5:
 #      driver = webdriver.Firefox(executable_path=r"C:\Users\Aron Kylebäck\Downloads\h\geckodriver.exe")
   # print("Initializing Client")
    #if i == 0:
     #   print("\u001b[33m[----------] (0%) DONE\u001b[0m")
      #  i += 1
    #elif i == 1:
     #   print("\u001b[33m[⬜--------] (20%) DONE\u001b[0m")
#        i += 1
 #   elif i == 2:
  #      print("\u001b[33m[⬜⬜------] (40%) DONE\u001b[0m")
   #     i += 1
    #elif i == 3:
     #   print("\u001b[33m[⬜⬜⬜----] (60%) DONE\u001b[0m")
      #  i += 1
  #  elif i == 4:
   #     print("\u001b[33m[⬜⬜⬜⬜--] (80%) DONE\u001b[0m")
    #    i += 1
    #elif i == 5:
     #   print("\u001b[32m[⬜⬜⬜⬜⬜] (100%) DONE")
     #   print("[---DONE---]\u001b[0m")
      #  i += 1
    #else:
     #   print("\u001b[31m-----[ERROR]----- \u001b[0m")
      #  print("Something went wrong!")
       # exit()
    #sleep(2)
    #clear()
sleep(2)
serverMessage("Opening browser client")
driver.get("https://www.instagram.com/") 
print("Loading...") 
sleep(6)   
serverMessage("Successfully opened instagram.com")
data = open("data.txt", "a+")
opnBool = False
opArr = []
# Variable decl
username = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
password = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
#with open("data.txt","r") as handler:
#    for l in handler:
#        if l:
#
#            opArr.append(l)
            
#print(opArr)
#print() 
userusername = str(input("What is your username/phone number/email?\n>> "))
userpassword = str(input("What is your password?\n>> "))
#saveUsername = str(input("Would you like me to save that?\n>> (y,n) "))
#boolean = True
#with open("data.txt","r") as handler:
 #   for line in handler:
  #      if line.strip() == f"USERNAME: {userusername}":
   #         if saveUsername.upper() == "Y" or saveUsername.upper() == "YES":
    #            boolean = False
     #           clear()
      #          errorMessage("An account with that username/phone number/email already exists!")
#if saveUsername.upper() == "Y" or saveUsername.upper() == "YES":
 #   if(boolean):
  #      clear()
   #     print("Saving...")
    #    data.write(f"USERNAME: {userusername}\nPASSWORD: {userpassword}\n")
     #   data.close()
      #  clear()
       # print("Done saving")

username.send_keys(userusername)
password.send_keys(userpassword)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
sleep(3)
clear()
if "Ditt lösenord var fel. Kontrollera lösenordet." not in driver.page_source:
     errorMessage("Wrong password")
     driver.close()

