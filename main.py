from __future__ import print_function
import os
import random
import time
import sys
from threading import Timer


def mecanografiar(texto):

 lista = texto.split()

 for palabra in lista:
    sys.stdout.write(palabra + " ")
    sys.stdout.flush()
    time.sleep(.3)

respuestas_correctas = 0;
iniciar_trivia = True
intentos = 0
lista_int = []
lista_punt = []
while iniciar_trivia == True:
  intentos += 1
  respuestas_correctas = 0
  print("\n")
  mecanografiar("\033[1;31m*** Bienvenido a la Trivia de Marvel ***    ")
  print("\n")
  nombre = str(input("\033[0;0m" + "Antes de comenzar coloca tu nombre aqui: "))
  while len(nombre) > 15:
    print("El nombre colocado es muy largo, por favor maximo 15 caracteres")
    nombre = input("\033[0;0m" + "Antes de comenzar coloca tu nombre aqui: ")
  else:
    print()
    print ("Bienvendio " + nombre.upper() + " aqui pondremos a prueba tus conocimientos de las peliculas y series de Marvel.")
  print ("\033[0;0mAhora vamos a poner a prueba tus conocimientos sobre el UCM.")
  print()
  print("Recuerda: Debes ingresar tus respuestas en MINÚSCULAS")
  print("\033[1;33mNotas: Si eliges una opcion incorrecta puedes volver a intentarlo pero no se te considerará el punto. Cada respuesta correcta al primer intento si te otorgara un punto.")
  print()
  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")
  print()
  time.sleep(1)
  mecanografiar("\033[0;34m1.¿Sabes en que año, se estreno Iron Man 1 y quién lo protagonizó? \n")
  print()
  print()
  print("\033[0;0ma) Año 2008, protanizado por Robert Downey Jr.")
  print("b) Año 2007, protanizado por Robert Downey Jr.")
  print("c) Año 2008, protanizado por Tom Cruise")
  print("d) Año 2009, protanizado por Robert De Niro")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
  print()
  respuesta_correcta = "a"
  intentosRealizados = 0
  while respuesta_usuario != respuesta_correcta:
    print("Has introducido una opcion incorrecta, vuelve a intentarlo.\n")
    respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
    intentosRealizados = intentosRealizados + 1
  
  print()
  print("\033[1;32m¡Correcto!\033[0;0m,Iron Man tuvo su premier en Sídney el 14 de abril de 2008, y se estrenó en cines el 2 de mayo. Recibió reseñas generalmente positivas de parte de la crítica y de la audiencia, con elogios en particular a la actuación de Robert Downey Jr. como Tony Stark y recaudó más de $585 millones contra un presupuesto de $140 millones.")
  
  if intentosRealizados < 1:
    respuestas_correctas = respuestas_correctas + 1
  else:
    respuestas_correctas = respuestas_correctas
  
  print()
  print()
  time.sleep(5)
  mecanografiar("\033[0;34m2. ¿Sabes cómo se llamó el equipo formado por Iron man, Black Widow, Captian America , Hulk , Hawkeye y Thor?")
  print()
  print()
  print("\033[0;0ma. Escuadron Suicida")
  print("b. Los Iluminatti")
  print("c. Los Vengadores")
  print("d. Los Defensores")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
  print()
  print()
  respuesta_correcta = "c"
  intentosRealizados2 = 0
  
  while respuesta_usuario != respuesta_correcta:
    print("Has introducido una opcion incorrecta, vuelve a intentarlo.\n")
    respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
    intentosRealizados2 = intentosRealizados2 + 1
    
  print()
  print("\033[1;32m¡Correcto!\033[0;0m, Iron Man/Tony Stark (Robert Downey Jr.), el Increíble Hulk/Bruce Banner (Mark Ruffalo), el Capitán América/Steve Rogers (Chris Evans), Thor (Chris Hemsworth), Black Widow/Natasha Romanoff (Scarlett Johansson) y Hawkeye/Clint Barton (Jeremy Lee Renner) son los personajes que conforman Los Vengadores.")
  
  if intentosRealizados2 < 1:
    respuestas_correctas = respuestas_correctas + 1
  else:
    respuestas_correctas = respuestas_correctas
    
  print()
  print()
  time.sleep(5)
  mecanografiar("\033[0;34m3. ¿Quién se sacrifico en la batalla final de Endgame para detener a Thanos ?")
  print()
  print()
  print("\033[0;0ma. Hulk")
  print("b. Los Guardianes de la Galaxia")
  print("c. Iron man")
  print("d. Black Widow")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
  print()
  print()
  respuesta_correcta = "c"
  intentosRealizados2 = 0
  
  while respuesta_usuario != respuesta_correcta:
    print("Has introducido una opcion incorrecta, vuelve a intentarlo.\n")
    respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
    intentosRealizados2 = intentosRealizados2 + 1
    
  print()
  print("\033[1;32m¡Correcto!\033[0;0m, Tony Stark (Robert Downey Jr) recibió la despedida que se merecía después de sacrificar su vida para derrotar a Thanos de una vez por todas. Los momentos finales de 'Endgame' se centraron en su funeral.")
  
  if intentosRealizados2 < 1:
    respuestas_correctas = respuestas_correctas + 1
  else:
    respuestas_correctas = respuestas_correctas
  
  print()
  print()
  time.sleep(3)
  numero_random = random.randint(1,5)
  if respuestas_correctas == 3:
    print("\033[1;33mFELICIDADES! Has llegado hasta aqui sin equivocarte, por eso tenemos una sorpresa. \nElige un numero del 1 al 5 y presiona enter, si el numero es el mismo, tu puntaje se multiplicara x2 , si tu respuesta es menor o mayor solo se sumara 2 puntos. ")
    eleccion= int(input("Elige un numero del 1 al 5: \033[0;0m"))
    if eleccion == (numero_random):
      print()
      print("\033[1;32mCORRECTO!\033[0;0m, El numero era ", numero_random , "tu puntaje se multiplicara x2.", "Tu puntaje anterior era ",respuestas_correctas)
      respuestas_correctas = respuestas_correctas*2
      print("Tu nuevo puntaje es ", respuestas_correctas)
    else:
      print()
      print("\033[1;31mINCORRECTO!\033[0;0m, El numero era ", numero_random,", a tu puntaje se le sumara 2. \nTu puntaje anterior era:", respuestas_correctas)
      respuestas_correctas = respuestas_correctas + 2
      print("\033[1;32mTu nuevo puntaje es:\033[0;0m", respuestas_correctas )
      print()
  else:
    print("\033[1;33mTu puntaje hasta ahora es\033[0;0m", respuestas_correctas)
  
  print()
  time.sleep(5)
  mecanografiar("\033[0;34m4. Antes de convertirse en Visión, ¿cómo se llama el mayordomo de inteligencia artificial de Iron Man?")
  print()
  print()
  print("\033[0;0ma. Alfred")
  print("b. Jarvis")
  print("c. Friday")
  print("d. Homero")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
  print()
  print()
  respuesta_correcta = "b"
  intentosRealizados2 = 0
  
  while respuesta_usuario != respuesta_correcta:
    print("Has introducido una opcion incorrecta, vuelve a intentarlo.\n")
    respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
    intentosRealizados2 = intentosRealizados2 + 1
    
  print()
  print("\033[1;32m¡Correcto!\033[0;0m, J.A.R.V.I.S., fue una inteligencia artificial creada por Tony Stark, nombrado de esta manera en honor a Edwin Jarvis, el mayordomo que trabajó para Howard Stark. Él tenía control sobre la Mansión Stark y la Torre Stark. También sirvió como una interfaz de usuario de las Armaduras de Iron Man, así como de los otros Vengadores, dándoles información valiosa en sus combates.")
  
  if intentosRealizados2 < 1:
    respuestas_correctas = respuestas_correctas + 1
  else:
    respuestas_correctas = respuestas_correctas
    
  print()
  print()
  time.sleep(3)
  mecanografiar("\033[0;34m5. ¿Cuál es la raza alienígena que Loki envía para invadir la Tierra en The Avengers?")
  print()
  print()
  print("\033[0;0ma. Los Skrulls")
  print("b. Los Kree")
  print("c. Los flerkens")
  print("d. Los Chitauri")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
  print()
  print()
  respuesta_correcta = "d"
  intentosRealizados2 = 0
  
  while respuesta_usuario != respuesta_correcta:
    print("Has introducido una opcion incorrecta, vuelve a intentarlo.\n")
    respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
    intentosRealizados2 = intentosRealizados2 + 1
    
  print()
  print("\033[1;32m¡Correcto!\033[0;0m, Los Chitauri fueron una especie inteligente de seres cibernéticamente mejorados que operaron bajo una mente central. Como subordinados de Thanos, los Chitauri destacaron por haber sido la primera gran amenaza a la Tierra que requirió la formación de los Vengadores cuando intentaron iniciar una invasión planetaria como parte de una alianza entre Thanos y Loki.")
  
  if intentosRealizados2 < 1:
    respuestas_correctas = respuestas_correctas + 1
  else:
    respuestas_correctas = respuestas_correctas
    
  print()
  print()
  time.sleep(3)
  mecanografiar("\033[0;34m6. ¿Qué tipo de médico es Stephen Strange?")
  print()
  print()
  print("\033[0;0ma. Neurocirujano")
  print("b. Cirujano cardiotoracico")
  print("c. Cirujano de trauma")
  print("d. Cirujano Plástico")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
  print()
  print()
  respuesta_correcta = "a"
  intentosRealizados2 = 0
  
  while respuesta_usuario != respuesta_correcta:
    print("Has introducido una opcion incorrecta, vuelve a intentarlo.\n")
    respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
    intentosRealizados2 = intentosRealizados2 + 1
    
  print()
  print("\033[1;32m¡Correcto!\033[0;0m, El Doctor Stephen Strange, un neurocirujano muy reconocido, pierde el uso de sus manos en un terrible accidente de auto, quedando éstas aplastadas hasta el antebrazo. Strange sobrevive apenas pero esto lo llevara a convertirse en Dr. Strange luego de su viaje a Kamar-Taj en Nepal.")
  
  if intentosRealizados2 < 1:
    respuestas_correctas = respuestas_correctas + 1
  else:
    respuestas_correctas = respuestas_correctas
    
  print()
  time.sleep(3)
  mecanografiar("\033[0;34m7. ¿Sobre qué ciudad recuerdan a menudo Hawkeye y Black Widow?")
  print()
  print()
  print("\033[0;0ma. Estanbul")
  print("b. Praga")
  print("c. Grecia")
  print("d. Budapest")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
  print()
  print()
  respuesta_correcta = "d"
  intentosRealizados2 = 0
  
  while respuesta_usuario != respuesta_correcta:
    print("Has introducido una opcion incorrecta, vuelve a intentarlo.\n")
    respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
    intentosRealizados2 = intentosRealizados2 + 1
  print()
  print("\033[1;32m¡Correcto!\033[0;0m, Esto es algo que se referencia en varias ocasiones a lo largo del universo, por ejemplo, en Los Vengadores, el primer crossover de Marvel, cuando en la batalla final Clint le dice a Natasha que eso era como estar de nuevo en Budapest")
  
  if intentosRealizados2 < 1:
    respuestas_correctas = respuestas_correctas + 1
  else:
    respuestas_correctas = respuestas_correctas
    
  print()
  time.sleep(3)
  mecanografiar("\033[0;34m8. ¿Cómo se llama la nave de los Guardianes de la galaxia en Avengers: Infinity War?")
  print()
  print()
  print("\033[0;0ma. El Halcon Milenario")
  print("b. El Benatar")
  print("c. El milano")
  print("d. El USS Enterprise")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
  print()
  print()
  respuesta_correcta = "b"
  intentosRealizados2 = 0
  
  while respuesta_usuario != respuesta_correcta:
    print("Has introducido una opcion incorrecta, vuelve a intentarlo.\n")
    respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
    intentosRealizados2 = intentosRealizados2 + 1
    
  print()
  print("\033[1;32m¡Correcto!\033[0;0m, El Benatar es una nave espacial de clase M utilizada por los Guardianes después de que el Milano fuera destruido")
  
  if intentosRealizados2 < 1:
    respuestas_correctas = respuestas_correctas + 1
  else:
    respuestas_correctas = respuestas_correctas
    
  print()
  time.sleep(3)
  mecanografiar("\033[0;34m9. Antes de “Thor: Ragnarok”, el Grandmaster apareció en: ")
  print()
  print()
  print("\033[0;0ma. Guardianes de la Galaxia")
  print("b. Thor: The Dark World")
  print("c. Guardianes de la Galaxia 2")
  print("d. Dr. Strange")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
  print()
  print()
  respuesta_correcta = "c"
  intentosRealizados2 = 0
  
  while respuesta_usuario != respuesta_correcta:
    print("Has introducido una opcion incorrecta, vuelve a intentarlo.\n")
    respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
    intentosRealizados2 = intentosRealizados2 + 1
    
  print()
  print("\033[1;32m¡Correcto!\033[0;0m, Cómo se vio anteriormente en los Créditos de Guardians of The Galaxy vol.2 en la parte en la que los personajes bailaban al son de la canción se vio por primera vez a este personaje interpretado por Jeff Goldblum en pantalla grande.")
  
  if intentosRealizados2 < 1:
    respuestas_correctas = respuestas_correctas + 1
  else:
    respuestas_correctas = respuestas_correctas
    
  print()
  time.sleep(3)
  mecanografiar("\033[0;34m10. ¿Quién es asesinado por Loki en los Vengadores?")
  print()
  print()
  print("\033[0;0ma. Maria Hill")
  print("b. Agente coulson")
  print("c. Doctor Erik Selvig")
  print("d. Nick Fury")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
  print()
  print()
  respuesta_correcta = "b"
  intentosRealizados2 = 0
  
  while respuesta_usuario != respuesta_correcta:
    print("Has introducido una opcion incorrecta, vuelve a intentarlo.\n")
    respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
    intentosRealizados2 = intentosRealizados2 + 1
    
  print()
  print("\033[1;32m¡Correcto!\033[0;0m, El Agente Phill Coulson fue la persona asesinada por loki en Los Vengadores cuando fue atravesado por una lanza.")
  
  if intentosRealizados2 < 1:
    respuestas_correctas = respuestas_correctas + 1
  else:
    respuestas_correctas = respuestas_correctas
    
  print()
  time.sleep(5)
  print()
  print("\033[1;33mBienvenido a la ronda final, aqui lo mas importante es cuan veloz eres, si terminas en menos de 15 segundos, tu puntaje se triplica, si te demoras mas de 15 pero menos de 30, se duplica y si es mas de 30 segundos el puntaje no se modifica. Estas listo?\033[0;0m")
  time.sleep(7)
  print()
  print("Comienza en: ") 
  print()
  mecanografiar("\033[1;33m9 8 7 6 5 4 3 2 1 . . .\033[0;0m")
  print()
  print()
  
  start = time.time()
  print("\033[1;31m1.¿Cómo se llama el martillo de Thor?")
  print()
  print()
  print("\033[0;0ma) Vanir")
  print("b) Aesir")
  print("c) Miolnir")
  print("d) Mjolnir")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
  print()
  respuesta_correcta = "d"
  intentosRealizados = 0
  while respuesta_usuario != respuesta_correcta:
    print("Has introducido una opcion incorrecta, vuelve a intentarlo.\n")
    respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
    intentosRealizados = intentosRealizados + 1
  
  print()
  print("\033[1;32m¡Correcto!\033[0;0m, EL martillo de thor se llama Mjolnir y esta de hecho de un material llamado Uru.")

  if intentosRealizados < 1:
    respuestas_correctas = respuestas_correctas + 1
  else:
    respuestas_correctas = respuestas_correctas
  print()
  print()
  print("\033[1;31m2.¿Por qué Ant-Man no aparece en Avengers: Infinity War?")
  print()
  print()
  print("\033[0;0ma) Se peleo con el Captian America")
  print("b) Estaba de viaje con su familia")
  print("c) Estaba en arresto domiciliario")
  print("d) Se quedo en prision")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
  print()
  respuesta_correcta = "c"
  intentosRealizados = 0
  while respuesta_usuario != respuesta_correcta:
    print("Has introducido una opcion incorrecta, vuelve a intentarlo.\n")
    respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
    intentosRealizados = intentosRealizados + 1
  
  print()
  print("\033[1;32m¡Correcto!\033[0;0m, Tanto Scott Lang(Ant-Man) como Clint Barton(Hawkeye) aceptaron un trato con el gobierno para mantenerse bajo arresto domiciliario y poder estar con sus familiares.")

  if intentosRealizados < 1:
    respuestas_correctas = respuestas_correctas + 1
  else:
    respuestas_correctas = respuestas_correctas
  print()
  print()
  print("\033[1;31m3.¿En qué película sale Stan Lee como jurado de un concurso de belleza?")
  print()
  print()
  print("\033[0;0ma) Thor: Ragnarok")
  print("b) Iron man 3")
  print("c) Spiderman Homecoming")
  print("d) Dr. Strange")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
  print()
  respuesta_correcta = "b"
  intentosRealizados = 0
  while respuesta_usuario != respuesta_correcta:
    print("Has introducido una opcion incorrecta, vuelve a intentarlo.\n")
    respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
    intentosRealizados = intentosRealizados + 1
  
  print()
  print("\033[1;32m¡Correcto!\033[0;0m, Es en Iron Man 3 donde Stan Lee realizó su cameo como un juez de concurso de belleza sujetando el número 10.")

  if intentosRealizados < 1:
    respuestas_correctas = respuestas_correctas + 1
  else:
    respuestas_correctas = respuestas_correctas
  print()
  print()
  print("\033[1;31m4.¿Cómo obtienen sus poderes Scarlet Witch y QuickSilver?")
  print()
  print()
  print("\033[0;0ma) Son mutantes hijos de Magneto")
  print("b) La gema de la Realidad")
  print("c) Experimentos de SHIELD")
  print("d) La gema de la Mente")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
  print()
  respuesta_correcta = "d"
  intentosRealizados = 0
  while respuesta_usuario != respuesta_correcta:
    print("Has introducido una opcion incorrecta, vuelve a intentarlo.\n")
    respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
    intentosRealizados = intentosRealizados + 1
  
  print()
  print("\033[1;32m¡Correcto!\033[0;0m, Es en Iron Man 3 donde Stan Lee realizó su cameo como un juez de concurso de belleza sujetando el número 10.")

  if intentosRealizados < 1:
    respuestas_correctas = respuestas_correctas + 1
  else:
    respuestas_correctas = respuestas_correctas
  print()
  print()
  print("\033[1;31m5.¿De qué está hecho el escudo del Capitán América?")
  print()
  print()
  print("\033[0;0ma) Adamantium")
  print("b) Vibranio")
  print("c) Acero")
  print("d) Carbonadio")
  print()
  respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
  print()
  respuesta_correcta = "b"
  intentosRealizados = 0
  while respuesta_usuario != respuesta_correcta:
    print("Has introducido una opcion incorrecta, vuelve a intentarlo.\n")
    respuesta_usuario = input("Escribe la letra de la respuesta en MINÚSCULA: ").lower()
    intentosRealizados = intentosRealizados + 1
  
  print()
  print("\033[1;32m¡Correcto!\033[0;0m, EL escudo del Capitan America esta hecho de vibranium, material que proviene del pais Wakanda.")
  if intentosRealizados < 1:
    respuestas_correctas = respuestas_correctas + 1
  else:
    respuestas_correctas = respuestas_correctas
  print()

  end = time.time()
  tiempo_rapido = end - start
  print("Tu puntaje anterior era: " , respuestas_correctas)
  if tiempo_rapido < 15:
    respuestas_correctas = respuestas_correctas*3
  elif tiempo_rapido >=15 and tiempo_rapido < 30:
    respuestas_correctas = respuestas_correctas*2
  else:
    respuestas_correctas = respuestas_correctas
  print("Te demoraste: " , str(round((end - start),2)) , " segundos")
  print()
  print("Procesando tu puntaje final")
  print()
  some_list= [10,20,30,40,65,70,80,100]
  for i in some_list:
    print("\033[1;31m", i, "%   CARGANDO...        \r",i, end='\r'+ "\033[0;0m")
    
    if i > 30 and i <= 65:
      print("\033[1;33m", i,"%  CARGANDO...         \r", end='\r'+ "\033[0;0m")
    if i >=70:
      print("\033[1;32m", i,"%  CARGANDO...        \r", end='\r'+ "\033[0;0m")
    if i ==100:
      print("\033[1;32m", i,"%  CARGADO       \r", end='\r'+ "\033[0;0m")
    time.sleep(1)
    
  print("\033[1;34m    PROCESO COMPLETADO     \033[0;0m")
  print()
  print('\033[1;36mTengo una ultima propuesta para ti, a continuacion aparecera una ruleta que te puede sumar o restar puntos entre el -20 hasta +20 , si escribes SI jugaras la ruleta , si respondes NO o cualquier otra tecla te quedaras con el mismo puntaje\033[0;0m')
  print()
  time.sleep(2)
  suerte = input('\033[1;33mCual es tu respuesta?: \033[0;0m').upper()
  ruleta = random.randint(0,30)
  signo = random.randint(0,1)
  
  if suerte == "SI" and signo == 0:
    respuestas_correctas += ruleta
    print('\033[1;33mAl parecer la fuerza te ha acompañado, a tu puntaje se le sumara',ruleta,'puntos\033[0;0m')
  elif suerte == 'SI' and signo == 1:
    respuestas_correctas -= ruleta
    print('\033[1;31mQue pena, hoy no es tu dia de suerte, mejor no salgas de tu casa, a tu puntaje se le restara',ruleta,'puntos\033[0;0m')
  elif suerte == "NO":
    respuestas_correctas=respuestas_correctas
    print("\033[1;34mAl parecer no quieres dejar las cosas al azar, esta bien tu puntaje no cambiara\033[0;0m")
  else:
    respuestas_correctas=respuestas_correctas
    print("\033[1;34mAl parecer no quieres dejar las cosas al azar, esta bien tu puntaje no cambiara\033[0;0m")
    
  if respuestas_correctas < 20:
    print("Tu puntaje final es: " +   "\033[1;31m" + str(respuestas_correctas))
  elif respuestas_correctas >=20 and respuestas_correctas <40:
    print("\033[0;0mTu puntaje final es: " +  "\033[1;33m" + str(respuestas_correctas))
  else:
    print("\033[0;0mTu puntaje final es: " +  "\033[1;32m" + str(respuestas_correctas))
      
  print("\n\033[1;33m¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  
  lista_int.append(intentos)
  lista_punt.append(respuestas_correctas)
  
  if repetir_trivia != "si": 
   print("\n{} Espero que lo hayas pasado bien, hasta pronto!".format(nombre).upper())
   for numberx in range(0,intentos):
    print("El puntaje de tu intento", lista_int[numberx], "es", lista_punt[numberx]) 
    iniciar_trivia = False