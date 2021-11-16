import pandas as pd
import datetime
import calendar
from Paciente import *
from Turnero import *

if __name__ == "__main__":

   turnero_vacunacion = Agenda('Vacunacion')

   vacunacion = Vacunacion('1', 'Covid', '1')
   vacunacion.turnero = turnero_vacunacion
   vacunacion.establecerTurnos(11,3,1)

   menor = Infante('10kg','1mt','Pedro Alberto','Paula Montenegro')

   vacunacion.asignarTurno(menor)
   