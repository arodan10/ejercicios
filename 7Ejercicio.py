#Realice un algoritmo que permita determinar el sueldo semanal de un trabajador con base en las horas trabajadas y el pago por hora, considerando que a partir de la hora numero 41 y hasta la 45, cada hora se le paga el doble, de la hora 46 a la 50, el triple, y que trabajar mas de 50 horas no esta permitido. Represente el algoritmo mediante el diagrama de flujo, el pseudocédigo y el diagrama N/ S.
def estCondicional01():
  #Definir variable
  sueldoP=0
  #Datos de entrada
  horasX=int(input("Ingrese la cantidad de horas trabajadas de esta semana:"))
  #Proceso
  if horasX>=41 and horasX<=45:
    sueldoP=(horasX-40)*20+400
  elif horasX>=46 and horasX<=50:
    sueldoP= (horasX-45)*30+500
  elif horasX>=51:
    sueldoP=650
    sueldoL="     OJO el maximo de horas es de 50 horas"
  else:
    sueldoP=horasX*10
  #Datos de salida
  print("Su sueldo semanal es:", sueldoP ,"soles", sueldoL )
estCondicional01()