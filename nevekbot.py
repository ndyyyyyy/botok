
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

nev = input("Mi az elso neved?---->")
nev2 = input("Mi a második neved?--->")
link = input("Írd ide a linket---->")
x = nev[0].upper() + nev[1:].lower()
y = nev2[0].upper() + nev2[1:].lower()
xy = x + " " + y
xylink = " ---> " + link.lower() 
d = "Nev -->  "


with open("nevek.txt", "r+") as f:
    data = f.read()
    f.write(d + xy + "\n")
    linkek = f.write(xylink + "\n")
    f.close()




with open("nevek.txt", "r") as d:
    Lines = d.readlines(linkek)
    if Lines == linkek:
        print("A link már létezik, próbált ujra!")
    else:
        print("Sikeres bejelentkezés!")    
    d.close()        
