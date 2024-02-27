"""
1 – Criar um programa de cadastro de Clientes com nome, endereço, Cep e CPF. Utilizar os
recursos de Classes e objetos. Encapsular todos os atributos para que possam ser alterados e
lidos apenas utilizando métodos de acesso. Para cada cliente informado, exibir os dados na tela
ao final da inserção de dados. Realizar a validação dos dados usando RegEX.
"""

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
    def get_cpf(self):
        return self.__cpf
    def get_adress(self):
        return self.__adress
    def get_cep(self):
        return self.__cep
    
client1 = Client('Eduardo', 'São Miguel Arcanjo', '18230-000', '490.822.938-46')
client2 = Client('Eliana', 'São Miguel Arcanjo', '18230-000', '454.265.542-12')


print('CLIENTS')
print(client1.get_client())
print(client2.get_client())