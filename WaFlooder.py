from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import requests
import pyfiglet 
import time
import os
import platform
import webbrowser

counter = 0
url = "https://tallgorilla.github.io"

def checkinternet():
    res = False
    try:
        requests.get('https://www.google.com')
        res = False
    except Exception:
        res = True
    if res:
        print("    |-$ It seems that you are not connected to Internet.")
        print('    |-$ WaFlooder will stop now...')
        exit()

def wpbombingwin():
    options = Options()
    wcr_dict = os.getcwd() + r'\chromedriver.exe'
    print (wcr_dict)

    browser = webdriver.Chrome(executable_path=wcr_dict)

    browser.get('https://web.whatsapp.com/')

    os.system('cls')
    print('    |-> 4')

    try:
        confirm = WebDriverWait(browser, 600).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "PVMjB")))
    except:
        print("You have to scan the code with your phone.")
        exit
    finally:
        pass

    browser.set_window_position(-10000,0)

    wp_victim = input("    |-$ Victim's Phone Number (with country code) > ")
    bad_chars = ['+', ' ', '-']

    for i in bad_chars :
        wp_victim = wp_victim.replace(i, '')

    mode = input('''    |
    |-PRESS------------------|
    | 1] Repetitive Mode     |
    | 2] Script/Lyrical Mode |
    |------------------------|
    |-> ''')

    if mode.lower() == '1' or mode.lower() == 'repetitive mode':
        reptxt = input('    |-$ Word/Sentence that you want to send Multiple Times > ')
        repcount = int(input('    |-$ How many times ? > '))

    elif mode.lower() == '2' or mode.lower() == 'script/lyrical mode':
        lyrics = open("lyrics.txt","r+")
        splitedlyrics = (lyrics.read().split())

    else:
        print('    |-} invalid input !')
        return


    browser.get(f'https://web.whatsapp.com/send?phone={wp_victim}&text&source&data&app_absent')

    try:
        confirm = WebDriverWait(browser, 600).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "PVMjB")))
    finally:
        pass

    try:
        confirm = WebDriverWait(browser, 600).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "_2FVVk._2UL8j")))
    except:
        print("    |-} please recheck victim's mobile no. ")
    finally:
        pass

    if mode.lower() == '1' or mode.lower() == 'repetitive mode':
        for i in range(repcount):
            global counter
            counter = counter + 1
            print ("Se han enviado", counter)
            browser.find_element_by_class_name("_2FVVk._2UL8j").send_keys(reptxt + Keys.ENTER)

    elif mode.lower() == '2' or mode.lower() == 'script/lyrical mode':
        for words in splitedlyrics:
            browser.find_element_by_class_name("_2FVVk._2UL8j").send_keys(words + Keys.ENTER)

    time.sleep(5)
    print(
    '''    |-} Done !
    |-----------------------------------------------------------''')
    browser.quit()

def wpbombinglinux():
    options = Options()
    options.add_argument("--log-level=3")
    cr_dict = os.getcwd() + r'/geckodriver'

    browser = webdriver.Firefox(executable_path=cr_dict, options=options)

    browser.get('https://web.whatsapp.com/')

    try:
        confirm = WebDriverWait(browser, 600).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "PVMjB")))
    except:
        print("You have to scan the code with your phone.")
        exit
    finally:
        pass

    browser.minimize_window()

    wp_victim = input("    |-$ Victim's Phone Number (with country code) > ")
    bad_chars = ['+', ' ', '-']

    for i in bad_chars :
        wp_victim = wp_victim.replace(i, '')

    mode = input('''    |
    |-PRESS------------------|
    | 1] Repetitive Mode     |
    | 2] Script/Lyrical Mode |
    |------------------------|
    |-> ''')

    if mode.lower() == '1' or mode.lower() == 'repetitive mode':
        reptxt = input('    |-$ Word/Sentence that you want to send Multiple Times > ')
        repcount = int(input('    |-$ How many times ? > '))

    elif mode.lower() == '2' or mode.lower() == 'script/lyrical mode':
        lyrics = open("lyrics.txt","r+")
        splitedlyrics = (lyrics.read().split())

    else:
        print('    |-} invalid input !')
        return


    browser.get(f'https://web.whatsapp.com/send?phone={wp_victim}&text&source&data&app_absent')

    try:
        confirm = WebDriverWait(browser, 600).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "PVMjB")))
    finally:
        pass

    try:
        confirm = WebDriverWait(browser, 600).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "_2FVVk._2UL8j")))
    except:
        print("    |-} please recheck victim's mobile no. ")
    finally:
        pass

    if mode.lower() == '1' or mode.lower() == 'repetitive mode':
        for i in range(repcount):
            global counter
            counter = counter + 1
            print ("Se han enviado", counter)
            browser.find_elements_by_xpath("//div[@class='_3FRCZ copyable-text selectable-text']")[1].send_keys(reptxt + Keys.ENTER)

    elif mode.lower() == '2' or mode.lower() == 'script/lyrical mode':
        for words in splitedlyrics:
            browser.find_elements_by_xpath("//div[@class='_3FRCZ copyable-text selectable-text']")[1].send_keys(words + Keys.ENTER)

    time.sleep(5)
    print(
    '''    |-} Done !
    |-----------------------------------------------------------''')
    browser.quit()

if platform.system() == 'Linux':
    linux = True
    pass
elif platform.system() == 'Windows':
    linux = False
    pass
else:
    print('OS not supported !')
    exit()

checkinternet()

result = pyfiglet.figlet_format("TallGorilla's WaFlooder")

print (result, "https://tallgorilla.github.io")

if linux:
    wpbombinglinux()
elif linux == False:
    wpbombingwin()
time.sleep(2)
