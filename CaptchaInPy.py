#Random Captcha generator in python 3.8 

'''
import random
import string

def Captcha(stringLength=8):
    letters = string.ascii_letters
    #join function join's tuple,string,list by given parameter
    #random.choice(parameter)<--select random obj present in parameter
    captcha = ''.join(random.choice(letters) for i in range(stringLength))
    return captcha
cap = Captcha()
print(cap)
p = input("Enter the Captcha:")
if p == cap:
    print("you enter right captcha")
else:
    print("wrong captcha")

    
'''
import Tkinter
top = Tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()
