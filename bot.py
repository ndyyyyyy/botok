import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


with open("nevek.txt", "r") as f:
    data = f.read()
    f.close()
login_reg = input("Belépés vagy Regisztráció?-->")

if login_reg=="Regisztráció":
  

if login_reg=="Belépés":    
 nev = input("Mi az elso neved?---->")
 if nev == "fk=%!876)=//=UVhH=(%!§dkdj78756)":
   print("Admin")
 elif nev != "fk=%!876)=//=UVhH=(%!§dkdj78756)":
  nev2 = input("Mi a második neved?--->")
  x = nev[0].upper() + nev[1:].lower()
  y = nev2[0].upper() + nev2[1:].lower()
  xy = x + y
  d = "Nev-->"



ix = 0
while ix < 999999999:
  link = input("Írd ide a linket---->")
  link2 = link.lower()
  xylink = "--->" + link2
  if xylink in data:
    print("Ez a link sajnos már használva van!")
    print("Próbálja újra!")

    ix + 1

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
      xyd = xd + yd
      print(xyd)
      d = "Nev-->"
   
      with open("nevek.txt", "r") as f:
        data = f.read()
       # print(data)
        adataimm = data.find(xyd)
        print(len(xyd))
        print(adataimm)
        getdata = data[adataimm : adataimm+len(xyd)]
        print(getdata)
        f.close()
        break

   if help.lower() =="nem":
    print("Program vége!!")
    break
   
   else:
    i += 1

   
