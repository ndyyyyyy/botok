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


if xylink in data:
    print("Ez a link sajnos már használva van!")
    print("Próbálja újra")

    
else:
  with open("nevek.txt","r+") as f:
     data = f.read()
     f.write(d + str(xy) + xylink + "\n")   
     f.close()  
     print("Sikeresen hozza adva")

szabalyzat = "ect...ect...ect..."


i=1

while i < 35455559789789789789798789:
    help = input('Kell segítség?- "Igen" vagy "Nem"-->')
    if help.lower() =="igen":
        
        print(szabalyzat)
        break

    if help.lower() =="nem":
        print("A program sikeresen lefutott!!")
        break
       

    else:
        i += 1
        

#Nev -->  F F ---> https://www.facebook.com/profile.php?id=100082492849171
      
