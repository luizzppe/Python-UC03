class ContaCorrente:
    def __init__(self, nome_cliente, num_conta, senha, saldo = 0.0,):          
        self.nome_cliente = nome_cliente
        self.num_conta = num_conta
        # self.agencia = agencia
        self.saldo = saldo
        self.senha = senha
        # self.cheque_especial = cheque_especial
        # self.cartao_credito = cartao_credito
        # self.financiamento = financiamento
        

    def mostrar_saldo(self):
        print(f"O saldo de {self.nome_cliente} agora é {self.saldo:.2f}")

    def sacar(valor,self):
        if 0 < valor < self.saldo:
            self.saldo -= valor
            print(f"Seu saque de R${valor:.2f} foi efeutado!")
            print(f"Seu saldo agora é: {self.saldo:.2f}")
        else:
            print("Não é possivel efetuar saques maiores que o valor na conta ou menores/iguais a zero")

    def depositar(valor,self):
        if valor > 0:
            self.saldo += valor
            print(f"Seu deposito de {valor:.2f} foi realizado, ")
            print(f"Seu saldo agora é: {self.saldo:.2f}")

    def transferir(self, valor, destinatario):
        if self.num_conta != destinatario.num_conta:
            ContaCorrente.sacar(valor,self)
            ContaCorrente.depositar(destinatario, valor)
        else:
            print("Você não pode realizar transferencias para si mesmo")