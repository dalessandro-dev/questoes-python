**Explicação do Código**

Este projeto simula um sistema básico de banco, onde é possível cadastrar contas, consultar saldo, depositar, sacar e transferir dinheiro entre contas.

**Classes Principais**

*Conta*

É uma classe abstrata que representa uma conta bancária genérica.

Ela controla:
• Nome do titular
• CPF
• Tipo da conta
• Número da conta (gerado automaticamente)
• Saldo

Métodos
get_numero() ->	Retorna o número da conta
get_saldo()	-> Retorna o saldo atual
creditar(valor) -> Adiciona dinheiro ao saldo
debitar(valor) -> Remove dinheiro do saldo (se tiver saldo suficiente)

*ContaCorrente*

Herda tudo da classe Conta, mudando apenas o tipo da conta para “corrente”.

*Banco*

Responsável por armazenar e gerenciar as contas cadastradas.
Ele possui uma lista que guarda até 100 contas.

Métodos
cadastrar(conta) -> Adiciona uma nova conta ao banco
procurar_conta(numero) -> Busca uma conta pelo número
debitar(numero, valor) -> Realiza saque em uma conta
creditar(numero, valor) -> Realiza depósito
transferir(origem, destino, valor) -> Transfere saldo entre contas
consultar_saldo(numero) -> Mostra o saldo da conta

**Parte Interativa (main())**

O sistema funciona em loop mostrando um menu para o usuário:

1. Criar uma nova conta corrente
2. Procurar conta por número
3. Sacar dinheiro
4. Depositar dinheiro
5. Transferir dinheiro entre contas
6. Consultar saldo
7. Sair do programa

Sempre que o usuário escolhe uma opção, o programa pede os dados necessários e chama os métodos do banco.