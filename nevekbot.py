import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


with open("nevek.txt", "r") as f:
    data = f.read()
    f.close()
login_reg = input("login vagy sign up?-->")

if login_reg.lower()=="sign up":
  nev = input("Mi az elso neved?---->")
  nev2 = input("Mi a második neved?--->")
  password_while = 0
  while password_while < 99999999999999999999:
   print("A jelszónak 8-16 karakterből kell álina!!")
   password=input("Írj be egy jelszót--->")
   password_again=input("Írja be a jelszót mégegyszer--->")

   if len(password) >= 8 and len(password) <= 16:
    print("jelszó megfelelő hosszuságú!")
    break

   else:
    password_while + 1   



  jhfudg = 0
  while jhfudg < 9999999999:

   if password==password_again:
    print("Jelszó sikeresen létrehozva")
    break
   elif password != password_again:
    print("De a jelszo sikertelen, nem eggyezik meg")
    password=input("Írj be egy jelszót--->")
    password_again=input("Írja be a jelszót mégegyszer--->")
    jhfudg + 1
    break
  
  email=input("Mi az email címed?--->")
  x = nev[0].upper() + nev[1:].lower()
  y = nev2[0].upper() + nev2[1:].lower()
  xy = x + y
  d = "Nev-->"
  with open("nevek.txt","r+") as f:
     data = f.read()
     f.write(d + str(xy) + "--->" + str(password) +"---->" + str(email) +"-----I" "\n")   
     f.close()  
     print("Fiók Sikeresen lérehozva!!")


if login_reg.lower()=="login":    
 loginemail = input("Mi az email címe?---->")
 if loginemail == "fk=%!876)=//=UVhH=(%!§dkdj78756)":
   print("Admin")
 elif loginemail != "fk=%!876)=//=UVhH=(%!§dkdj78756)":
  loginpass = input("Kérem írja be a jelszavát--->")

 print("DDDD")

 f = open("nevek.txt")
 datae = f.read
 szo=datae
 if szo.index((loginemail)) > -1:
    print("bennevan")
 else:
    print("nincs benne")



 for loginemail in f:
    elemek = loginemail.strip().split("---->")
    elemek2 = elemek[1].split("-----I")
    nev = elemek2[0]
    while True:
        if nev[-1] == "-":
            nev = nev[0:len(nev)-1]
        else:
            break
    print(nev)

 f.close()   



 ix = 0
 while ix < 999999999:
  link = input("Írd ide a linket---->")
  link2 = link.lower()
  xylink = "--->" + link2
  d = "Nev-->"
  if xylink in data:
    print("Ez a link sajnos már használva van!")
    print("Próbálja újra!")

    ix + 1

  else:
    with open("nevek.txt","r+") as f:
     nevdata = f.read()
     nevfinderr = str(nevdata.find(xy))
     print(nevfinderr)
     nevfinder = nevfinderr[f.readline(-1)]
     print(nevfinder)
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
    i + 1

   
