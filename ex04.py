"""
Criar um programa que exiba o resultado das operações soma, subtração,
multiplicação, radiciação e fatorial com o uso de objetos e métodos.
 
Para o cálculo do fatorial, procure usar métodos recursivos.
"""

class Operations():
    def __init__(self) -> None:
        pass

    def sum(self, *args):
        if all(isinstance(arg, (int, float)) for arg in args):
            sum_result = 0
            for arg in args:
                sum_result += arg
            return sum_result
        else:
            return 'Please enter a valid value.'
        
    def subtraction(self, *args):
        if all(isinstance(arg, (int, float)) for arg in args):
            sub_result = args[0]
            for arg in args:
                if arg == args[0]:
                    continue
                sub_result -= arg
            return sub_result
        else:
            return 'Please enter a valid value.'
        
    def multiplication(self, *args):
        if all(isinstance(arg, (int, float)) for arg in args):
            mult_result = args[0]
            for arg in args:
                if arg == args[0]:
                    continue
                mult_result *= arg
            return mult_result
        else:
            return 'Please enter a valid value.'
        
    def rooting(self, arg):
        if isinstance(arg, (int, float)):
            if arg < 0:
                return "Não é possível calcular a raiz quadrada de um número negativo."
    
            if arg == 0:
                return 0
    
            # Start with a inicial stimated that is equal to half of 'arg' 
            estimate = arg / 2

            # Defines the accurary of the method 
            accuracy = 0.01

            # Apply the Newton-Rapson method 
            while True:
                next_estimate = (estimate + arg / estimate) / 2
                if abs(next_estimate - estimate) < accuracy:
                    return next_estimate
                estimate = next_estimate
        
            #Teacher in this rooting calculation, the estimated never be 0 even in 
            #numbers with exact roots, because in here the code makes an estimate. 
            #It is doing divisions as close to 0, that's why I'm using ':.2f' when showing the result.
        else:
            return 'Please enter a valid value.'

    def factorial(self, arg):
        if isinstance(arg, (int, float)):
            if arg == 0:
                return 1
            
            return arg * operation.factorial(arg-1)
        else:
            return 'Please enter a valid value.'

operation = Operations()

print('1.Sum')
print(operation.sum(2,2.1))
print(operation.sum('12'))
print('2.Subtraction')
print(operation.subtraction(100,20.1))
print(operation.subtraction('12'))
print('3.Multiplication')
print(operation.multiplication(2,2.2))
print(operation.multiplication('12'))
print('4.Rooting')
print(f'{operation.rooting(25):.2f}')
print(operation.rooting('12'))
print('5.Factorial')
print(operation.factorial(5))
print(operation.factorial('12'))