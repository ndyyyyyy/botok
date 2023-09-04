#import pickle
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
    f.write(d + xy + xylink + "\n")
    f.close()

#os.system("clear")    
#pickle.dump(xy, open("names.dat", "wb"))

#namessaved = pickle.load(open("names.dat", "rb"))
    