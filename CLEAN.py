with open("nevek.txt", "r") as f:
    data = f.read()
    f.close()
login_reg = input("login vagy sign up?-->")

#SIGN UP-----------------------------------------------------------------------------SIGN UP--------------------------------------------------------------------------------------SIGN UP

if login_reg.lower()=="sign up":
  nev = input("Mi az elso neved?---->")
  nev2 = input("Mi a második neved?--->")
  password_while = 0
  while password_while < 99999999999999999999:
   print("A jelszónak 8-16 karakterből kell álina!!")
   password=input("Írj be egy jelszót--->")
   password_again=input("Írja be a jelszót mégegyszer--->")

   if len(password) >= 8 and len(password) <= 16:
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
  with open("nevek.txt","r+") as f:
     data = f.read()
     f.write(str(xy) +","+ str(email) +","+ str(password) +","+"\n")   
     f.close()  
     print("Fiók Sikeresen lérehozva!!")

#LOGIN----------------------------------------------------------------------------------LOGIN------------------------------------------------------------------------------------LOGIN

if login_reg.lower()=="login":   
 loginemail = input("Mi az email címe?---->")
 if loginemail =="fk=%!876)=//=UVhH=(%!§dkdj78756)":
   print("Admin")
  
 elif loginemail !="fk=%!876)=//=UVhH=(%!§dkdj78756)":
  loginpass = input("Kérem írja be a jelszavát--->")

 #ÁTNÉZNI---------------------ÁTNÉZNI----------------------ÁTNÉZNI----------------------ÁTNÉZNI----------------------ÁTNÉZNI----------------------ÁTNÉZNI----------------------ÁTNÉZNI
  with open("nevek.txt", "a+") as f:
     for sor in f:
      elemek = sor.strip().split(",")
      valasztas = sor[elemek[loginemail][loginpass]]
      print(valasztas)
      print("DDDD")
#ÁTNÉZNI----------------------ÁTNÉZNI----------------------ÁTNÉZNI----------------------ÁTNÉZNI----------------------ÁTNÉZNI----------------------ÁTNÉZNI----------------------ÁTNÉZNI
  jelszo_link = input(str("Írd be a jelszót---->"))
  link = input("Írd ide a linket---->")
  link2 = link.lower()
  xylink = "--->" + link2
  if xylink in data:
    print("Ez a link sajnos már használva van!")
    print("Próbálja újra!")
  with open("nevek.txt","r+") as f:
    #ÁTNÉZNI----------------------#ÁTNÉZNI----------------------#ÁTNÉZNI----------------------#ÁTNÉZNI----------------------#ÁTNÉZNI----------------------#ÁTNÉZNI----------------------#ÁTNÉZNI
     data = f.read()
     f.write(str(link)+"\n")
     print("dddddddddd")
     jel_kereso = data.find(jelszo_link)
     jelszo01 = data[jel_kereso + len(link2)]
     print(jelszo01)   
     f.close()  

    #ÁTNÉZNI----------------------#ÁTNÉZNI----------------------#ÁTNÉZNI----------------------#ÁTNÉZNI----------------------#ÁTNÉZNI----------------------#ÁTNÉZNI----------------------#ÁTNÉZNI

  with open("nevek.txt", "a+") as f:
     for sor in f:
      elemek = sor.strip().split(",")
      print(sor)
     
f.close()




#SEGíTSÉG-------------SEGíTSÉG-------------SEGíTSÉG-------------SEGíTSÉG-------------SEGíTSÉG-------------SEGíTSÉG-------------SEGíTSÉG-------------SEGíTSÉG-------------SEGíTSÉG

i = 0

szabályzat = "fffff"

while i < 9999999999999999:
   help = input('Kell segítség?- "igen" vagy "nem" vagy "adataim"--->')
   if help.lower() =="igen":
    print(szabályzat)
    break
   
   if help.lower() =="adataim":
    f = open("nevek.txt")
    osszesSor = f.readlines()
    f.close()
    adataim_email = input("Kérem írja be az EMAIL címét---")



   if help.lower() =="nem":
    print("Program vége!!")
    break
   
   else:
    print("Hiba, helytelen szóhasznála, próbálja újra")
    i + 1
