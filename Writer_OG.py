import keyboard
import time
from keyboard import press

a = []
y = []
a.append("#")
nummer = 1
timee = 0.6

def the_best():
    global a
    global timee
    if a != ["#"]:
        time.sleep(5)
        for d in range(len(a)):
            if a[d] == "#":
                press("enter")
                time.sleep(timee)
            else:
                keyboard.write(" " + a[d] + " ")
                time.sleep(timee)
    else:
        print("\nWrite enything\n[-h] [-help]\n")

print(f"[-h] [-help] or [h] [help]\nWrite time:{timee}\n")
while True:
    text=input(f"Write your {nummer} Paragraph:")
    if text == "":
        print("\nWrite enything\n[-h] [-help] or [h] [help]\n")
#------------------------------------------------------------------------------------------------------------------------        
    elif text == "-h" or text == "-help" or text == "h" or text == "help":
        print(f"[-h] [-help]   or [h] [help]\n[-s] [-start]  or [s] [start]\n[-d] [-delete] or [d] [delete]\n[-t] [-text]   or [t] [text]\n[-faster]\n[-slower]\nWrite time:{timee}\n")
#------------------------------------------------------------------------------------------------------------------------        
    elif text == "-s" or text == "-start" or text == "s" or text == "start":
        the_best()
#------------------------------------------------------------------------------------------------------------------------        
    elif text == "-faster":
        if timee <= 0.11:
            print("No MORE")
        else:
            timee = timee - 0.1
            print("Write time:",timee)
#------------------------------------------------------------------------------------------------------------------------        
    elif text == "-slower":
        if timee >= 0.9:
            print("No MORE")
        else:
            timee = timee + 0.1
            print("Write time:",timee)       
#------------------------------------------------------------------------------------------------------------------------        
    elif text == "-d" or text == "-delete" or text == "d" or text == "delete":
        y.clear()
        if nummer >= 2:
            nummer = nummer - 1
        for i in range(len(a)):
            if a[i] == "#":
                y.append(i)
        try:
            b = a[y[-2]:y[-1]]
            text = ""
            for d in range(len(b)):
                if b[d] == "#":
                    pass
                else:
                    text = text + b[d]
            print(f"\nYou deleted Paragraph {nummer}: ",text,"\n")
            del a[y[-2]:y[-1]]
        except:
            pass
#------------------------------------------------------------------------------------------------------------------------            
    elif text == "-t" or text == "-text" or text == "t" or text == "text":
        if a == ["#"]:
            print(f"[-h] [-help] or [h] [help]\nWrite time:{timee}\n-----------------------\nText:")
            text = "\n(empty)\n"
        else:
            print("\nText:")
            text = ""
            for d in range(len(a)):
                if a[d] == "#":
                    text = text + "\n"
                else:
                    text = text + a[d]
        print(text,"\n-----------------------")
#------------------------------------------------------------------------------------------------------------------------        
    else:
        nummer = nummer + 1
        c = text.split(' ')
        for i in range(len(c)):
            if c[i] == "":
                pass
            else:
                for h in c[i]:
                  a.append(h)
            a.append(" ")
        a.append("#")
