#Realice un algoritmo para determinar el sueldo semanal de un trabajador con base en las horas trabajadas y el pago por hora.
def estCondicional01():
  #Definir variable
  sueldoP=0
  #Datos de entrada
  horasX=int(input("Ingrese la cantidad de horas trabajadas de esta semana:"))
  #Proceso
  if horasX>=40:
    sueldoP=(horasX-40)*20+400
  else:
    sueldoP=horasX*10
  #Datos de salida
  print("Su sueldo semanal es:", sueldoP ,"soles" )
estCondicional01()