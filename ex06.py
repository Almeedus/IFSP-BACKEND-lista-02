#Imports
import re

def validate_cpf(cpf):
    #Remove all characters that aren't digits
    cpf = re.sub(r'\D', '', cpf)
    
    #Validate if CPF have 11 digits
    if len(cpf) != 11:
        return False
    
    #Validate if all digits are the same, if are the same the function invalidates the CPF
    if cpf == cpf[0] * 11:
        return False
    
    #Calculating the first digit
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        resto = 0
    if resto != int(cpf[9]):
        return False
    
    # Calculating the second digit
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        resto = 0
    if resto != int(cpf[10]):
        return False
    
    return True

#Using
if __name__ == "__main__":
    cpf = input("Enter a CPF to validate: ")
    if validate_cpf(cpf):
        print("Valid CPF")
    else:
        print("Invalid CPF")

