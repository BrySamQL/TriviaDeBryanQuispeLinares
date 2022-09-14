RED='\033[31m'
YELLOW='\033[33m'
GREEN='\033[32m'
RESET='\033[39m'
print("Bienvenido a mi trivia de \"Conducta Financiera\".")
print("Evaluaremos sus habitos financieros.\n")
print("Por favor, ingrese su nombre para comenzar:\n")
nombre=input("")
print("\nMuy bien", nombre,", le haremos algunas preguntas. \nEscriba la letra de la alternativa y presione 'Entrer'"":\n")
print(RED+"\nPregunta 1\n¿De qué manera distribuye su salario mensual?\n"+RESET)
print("a) 1. Realizo compras de vestimenta, viajes y entretenimiento.\n   2. Pago las deudas y servicios.\n   3. Pago el alquiler y la factura por consumo de alimentos.\n")
print("b) 1. Pago el alquiler y la factura por consumo de alimentos.\n   2. Pago las deudas y servicios.\n   3. Realizo compras de vestimenta, viajes y entretenimiento.\n")
print("c) Cuento con un plan mensual de gastos.\n   Está elaborado acorde a mi ingreso mensual promedio.\n")
print("d) Hago uso de mi dinero a medida que lo requiera.\n")
print("Ingrese su respuesta:.\n")
Respuesta1=input("")
while Respuesta1 not in ("a","b","c","d"):
  Respuesta1=input(YELLOW+"\nDebes responder con a, b, c o d.\n\n"+RESET)
if Respuesta1=="a":
  print(GREEN+"\nDeberia reevaluar sus prioridades."+RESET)
elif Respuesta1=="b":
  print(GREEN+"\nNada mal."+RESET)
elif Respuesta1=="c":
  print(GREEN+"\n¡Muy bien!"+RESET)
elif Respuesta1=="d":
  print(GREEN+"\n¡No descuide su economia!"+RESET)
else:
    print(GREEN+"No existe esa alternativa."+RESET)
print(RED+"\nPregunta 2\n¿Qué uso le das a la tarjeta de crédito?\n"+RESET)
print("a) Compro con tarjeta de crédito los productos deseo.\n   Divido en cuotas para no pagar mucho.\n")
print("b) Compro con tarjeta de crédito productos y servicios que necesito.\n   Pago antes de la fecha de corte.\n")
print("c) No uso tarjeta de crédito porque siempre me quitan dinero.\n")
print("d) Compro todo con tarjeta de crédito ya que acumulo puntos.\n")
print("Ingrese su respuesta:.\n")
Respuesta2=input("")
while Respuesta2 not in ("a","b","c","d"):
  Respuesta2=input(YELLOW+"\nDebes responder con a, b, c o d.\n\n"+RESET)
if Respuesta2=="a":
  print(GREEN+"\nConsidere los intereses que acumularan sus gastos."+RESET)
elif Respuesta2=="b":
  print(GREEN+"\n¡Muy bien!"+RESET)
elif Respuesta2=="c":
  print(GREEN+"\nBien. Pero no descuides tu historial crediticio."+RESET)
elif Respuesta2=="d":
  print(GREEN+"\n¡No descuide su economia!"+RESET)
else:
    print(GREEN+"No existe esa alternativa."+RESET)
print(RED+"\nPregunta 3\n¿Cómo apartas el dinero para tus ahorros?\n"+RESET)
print("a) Al terminar los gastos del mes, destino el sobrante para ahorros.\n")
print("b) No tengo ahorros.\n")
print("c) El dinero excedente lo invierto en la bolsa de valores.\n")
print("d) Mi ahorro es un costo fijo. Lo deposito mensualmente en una cuenta de ahorros.\n")
print("Ingrese su respuesta:.\n")
Respuesta3=input("")
while Respuesta3 not in ("a","b","c","d"):
  Respuesta3=input(YELLOW+"\nDebes responder con a, b, c o d.\n\n"+RESET)
if Respuesta3=="a":
  print(GREEN+"\nNada mal. Pero un monto variable no permitirá proyectarse en el futuro."+RESET)
elif Respuesta3=="b":
  print(GREEN+"\n¡No descuide su economia!"+RESET)
elif Respuesta3=="c":
  print(GREEN+"\nRecuerde que la bolsa de valores cambia todo el tiempo."+RESET)
elif Respuesta3=="d":
  print(GREEN+"\n¡Muy bien!"+RESET)
else:
    print(GREEN+"No existe esa alternativa."+RESET)
print("\n¡La trivia a terminado, gracias por participar!")