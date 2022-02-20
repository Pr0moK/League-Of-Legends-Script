import pyautogui
import time
import os

clear = lambda: os.system('cls')
get_ban = 0
get_pick = 0
ask_champs = True
start_autoaccept = False
select_champ = False
pick_phase = False


def search_pick():
    global get_pick
    search_champ = pyautogui.locateCenterOnScreen('lockin.png', grayscale=True, confidence=.98)
    time.sleep(0.5)
    if search_champ != None:
        print("Znalazlem picka")
        pyautogui.click(search_champ[0] + 185, search_champ[1] - 505)
        time.sleep(1)
        pyautogui.write(champ_to_pick)
        time.sleep(0.5)
        get_pick += 1
    else:
        print("Nie ma twojego picka")
        time.sleep(2)


def pick_champ():
    pick = pyautogui.locateCenterOnScreen('lockin.png', grayscale=True, confidence=.98)
    if pick != None:
        pyautogui.moveTo(pick[0] - 265, pick[1] - 455)
        pyautogui.click(pick[0] - 265, pick[1] - 455)
        print("Wybrano picka")
        time.sleep(0.5)
        pyautogui.click(pick)
        time.sleep(2)
        exit("Zakonczono WYBOR")
    else:
        print("Nie wybrano picka")
        time.sleep(2)


def search_ban():
    global get_ban
    search = pyautogui.locateCenterOnScreen('ban.png', grayscale=True, confidence=.90)
    time.sleep(0.5)
    if search != None:
        print("Wpisuje Bana")
        pyautogui.click(search[0] + 185, search[1] - 505)
        time.sleep(1)
        pyautogui.write(champ_to_ban)
        time.sleep(0.5)
        get_ban += 1
    else:
        print("Nie wpisuje bana")
        time.sleep(2)


def ban_champ():
    global ban_phase
    global pick_phase
    ban = pyautogui.locateCenterOnScreen('ban.png', grayscale=False, confidence=.98)
    if ban != None:
        pyautogui.moveTo(ban[0] - 265, ban[1] - 455)
        pyautogui.click(ban[0] - 265, ban[1] - 455)
        print("Banuje postac")
        time.sleep(0.5)
        pyautogui.click(ban)
        time.sleep(2)
        pick_phase = True
    else:
        print("Nie ma postaci do banowania")
        time.sleep(2)


def accept_match():
    global select_champ
    accept = pyautogui.locateCenterOnScreen('accept.png', grayscale=True, confidence=.5)

    if accept != None:
        print("Akceptuje mecz")
        pyautogui.click(accept)
        time.sleep(12)
        select_champ = True
    else:
        print("Nie akceptuje")
        time.sleep(2)


def match_dodged():
    global select_champ
    global pick_phase
    accept = pyautogui.locateCenterOnScreen('accept.png', grayscale=True, confidence=.5)
    if select_champ == True and accept != None:
        print("Macz zdodgowany")
        time.sleep(1)
        select_champ = False
        pick_phase = False
    else:
        pass


while ask_champs == True:
    champ_to_pick = input('What would you like to pick?: ')
    champ_to_ban = input('What should we ban?: ')
    if champ_to_pick and champ_to_ban != None:
        print('Champion to pick: ' + champ_to_pick)
        print('Champion to ban: ' + champ_to_ban)
        confrim_select = input("Is that right? Y/N ").upper()
        if confrim_select == "Y":
            ask_champs = False
            start_autoaccept = True
        else:
            pass

while start_autoaccept == True:
    match_dodged()
    if pick_phase == True:
        if get_pick != 1:
            search_pick()
        else:
            pick_champ()
    else:
        if select_champ == True:
            if get_ban != 1:
                search_ban()
            else:
                ban_champ()
        else:
            accept_match()
