"""
Criar um programa que receba duas datas e exiba o número de dias de diferença entre elas.
Resolver utilizando Classes e objetos, passando as datas como parâmetros.
Verificar na linguagem escolhida se há um método, função ou API específica para datas.
"""
import datetime
class Dates():
    def __init__(self) -> None:
        pass

    def diference_between_dates(self, date1: datetime.date, date2: datetime.date):
        diference = date1 - date2
        num_days = diference.days

        return abs(num_days)

date = Dates()
print(date.diference_between_dates(datetime.date(2023,12,1),datetime.date(2024, 1, 29)))