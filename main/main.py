import pandas as pd
import datetime
import calendar
from Paciente import *
from Turnero import *

if __name__ == "__main__":

   odonto = Especialidad('Odontología', 1, 'Luciana Altamirano', '01:00')
   oftalmo = Especialidad('Oftalmología', 2, 'Roberto Garcia', '00:20')
   gineco = Especialidad('Ginecología', 3, 'Pedro Menuan', '00:30')
   clinico = Especialidad('Médico Clínico', 4, 'Alejandra Ilgaramo', '00:25')

   turnero = Agenda('22 al 26 de noviembre')

   especialidades = [odonto, oftalmo, gineco, clinico,]
   for especialidad in especialidades:
      especialidad.turnero = turnero
      especialidad.establecerTurnos(11,3,7)

   pediatra = Especialidad('Pediatría', 5, 'Analia Montalvan', '00:40')
   pediatra.turnero = turnero
   pediatra.establecerTurnos(11,3,[1,3,5])

   especialidades.append(pediatra)

   print("""
   Bienvenido al TURNERO del Centro de Salud Comunitario.
      La atención es de lunes a viernes de 10 a 17 hs.
   """)
   paciente = Paciente()
   paciente.datosP()
   paciente.datosPacientes
 

   print("""
   ¿Para cuál especialidad quiere pedir un turno?
   """)

   for i in range(len(especialidades)):
      print(i+1,'-',especialidades[i].nombre,'( marque',i+1,')')

   espe_elegida=input('Marque el número de la especialidad: ')
   espe_elegida=int(espe_elegida)-1

   print(espe_elegida)

   print("""
   ---------------------------------------------------------

   La semana habilitada es del 22 al 26 de noviembre de 2021
   ¿Para cuál día desea consultar los horarios disponibles?       
   """)

   especialidades[espe_elegida].asignarTurno(paciente.nombreCompleto)
   