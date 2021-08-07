"""Criando uma classe para usar a data formatada de forma elegante."""

from datetime import datetime
now = datetime.now()

class Date:

    def __init__(self):
        self.day    = now.day
        self.month  = now.month
        self.year   = now.year
        self.hour   = now.hour
        self.minute = now.minute


    def date_visualization(self):
        print(f'{self.day}/{self.month}/{self.year}')


    def hour_visualization(self):
        print(f"{self.hour}:{self.minute}")