#El duefio de un estacionamiento requiere un diagrama de flujo con el algoritmo que le permita determinar cuanto debe cobrar por el uso del estacionamiento a sus clientes. Las tarifas que se tienen son las siguientes:
#Las dos primeras horas a $5.00 c/u.
#Las siguientes tres a $4.00 c/u.
#Las cinco siguientes a $3.00 c/u.
#Después de diez horas el costo por cada una es de dos pesos.
def estCondicional01():
  #Definir variable
  montoP=0
  #Datos de entrada
  horasX=int(input("Ingrese la cantidad de horas:"))
  #Proceso
  if horasX>=10:
    montoP= (horasX-10)*2+37
  elif horasX>=5 and horasX<=10:
    montoP= (horasX-5)*3+22
  elif horasX>=3 and horasX<=5:
    montoP= (horasX-2)*4+10        
  else:
    montoP=horasX*5
  #Datos de salida
  print("Total a pagar:", montoP ,"pesos")
estCondicional01()