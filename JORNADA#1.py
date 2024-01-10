import  pyautogui
import time
import pandas

pyautogui.press("win")
pyautogui.write("Firefox")
pyautogui.PAUSE = 2
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(x=1030, y=407)
pyautogui.write("Seu_Email_Aqui")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("enter")
tabela = pandas.read_csv("produtos.csv")

for i in tabela:
    pyautogui.click(x=785, y=284)
    pyautogui.write("MOLO000192")
    pyautogui.press("tab")
    pyautogui.write("Logitech")
    pyautogui.press("tab")
    pyautogui.write("Mouse")
    pyautogui.press("tab")
    pyautogui.write("1")    
    pyautogui.press("tab")
    pyautogui.write("25.95")
    pyautogui.press("tab")
    pyautogui.write("6.5")
    pyautogui.press("tab")
    pyautogui.write("")
    pyautogui.press("tab")
    pyautogui.press("enviar")
    pyautogui.press("enter")
    pyautogui.scroll(1000)
    print(tabela)