#Realice un algoritmo para determinar si una persona puede votarcon base en su edad en las préximas elecciones. Construya el diagrama de flujo, el pseudocodigo y el diagrama N/ S.
def estCondicional01():
  #Definir variable
  edadP=0
  #Datos de entrada
  edadX=int(input("Ingrese la edad:"))
  #Proceso
  if edadX>=18:
    edadP="SI"
  elif edadX<=0:
    edadP="error"  
  else:
    edadP="NO"
  #Datos de salida
  print("Usted vota:", edadP)
estCondicional01()