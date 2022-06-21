import pyautogui, time

def enviar(cb_email, mes, ano):
    pyautogui.PAUSE = 2.5
    pyautogui.press("win")
    pyautogui.write("email.txt")
    pyautogui.press("up")
    pyautogui.press("enter")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    pyautogui.hotkey("alt", "f4")
    pyautogui.click(x=408, y=745)
    pyautogui.hotkey("ctrl", "t")
    pyautogui.write("https://outlook.live.com/")
    pyautogui.press("enter")
    time.sleep(15)
    pyautogui.click(x=196, y=144)
    time.sleep(5)
    pyautogui.write(cb_email)
    pyautogui.press("enter")
    pyautogui.press("tab")
    mes = meses(mes)
    pyautogui.write(f"ORDENS DE SERVICO EM ABERTO - {mes.upper()} DE {ano}")
    pyautogui.press("tab")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")


def meses(m):
    m = int(m)
    if m == 1:
        return ("Dezembro")
    elif m == 2:
        return ("Janeiro")
    elif m == 3:
        return ("Fevereiro")
    elif m == 4:
        return ("Março")
    elif m == 5:
        return ("Abril")
    elif m == 6:
        return ("Maio")
    elif m == 7:
        return ("Junho")
    elif m == 8:
        return ("Julho")
    elif m == 9:
        return ("Agosto")
    elif m == 10:
        return ("Setembro")
    elif m == 11:
        return ("Outubro")
    elif m == 12:
        return ("Novembro")
