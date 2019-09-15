import os


curr_res = os.system("QRes.exe /s > temp.dat")
with open("temp.dat", "r") as f:
    # print(f.read())
    if  "1920x1080, 32 bits @ 60 Hz." in f.read():
        print("Risoluzione corrente Full HD: Passo as 2K")
        os.system("QRes.exe /x:2560 /y:1440 /c:32  /r:60")
    else:
        print("Risoluzione corrente 2K: Passo as Full HD")  
        os.system("QRes.exe /x:1920 /y:1080 /c:32  /r:60")
