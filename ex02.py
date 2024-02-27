"""
Criar um programa com Classes e Objetos que tenha um método chamado “contaPrimos( )”.
 Este método recebe como parâmetro dois números inteiros positivos, sendo o primeiro menor do que o segundo. 
 O retorno do método será a quantidade de números primos encontrados do primeiro ao segundo valor informado. 
 
 Ex: (‘obj’ é um objeto qualquer a escolha do aluno) x = obj.contaPrimos(5, 20) → x terá o valor 6, já que de 5 até 20 existem seis números primos.
"""

class Numbers():
    def __init__(self,number1, number2) -> None:
        self.number1 = number1
        self.number2 = number2

    def calculo(self, number1, number2):
        if number1 > number2:
            _ = number1
            number1 = number2
            number2 = _

        








"""
primo -
numero divisivel por 1 e por ele mesmo
"""
