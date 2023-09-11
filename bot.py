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



#def nevvissza(link, uzenet="Ez a link mar letezik, probald ujra!"):

with open("nevek.txt", "r") as f:
    data = f.read()
    #temp1 = data.find(xylink)
    #linklength = data[temp1 + len(link2)]
   # print(linklength)

    # print(data)
    #temp = data.find(xy)
    #link33 = data[temp + len(xy) + 6: data.find("Nev", temp)]
    #d_finder = data.find(xy)
    # print(link33)
    f.close()   

#if xy in data:
#   print("Ez a nev mar hasznalt")
                                    ### 1 nevhez tobb link, 1 linkhez 1 ember

if xylink in data:
    print("Ez a link sajnos már használva van!")
    print("Próbálja újra")

    
else:
  with open("nevek.txt","r+") as f:
     data = f.read()
     f.write(d + str(xy) + xylink + "\n")   
     f.close()  
     print("Sikeresen hozza adva")


help = input('Kell segítség?- ha igen írd ide, hogy "help"-->')
print(help)

if help =="help":
    print("f")


