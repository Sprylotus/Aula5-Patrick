import os

os.system ('cls')
print(30*'=')


# turno = int(input('Informe o número do turno: '))

# match turno:
#     case 1:
#         print('Manhã')
#     case 2:
#         print('Tarde')
#     case 3:
#         print('Noite')
#     case _:
#         print('Turno inválido')

# n = int(input('Informe um número entre 1 e 6: '))


# match n:
#     case 1:
#         print('Janeiro')
#     case 2:
#         print('Fevereiro')
#     case 3:
#         print('Março')
#     case 4:
#         print('Abril')
#     case 5:
#         print('Maio')
#     case 6:
#         print('Junho')
#     case _:
#         print('Número inválido')


# print('\n[1] Chinês \n[2] Italiano \n[3] Mexicano \n[4] Vegetariano')

# opcao = int(input('Informe o restaurante desejado e receba uma recomendação: '))

# match opcao:
#     case 1:
#         print('Yakisoba')
#     case 2:
#         print('Macarrão')
#     case 3:
#         print('Taco')
#     case 4:
#         print('Salada')
#     case _:
#         print('Tipo de restaurante inválido')


alt1 = int(input('Escolha um número: '))
print(f'A opção que você escolheu foi {alt1}')

alt2 = int(input('Informe um número de 1 a 4: '))

print('\n[1] Adicionar Item \n[2] Remover Item \n[3] Listar Itens \n[4] Sair')

match alt2:
    case 1:
        print(alt1 + 1)
    case 2:
        print(alt1 - 1)
    case 3:
        print(f'{alt1} e {alt2}')
    case 4:
        print('Saindo...')
    case _:
        print('Opção inválida')


