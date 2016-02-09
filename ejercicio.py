#!/usr/bin/python
# -*- coding: utf-8 -*-
# Sistemas Teleco. Sara Suárez.

fd = open('/etc/passwd', 'r')
lineas = fd.readlines()

diccionario_users = {}
for linea in lineas:
	elementos = linea.split(':')
	user = elementos[0]
	shell = elementos[-1]
        diccionario_users[user]=[shell]

print "Usuario root:", diccionario_users.get("root")  #De esta forma no salta una excepción

try:
    diccionario_users['imaginario']   #Uso esta forma para que me salte una excepción y manejarla
except KeyError:
    print "Error: Este usuario no existe"
    
num_users = len(lineas)
print "Hay", num_users, "usuarios"

fd.close()


