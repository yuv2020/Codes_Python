import time
import pyautogui


def delayed_typing(code):
    time.sleep(5)
    code_str = f"""{code}"""
    pyautogui.write(code_str, interval=0)


code = '''

'''
delayed_typing(code)
