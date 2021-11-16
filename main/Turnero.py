import pandas as pd
import datetime
import calendar

class Agenda:

   def __init__(self, nombre, datos = pd.DataFrame([])):
      self.nombre = nombre
      self.csv = nombre+'.csv'
      self.__guardadEnCsv(datos)

   def __guardadEnCsv(self, datos):
      datos.to_csv(self.csv)

   def leerDatos(self):
      return pd.read_csv(self.csv, index_col=0)
   
   def mostrarDatos(self):
      print(self.leerDatos())
   
   def insertarDatos(self, datos):
      df = self.leerDatos()
      df = pd.concat([df, datos], axis=0, ignore_index=True)
      self.__guardadEnCsv(df)
   
   def columnasDias(self):
      df = self.leerDatos()
      df = df.columns.values[3:]
      return list(df)   

   def guardarTurno(self, id_espe, paciente, dia, horario):
      df = self.leerDatos()
      df.loc[(df['id_espe']==id_espe) & (df['Horario']==horario), dia] = paciente
      self.insertarDatos(df)

class Especialidad:
   diasDeLaSemana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
   horaApertura = '10:00'
   horaCierre = '17:00'

   def __init__(self, nombre, id, medico, duracionTurno):
      self.nombre = nombre
      self.id = id
      self.medico = medico
      self.duracionTurno = duracionTurno
      self.__dias = []

   def establecerDias(self, diaInt = 0):
      if diaInt == 0:
         print("Debe establecer los dias de atencion")
         for i in range(len(self.diasDeLaSemana)):
            print (i+1,'-', self.diasDeLaSemana[i])
         print("7 - Lunes a viernes")
         print("8 - TODOS")
         print("0 - SALIR")

         diaInt = int(input("Por favor seleccione los días de atencion de la especialidad, o 0 (cero) para salir"))

      elif (diaInt == 7):
         dias = list(range(0,5))
      elif (diaInt == 8):
         dias = list(range(0,6))
      elif (isinstance(diaInt, list)):
         dias = [x-1 for x in diaInt]
      else:
         dias = []
         while diaInt != 0:
            dias.append(diaInt-1)
            diaInt = int(input("Por favor seleccione los días de atencion de la especialidad, o 0 (cero) para salir"))

      self.__dias = dias
      
   def __formatSemana(self, anio, mes, semana):
      calen = calendar.Calendar()
      semana = calen.monthdayscalendar(anio, mes)[semana]
      diaDelaSemana = self.diasDeLaSemana
      dias = []
      for i in self.__dias:
         dias.append(diaDelaSemana[i]+' '+str(semana[i])+'/'+str(mes))
      return dias

   def establecerTurnos(self, mes, semana, dias = 0):
      anio = 2021

      if (len(self.__dias) == 0):
         self.establecerDias(dias)

      self.diasDisponibles = self.__formatSemana(anio, mes, semana)
      
      if not len(self.diasDisponibles) == 0:
         encabezados = ['id_espe','Especialidad','Horario']+self.diasDisponibles
         inicio = datetime.datetime.strptime(self.horaApertura, '%H:%M')
         turno = datetime.datetime.strptime(self.duracionTurno, '%H:%M')
         time_zero = datetime.datetime.strptime('00:00', '%H:%M')
         final = datetime.datetime.strptime(self.horaCierre, '%H:%M')
         
         final = final - turno + time_zero
         
         filas = []
         while inicio <= final:
            fila = [self.id, self.nombre, inicio.time()]+['disponible' for x in range(len(self.diasDisponibles))]
            inicio = inicio - time_zero + turno
            filas.append(fila)

         df = pd.DataFrame(filas, columns=encabezados)
         #print(df)

      self.turnero.insertarDatos(df)

   def traerDisponibles(self):
      df = self.turnero.leerDatos()
      df = df[df['id_espe'].eq(self.id)]
      df = df.loc[:, ['Horario']+self.diasDisponibles]
      return df

   def asignarTurno(self,paciente):
      disponibles = self.traerDisponibles()
      dias = disponibles.columns.values[1:]
      for i in range(len(dias)):
         print (str(i+1),'-',dias[i])
      
      dia = int(input("Selecciona un día para el turno (ingresa el numero correspondiente a la opcion"))

      diaElegido = dias[dia-1]

      horariosDisponibles = self.horario(diaElegido)
      print(horariosDisponibles)

      horarioElegido = int(input("Selecciona el horario: ingresa el numero correspondiente a la opcion"))

      horarioElegido = horariosDisponibles.loc[0, 'Horario']
      

      self.turnero.guardarTurno(self.id, paciente, diaElegido, horarioElegido)

   def horario(self, dia):
      df = self.turnero.leerDatos()
      df = df[df['id_espe'].eq(self.id)]
      df = df[['Horario']][df[dia] == 'disponible']
      return df.reset_index(drop=True)

