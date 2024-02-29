from math import pi

class Calculation():
    def __init__(self) -> None:
        pass
        
    def calc_func(self, *args):
        if len(args) == 1:
            if isinstance(args[0], float):
                radius = args[0]
                return pi * radius ** 2

        elif len(args) == 2:
            if all(isinstance(arg, float) for arg in args):
                side1, side2 = args
                return side1 * side2
            elif isinstance(args[0], int) and isinstance(args[1], float):
                base, height = args
                return 0.5 * base * height
        
        elif len(args) == 3:
            if all(isinstance(arg, int) for arg in args):
                sideA, sideB, sideC = args
                return sideA + sideB + sideC

            elif all(isinstance(arg, tuple) and len(arg) == 2 for arg in args):
                x1, y1 = args[0]
                x2, y2 = args[1]
                x3, y3 = args[2]
                return 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
            
        else:
            return 'Incorrect Use'

calculation = Calculation()
print(calculation.calc_func(5.0))
print(calculation.calc_func(4.0,3.0))
print(calculation.calc_func(3,4,5))
print(calculation.calc_func(4,5.0))
print(calculation.calc_func((0,0), (3,0), (0,4)))
print(calculation.calc_func("Text"))