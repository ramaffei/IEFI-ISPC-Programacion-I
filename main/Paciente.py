import pandas as pd
import datetime
import calendar

class Paciente:
   def __init__(self):
      self.datosPacientes=[]

   def datosP(self):
      print ("Le vamos a pedir los datos del paciente")

      while True:            
  
         try:                        
            self.nombre=input("Nombre: ")
            self.nombre=str(self.nombre)
            self.apellido=input("Apellido: ")
            self.apellido=str(self.apellido)

            self.nombreCompleto = self.nombre + self.apellido
        
            edad=input("Edad: ")
            edad=int(edad)

            genero=input("Género: \n 1 Femenino (marque 1) \n 2 Masculino (marque 2) \n 3 Otro (marque 3) \n")
            genero=int(genero)
            if genero <1 or genero >3:
               print('Marque 1, 2 ó 3 según el menú anterior:')
               genero=input("Género: \n 1 Femenino (marque 1) \n 2 Masculino (marque 2) \n 3 Otro (marque 3) \n")

            dni=input("DNI: ")
            dni=int(dni)
                
            cel=input("Teléfono móvil: ")
            cel=int(cel)

            break
            
         except (ValueError): 
            print("Error al ingresar los datos")        

      self.datosPacientes.append({'Nombre':self.nombre,'Apellido':self.apellido,'Edad':edad,'Género':genero,'DNI':dni,'Celular':cel})
      
