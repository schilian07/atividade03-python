#Questão 1
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}'
    
    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        return f'Olá, {self.nome}! Como está a vida de {self.profissao}?'

pessoa = Pessoa('João Vitor', 17, 'Vendedor')

print(pessoa)

pessoa.aniversario()
print(f'Idae após aniversário: {pessoa.idade}')

print(pessoa.saudacao)

    
#Questão 2
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self):
        return f'Titular: {self.titular}, Saldo: R${self.saldo:.3f}'
    
#Questão 3   
#Instanciando e imprimindo instâncias de ContaBancaria
conta1 = ContaBancaria('Anna Lucia', 47.000)
conta2 = ContaBancaria('Murilo Camillo', 65.000)

print(conta1)
print(conta2)

#Questão 4
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False
    
    def __str__(self):
        return f'Titular: {self.titular}, Saldo: R${self.saldo:.4f}'

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

    @property
    def ativo(self):
        return self._ativo
    
    @ativo.setter
    def ativo(self, value):
        self._ativo = value

conta = ContaBancaria('João Vitor', 100.000)
ContaBancaria.ativar_conta(conta)
print(conta.ativo)

#Questão 5
class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular: {self.titular}, Saldo: R${self.saldo:.4f}'

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo

    @ativo.setter
    def ativo(self, value):
        self._ativo = value
#Questão 6
#Instãncia que imprime o valor da propriedade titular
conta = ContaBancaria('João Vitor', 100.000)
print(conta.titular)
    
#Questão 7
class ClienteBanco:
    def __init__(self, nome, idade, cpf, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

cliente1 = ClienteBanco('Murillo Camillo', 17, '123.456.789-00', 'Rua A, 123', '99999-9999')
cliente2 = ClienteBanco('Anna Lucia', 17, '987.654.321-00', 'Av. B, 456', '88888-8888')
cliente3 = ClienteBanco('João Vitor', 17, '111.222.333-00', 'Trav. C, 789', '77777-7777')

#Questão 8
class ClienteBancoVip:
    def __init__(self, nome, idade, cpf, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    @classmethod
    def criar_cliente_vip(cls, nome, cpf):
        return cls(nome, 0, cpf, 'Endereço VIP', 'Telefone VIP')
    
    def __str__(self):
        return (f'Nome: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}, ' 
                f'Endereço: {self.endereco}, Telefone: {self.telefone}')
    

cliente_vip = ClienteBancoVip('João VIP', 17, '111.222.333-00','Trav. C, 789', '77777-7777')
print(cliente_vip)
