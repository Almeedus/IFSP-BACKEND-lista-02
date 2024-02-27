#Imports
import ex06

#Client class - read and update data
class Client():
    def __init__(self, name, adress, cep, cpf) -> None:
        self.__name = name
        self.__adress = adress
        self.__cep = cep
        self.__cpf = cpf

    def get_client(self):
        return f'{self.__name} - {self.__cpf} | {self.__adress} - {self.__cep}'
    
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_cpf(self):
        return self.__cpf
    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_adress(self):
        return self.__adress
    def set_adress(self, adress):
        self.__adress = adress

    def get_cep(self):
        return self.__cep
    def set_cep(self, cep):
        self.__cep = cep
    
#Object client 
client1 = Client('Eduardo', 'São Miguel Arcanjo', '18230-000', '490.120.938-46')
options = ['Show Client', 'Update Client', 'Exit']

while True:
    print('Clients')
    for x, y in enumerate(range(3)):
        print(f'{x+1}. {options[y]}')

    option = int(input("What's your choise? "))
    if option == 1:
        print(client1.get_client())
    elif option == 2:
        name = input("New name: ")
        adress = input('New adress: ')
        cep = input('New CEP: ')
        cpf = input('New CPF: ')

        if name != '':
            client1.set_name(name=name)
        if adress != '':
            client1.set_adress(adress=adress)
        if cep != '':
            client1.set_cep(cep=cep)
        if cpf != '':
            #CPF valitation with RegEX
            if ex06.validate_cpf(cpf=cpf):
                client1.set_cpf(cpf=cpf)
            
    elif option == 3:
        break
    else: 
        print('Enter a valid value.')