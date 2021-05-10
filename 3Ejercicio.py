#El 14 de febrero una persona desea comprarle un regalo al ser querido que mas aprecia en ese momento, su dilema radica en qué regalo puede hacerle, las altemativas que tiene son las siguientes:
#tarjeta:$10.00 o menos
#chocolates:$11.00 a $100.00
#flores:$101.00 a $250.00
#anillo: mas de $251.00
def estCondicional01():
  #Definir variable
  regaloP=0
  #Datos de entrada
  cantidadX=int(input("Ingrese la cantidad de dinero:"))
  #Proceso
  if cantidadX>=11 and cantidadX<=100:
    regaloP= "unos Chocolates"
  elif cantidadX>=101 and cantidadX<=250:
    regaloP= "unas Flores"
  elif cantidadX>=251:
    regaloP= "un Anillo" 
  elif cantidadX<=0:
    regaloP= "error"        
  else:
    regaloP="una Tarjeta"
  #Datos de salida
  print("Usted puede comprar:", regaloP)
estCondicional01()