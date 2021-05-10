#El secretario de educacion ha decidido otorgar un bono per desempeño a todos los profesores con base en la puntuación siguiente:
#0-100            1 salario
#101-150          2 salarios minímos
#151-en adelante  3 salarios minímos
def estCondicional01():
  #Definir variable
  calificacionP=0
  #Datos de entrada
  notaX=int(input("Ingrese su puntuación:"))
  #Proceso
  if notaX>=0 and notaX<=100:
    calificacionP="1 salario mínimo"
  elif notaX>=101 and notaX<=150:
    calificacionP="2 salarios mínimos"
  else:
    calificacionP="3 salarios mínimos"
  #Datos de salida
  print("Su premio es de: ",calificacionP)
estCondicional01()