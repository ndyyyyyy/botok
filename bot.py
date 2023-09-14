import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


with open("nevek.txt", "r") as f:
    data = f.read()
    f.close()

    
nev = input("Mi az elso neved?---->")
if nev == "fk=%!876)=//=UVhH=(%!§dkdj78756)":
  print("Admin")
elif nev != "fk=%!876)=//=UVhH=(%!§dkdj78756)":
 nev2 = input("Mi a második neved?--->")
 link = input("Írd ide a linket---->")
 x = nev[0].upper() + nev[1:].lower()
 y = nev2[0].upper() + nev2[1:].lower()
 link2 = link.lower()
 xy = x + " " + y
 xylink = " ---> " + link2
 d = "Nev -->  "
   

ix = 0
while ix < 999999999:
  if xylink in data:
    print("Ez a link sajnos már használva van!")
    print("Próbálja újra!")
    i + 1
    
  else:
    with open("nevek.txt","r+") as f:
     data = f.read()
     f.write(d + str(xy) + xylink + "\n")   
     f.close()  
     print("Sikeresen hozza adva!")
     break




i = 0

szabályzat = "fffff"

while i < 9999999999999999:
   help = input('Kell segítség?- "igen" vagy "nem" vagy "adataim"--->')
   if help.lower() =="igen":
    print(szabályzat)
    break
   
   if help.lower() =="adataim":
      nev11 = input("Mi az elso neved?---->")
      nev22 = input("Mi a második neved?--->")
      xd = nev11[0].upper() + nev11[1:].lower()
      yd = nev22[0].upper() + nev22[1:].lower()
      xyd = xd + " " + yd
      d = "Nev -->  "
   
      with open("nevek.txt", "r") as f:
        data = f.read()
        adataimm = data.find(xyd)
        getdata = data[adataimm : len(xyd)]
        print(getdata)
        f.close()
        break

   if help.lower() =="nem":
    break
   
   else:
    i += 1
