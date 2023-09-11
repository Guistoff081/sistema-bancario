import datetime

class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        self.extrato = []
        self.saque_diario = {'data_ultimo_saque': None, 'saques': 0, 'valor_total': 0}

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"{self._get_data_hora()} - Depósito de R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            hoje = datetime.date.today()
            if self._verificar_limite_diario_saque(valor, hoje):
                self.saldo -= valor
                self.extrato.append(f"{self._get_data_hora()} - Saque de R$ {valor:.2f}")
                self.saque_diario['data_ultimo_saque'] = hoje
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Você atingiu o limite diário de saques ou excedeu o limite de saque por operação.")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def ver_extrato(self):
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("\n=================== EXTRATO ===================")
            print(f"Extrato da conta de {self.titular}:")
            for transacao in self.extrato:
                print(transacao)
            print(f"Saldo atual: R$ {self.saldo:.2f}")
            print("\n===============================================")

    def _verificar_limite_diario_saque(self, valor, hoje):
        if self.saque_diario['data_ultimo_saque'] != hoje:
            self.saque_diario['data_ultimo_saque'] = hoje
            self.saque_diario['saques'] = 0
            self.saque_diario['valor_total'] = 0
        if self.saque_diario['saques'] < 3 and valor <= 500:
            self.saque_diario['saques'] += 1
            self.saque_diario['valor_total'] += valor
            return True
        return False

    def _get_data_hora(self):
        agora = datetime.datetime.now()
        return agora.strftime("%Y-%m-%d %H:%M:%S")


def main():
    menu = """
      [c] Configurar conta
      [d] Depositar
      [s] Sacar
      [e] Ver extrato da conta
      [q] Sair
      =>
    """
    print("Bem vindo ao GuigoBank!")
    titular = input("Digite o nome do titular da conta: ")
    conta = ContaBancaria(titular)

    while True:
        print(f"Olá, {titular}! Selecione a opção desejável:")
        print(menu)
        opcao = input().lower()

        if opcao == 'c':
            titular = input("Digite o nome do novo titular da conta: ")
            conta = ContaBancaria(titular)
            print(f"Conta configurada para {titular}.")

        elif opcao == 'd':
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)

        elif opcao == 's':
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)

        elif opcao == 'e':
            conta.ver_extrato()

        elif opcao == 'q':
            print("Saindo do sistema. Obrigado!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
