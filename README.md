import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

nev = input("Mi az elso neved?---->")
nev2 = input("Mi a második neved?--->")
link = input("Írd ide a linket---->")
x = nev[0].upper() + nev[1:].lower()
y = nev2[0].upper() + nev2[1:].lower()
link2 = link.lower()
xy = x + " " + y
xylink = " ---> " + link2
d = "Nev -->  "


with open("nevek.txt","r+") as f:
    data = f.read()
    f.write(d + xy + xylink + "\n")   
    d.close()  
