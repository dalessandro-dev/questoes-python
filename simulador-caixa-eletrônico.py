mensagem = """\n=== MENU DO CAIXA ELETRÔNICO ===
1 - Depositar
2 - Sacar
3 - Ver saldo
4 - Ver histórico de transações
5 - Sair"""

saldo = 1000.00
deposito = []
saque = []

while True:
  try:
    print(mensagem)
    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
      print("\n=== DEPÓSITO ===")

      valor = float(input("Digite o valor que deseja depositar: "))
      saldo += valor

      deposito.append(f"{valor:.2f}")

      print("Valor depositado com sucesso.")
    elif opcao == 2:
      print("\n=== SAQUE ===")

      valor = float(input("Digite o valor que deseja sacar: "))
      if valor > saldo:
        print("Saldo insuficiente.")
      else:
        saldo -= valor
        saque.append(f"{valor:.2f}")

        print("Valor sacado com sucesso.")
    elif opcao == 3:
      print("\n=== SALDO ===")
      print(f"Seu saldo é de R${saldo:.2f}")
    elif opcao == 4:
      print("\n=== HISTÓRICO DE TRANSAÇÕES ===")

      print("\n=== DEPÓSITOS ===")
      if not deposito:
        print("Nenhum depósito realizado.")
      else:
        for valor in deposito:
          print(f"\nR${valor}")
      
      print("\n=== SAQUES ===")
      if not saque:
        print("Nenhum saque realizado.")
      else:
        for valor in saque:
          print(f"\nR${valor}")

    elif opcao == 5:
      print("\nSaindo...")
        
      break
    else:
      print("Opção inválida. Tente novamente.")
  except ValueError:
    print("Digite um valor válido. Tente novamente.")
    continue
