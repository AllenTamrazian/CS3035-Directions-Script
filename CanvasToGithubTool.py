import pyautogui
import pyperclip
import time

arrayOfPagesForC = [
                    ("description user_content enhanced","https://calstatela.instructure.com/courses/101967/assignments/1746370?module_item_id=6605172"), 
                    ("description user_content enhanced","https://calstatela.instructure.com/courses/101967/assignments/1746373?module_item_id=6605174"),
                    ("show-content user_content clearfix enhanced","https://calstatela.instructure.com/courses/101967/pages/ungraded-exercises-c-part-ii?module_item_id=6972926"),
                    ("show-content user_content clearfix enhanced","https://calstatela.instructure.com/courses/101967/pages/ungraded-exercise-write-spaghetti-code?module_item_id=6616855"),
                    ("show-content user_content clearfix enhanced","https://calstatela.instructure.com/courses/101967/pages/ungraded-exercises-c-part-iii?module_item_id=6605177"),
                    ("show-content user_content clearfix enhanced","https://calstatela.instructure.com/courses/101967/pages/ungraded-exercise-pointer-arithmetic?module_item_id=6605173"),
                    ("description user_content enhanced","https://calstatela.instructure.com/courses/101967/assignments/1746383?module_item_id=6605175"),
                    ("description user_content enhanced","https://calstatela.instructure.com/courses/101967/assignments/1746389?module_item_id=6605178"),
                    ("show-content user_content clearfix enhanced","https://calstatela.instructure.com/courses/101967/pages/ungraded-exercise-c-type-compatibility?module_item_id=6617074")
                    ]
arrayOfPagesForPython = [
("show-content user_content clearfix enhanced", "https://calstatela.instructure.com/courses/101967/pages/ungraded-exercise-python?module_item_id=6614909"),
("description user_content enhanced","https://calstatela.instructure.com/courses/101967/assignments/1749137?module_item_id=6614911"),
("description user_content enhanced","https://calstatela.instructure.com/courses/101967/assignments/1746789?module_item_id=6606138"),
("description user_content enhanced","https://calstatela.instructure.com/courses/101967/assignments/1749136?module_item_id=6614910"),
]

def pressTwo(firstKey, secondKey):
    pyautogui.keyDown(firstKey)
    pyautogui.keyDown(secondKey)
    pyautogui.keyUp(firstKey)
    pyautogui.keyUp(secondKey)

def pressThree(firstKey, secondKey, thirdKey):
    pyautogui.keyDown(firstKey)
    pyautogui.keyDown(secondKey)
    pyautogui.keyDown(thirdKey)
    pyautogui.keyUp(firstKey)
    pyautogui.keyUp(secondKey)
    pyautogui.keyUp(thirdKey)

def getDirectionsC():
    pressTwo('command', 'tab')
    for pageNumber in range(len(arrayOfPagesForC)):
        pressTwo('command', 'l')
        pyautogui.typewrite(str(arrayOfPagesForC[pageNumber][1]))
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
        time.sleep(5)
        if(pageNumber==0):
            pressThree('option', 'command','i')
        time.sleep(1)
        pressTwo('command', 'f')
        pyautogui.typewrite(str(arrayOfPagesForC[pageNumber][0]))
        time.sleep(1)
        pyautogui.keyDown('tab')
        pyautogui.keyUp('tab')
        pressTwo('command','c')
        s = pyperclip.paste()
        fileString = '/Users/allentamrazian/Documents/Directions/DirectionsC' + str(pageNumber) + '.txt'
        file = open(fileString, 'w')
        file.write(s)
        file.close()
        fileString=''
# getDirectionsC

def getDirectionsPython():
    pressTwo('command', 'tab')
    for pageNumber in range(len(arrayOfPagesForPython)):
        pressTwo('command', 'l')
        pyautogui.typewrite(str(arrayOfPagesForPython[pageNumber][1]))
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
        time.sleep(5)
        if(pageNumber==0):
            pressThree('option', 'command','i')
        time.sleep(1)
        pressTwo('command', 'f')
        pyautogui.typewrite(str(arrayOfPagesForPython[pageNumber][0]))
        time.sleep(1)
        pyautogui.keyDown('tab')
        pyautogui.keyUp('tab')
        pressTwo('command','c')
        s = pyperclip.paste()
        fileString = '/Users/allentamrazian/Documents/DirectionsPython' + str(pageNumber) + '.txt'
        file = open(fileString, 'w')
        file.write(s)
        file.close()
        fileString=''
getDirectionsPython()