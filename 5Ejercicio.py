#Se tiene el nombre y la edad de tres personas. Se desea saber el nombre y la edad de la persona de menor edad. Realice el algoritmo correspondiente y represéntelo con un diagrama de flujo, pseudocodigo y diagrama N/S.
def estCondicional01():
  #Definir variable
  regaloP=0
  #Datos de entrada
  cantidadX=int(input("De que persona desea saber su edad y su nombre del de   -Mayor edad(opcion 1)   -Media edad(opcion 2)   -Menor edad(opcion 3):"))
  #Proceso
  if cantidadX==1:
    nombreP="Bryan"
    edadP=17
  elif cantidadX==2:
    nombreP="Josue"
    edadP=12
  elif cantidadX==3:
    nombreP="Matius"    
    edadP=10    
  else:
    nombreP="-----"
    edadP="--"
  #Datos de salida
  print("NOMBRE:",nombreP,"     ","EDAD:",edadP)
estCondicional01()