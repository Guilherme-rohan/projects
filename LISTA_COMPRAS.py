from time import sleep
"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar os valores de sua lista
Não permita que o programa quebre 
com erros de índices inexistente na lista.
"""
lista_compras = []

while True: 
        menu = str(input(''' 
[1] ADICIONAR COMPRAS
[2] APAGAR COMPRAS
[3] LISTAR COMPRAS
[4] SAIR
DIGITE QUAL É O SEU INTERESSE: '''))
        print('-='*50)
        try:
            if int(menu) in (1,2,3,4):
                if int(menu) == 1:
                    lista_compras.append(str(input('Adicione sua compra: ')))
                    sleep(0.5)
                    print('-='*50)
                    print('Produto adicionado com sucesso.')
                    print('-='*50)
                    sleep(0.5)
                    continue
                elif int(menu) == 2:
                    if not lista_compras:
                        print('NADA FOI ADICIONADO AINDA')
                        print('-='*50)
                        continue
                    print('Sua lista de compras é essa:')
                    print('-='*50)
                    sleep(0.2)
                    for i,j in enumerate(lista_compras):
                        sleep(0.2)
                        print(f'[{i}] -> {j}')
                        sleep(0.2)
                                      
                    try:
                        print('-='*50)
                        apagar = int(input('Digite o NUMERO DO valor que deseja apagar: '))
                        if 0 <= apagar < len(lista_compras):
                            sleep(0.5)
                            print('-='*50)
                            print(f'Produto "{lista_compras[apagar]}" apagado')
                            print('-='*50)
                            sleep(0.2)
                            lista_compras.pop(apagar)
                            continue
                        
                        else:
                            print('-='*50)
                            sleep(0.5)
                            print('PRODUTO NÃO ENCONTRADO')
                            print('-='*50)
                            continue
                    except:
                        sleep(0.5)
                        print('NUMERO DIGITADO INVÁLIDO')
                        print('-='*50)
                    
                elif int(menu) == 3:
                    if not lista_compras:
                        print('NADA FOI ADICIONADO AINDA')
                        print('-='*50)
                        continue
                    else:
                        for i,j in enumerate(lista_compras):
                            sleep(0.2)
                            print(f'[{i}] -> {j}')
                            sleep(0.2)
                        print('-='*50)       
                            
                                    
                elif int(menu) == 4:
                    print(f'{"OBRIGADO POR USAR NOSSO PROGRAMA":^100}')
                    break
        except:
            print('Digite um NUMERO VÁLIDO')
            print('-='*50)
