saldo = 0

while True:
    print('\n ---- CAIXA ELETRÔNICO ----')
    print('1 - Ver Saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print(f'Seu saldo é R$ {saldo}')
    elif opcao == '2':
        valor = float(input('Digite o valor para depósito: R$ '))
        saldo += valor
        print('Depósito realizado com sucesso!')
    elif opcao == '3':
        valor = float(input('Digite o valor do saque: R$ '))

        if valor > saldo:
            print('Saldo Insuficiente!')
        else:
            saldo -= valor
            print('Saque realizado com sucesso!')
            print(f'Saldo restante: R$ {saldo:.2f}')
    elif opcao == '4':
        print('Encerrando o Sistema')
        break
    else:
        print('Opção inválida')
