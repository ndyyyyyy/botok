from nevek import *
#import pickle
#import os
nev = input("Mi az elso neved?---->")
nev2 = input("Mi a második neved?--->")
x = nev[0].upper() + nev[1:].lower()
y = nev2[0].upper() + nev2[1:].lower()
xy = x + y
print(xy)

d = "emberneve = "


n = open("nevek.py", "w")

nev_1 = n.write( str(d) + str([xy]))

n.close()

nev = input("Mi az elso neved?---->")
nev2 = input("Mi a második neved?--->")
x = nev[0].upper() + nev[1:].lower()
y = nev2[0].upper() + nev2[1:].lower()
xy = x + y
print(xy)


n = open("nevek.py", "w")

nev_2 = n.write( str(d) + str([xy]))


d.append(nev_2)
n.close()
