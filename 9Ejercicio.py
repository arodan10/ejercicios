#Se les daré un bone per antiguedad a los empleados de una tienda. Si tienen un año, se les dara $100; si tienen 2 años, $200, y asi sucesivamente hasta los 5 años. Para los que tengan mas de 5, el bono sera de $1000. Realice un algoritmo y represéntelo mediante el diagrama de flujo, el pseudocedigo y diagrama N/S que permita determinar el bono que recibiré un trabajador.
def estCondicional01():
  #Definir variable
  bonoP=0
  #Datos de entrada
  añosX=int(input("Indique cuantos años tiene como empleado de esta tienda:"))
  #Proceso
  if añosX>=0 and añosX<=5:
    bonoP=añosX*100
  else:
    bonoP=1000
  #Datos de salida
  print("Usted accede a un bono de:",bonoP,"soles")
estCondicional01()