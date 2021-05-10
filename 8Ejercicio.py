#Realice un algoritmo que, con base en una calificacion proporcionada (0-10), indique con letra la calificacion que le corresponde: 10 es “A", 9 es “B", 8 es “C", 7 y 6 son “D", y de 5 a 0 son “F". Represente el diagrama de flujo, el pseudocédigo y el diagrama N/ S correspondiente.
def estCondicional01():
  #Definir variable
  calificacionP=0
  #Datos de entrada
  notaX=int(input("Ingrese su nota:"))
  #Proceso
  if notaX==10:
    calificacionP="A"
  elif notaX==9:
    calificacionP="B"
  elif notaX==8:
    calificacionP="C"
  elif notaX>=6 and notaX<=7:
    calificacionP=  "D"
  elif notaX>=0 and notaX<=5:
    calificacionP=  "F"
  else:
    calificacionP="error!!"
  #Datos de salida
  print("Su calificacion es:",calificacionP)
estCondicional01()