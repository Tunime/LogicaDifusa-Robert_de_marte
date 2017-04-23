import random

#print(random.randrange(10))

d=0
volt=0
vo=0
aux=0
dis=int(input("Distancia a recorrer : "))
while(dis>=d):
  form=random.randrange(50)
  alt_obj=random.randrange(30)
  if(form<=6):
    print("Objeto cerca a : ",form,"m")
  else:
    if(form<=21):
      print("Objeto no tan serca a : ",form,"m")
    else:
      print("Onjeto esta lejos a : ",form,"m")
  #tamaño del objeto
  aux=vo
  if(alt_obj<=7):
    print("Objeto pequeño de : ",alt_obj,"cm")
    vo=50
  else:
    if(alt_obj<=12):
      print("Objeto mediano de : ",alt_obj,"cm")
      vo=30
    else:
      print("Objeto Grande de : ",alt_obj,"cm")
      print("Rodeando objeto")
      vo=10
  #verificar la velocidad
  if(aux<=vo):
    if(aux==vo):
      print("Mantener la velocidad actual de : ",vo,"km")
    else:
      print("Subir la velocidad de : ",aux,"km a ",vo,"km")
  else:
    print("Vajar velocidad de : ",aux,"km a ",vo,"km")
  d=d+form
  print("--------------------------")
  print("--------------------------")


