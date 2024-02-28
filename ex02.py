class Numbers():
    def __init__(self,number1, number2) -> None:
        self.number1 = number1
        self.number2 = number2

    def calculation(self):
        if self.number1 > self.number2:
            _ = self.number1
            self.number1 = self.number2
            self.number2 = _

        def isPrimo(number):
            if number <= 1:
                return False
            if number <= 3:
                return True
            if number % 2 == 0 or number % 3 == 0:
                return False
            i = 5
            while i * i <= number:
                if number % i == 0 or number % (i + 2) == 0:
                    return False
                i += 6
            return True
    
        primos = []
        for number in range(max(2, self.number1), self.number2):
            if isPrimo(number):
                primos.append(number)
        return primos

        
numbers = Numbers(5,20)
print(numbers.calculation())