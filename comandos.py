import subprocess
import wifi_qrcode_generator as qr
import cv2
import numpy as np

try:
	com = str(subprocess.check_output(['netsh', 'wlan', 'show', 'interface' ]))
#print(com)#imprimir la secuencia de subproceso de los comandps
#print("\n")#salto de linea para ver la ejecucuión del comando anterior y diferenciarlo del resto
	Perfil = None #declaración de la variable sin valor para posteriormente asignarle uno 
	Password = None
	contr = com.split()#separo la cadena de texto en palabras indivisuales sin espacios ni saltos de línea, solo valores no vacio
#print(len(contr))#imprimo la cantidad de caracteres separados se han identificado con valor no nulo
#print(contr)#comprobacion del resultado de la función split()
#print("\n")#salto de linea para ver los diferentes puntos de ejecución
	for i in range(len(contr)): #bucle for en el rango de la longitud de caracteres encontrados de split()
		if contr[i] == "Perfil": #si la variable contrib coincide con "Perfil" 
			Perfil = contr[i+2]
		#print  (contr[i+2])#entonces imprimo la posicon +2 de contr, contando "Perfil" y ":""
	#print("Wi-Fi: ",Perfil)
	com2 = str(subprocess.check_output(['netsh', 'wlan', 'show', 'profile', Perfil, 'Key=clear']))
	contr2 = com2.split()
	for i in range(len(contr2)):
		if(contr2[i] == "clave"):
			Password = (contr2[i+2].split("\\r\\n\\r\\"))[0]
	#print("Password: ", Password)
	pass
	
except Exception as e:
	print("Something wrong") #Método de comprobación que todo se pudo realizar de  manera correcta
else:
	pass
finally:
	#Caracteristicas del texto para la red
	Text = "Wi-Fi: " + Perfil #Texto a poner en la imagen
	Place = (5,12) #Ubicación de l aimahen en pixeles donde irá el texto
	Font = cv2.FONT_ITALIC #Fuente de la letra
	Mesure = 0.45 #Medida de la letra
	ColourLetter = (10,10,10) #Color del texto con código html (Color negro)
	Thickness = 1 #Grosor de la letra

	#Caracteristicas del texto para la contraseña
	Text_ = "Password: " + Password #Texto a poner en la imagen
	Place_ = (5,27) #Ubicación de l aimahen en pixeles donde irá el texto
	Font_ = cv2.FONT_ITALIC #Fuente de la letra
	Mesure_ = 0.45 #Medida de la letra
	ColourLetter_ = (10,10,10) #Color del texto con código html (Color negro)
	Thickness_ = 1 #Grosor de la letra

	img = qr.wifi_qrcode(Perfil, True, 'WPA', Password)#Generación del código QR 
	img.save('Wifi_UAB.png')#Guardamos como imagen .png "img"
	image = cv2.imread('Wifi_UAB.png', 0)#opencv lo lee 
	cv2.putText(image,Text,Place,Font,Mesure,ColourLetter,Thickness)#Añadimos la red a la que nos vamos a conectar (solo información)
	cv2.putText(image, Text_, Place_, Font_, Mesure_, ColourLetter_, Thickness_)#Añadimos la contraseña de la red (solo información)
	cv2.imwrite("Wifi_UAB.png", image)#Actualizamos los datos de la imagen una vez añadido el texto en cuestion
	cv2.imshow('sample',image)#mostramos por pantalla el código Qr creado
	cv2.waitKey(5000)#Muestra por pantalla la imagen creada del código Qr durante 5 segundos 
