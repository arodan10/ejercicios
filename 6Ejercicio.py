#Realice el diagrama de flujo, el pseudocodjgo y el diagrama N/S que muestren el algoritmo para determiner el costo y el descuento que tendra un articulo. Considere que si su precio es mayor o igual a $200 se le aplica un descuento de 15%, y si su precio es mayor a $100 pero menor a $200, el descuento es de 12%, y si es menor a $100,solo 10%.
def estCondicional01():
  #Definir variable
  montoP=0
  #Datos de entrada
  precioX=int(input("Ingrese el monto:"))
  #Proceso
  if precioX>=200:
    montoP=precioX-(precioX*0.15)
  elif precioX>=100 and precioX<=200:
    montoP=precioX-(precioX*0.12)         
  else:
    montoP=precioX-(precioX*0.10)
  #Datos de salida
  print("Total a pagar:",montoP,"soles" )
estCondicional01()