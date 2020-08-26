import datetime
import PySimpleGUI as sg
from time import sleep

now = datetime.datetime.now()
current_time = now.strftime('%H:%M:%S')

algomais = ''
total = 0

while algomais != 'n' or 'N':
    print('')
    print('{:*^87}'.format(' COMIDAS E BEBIDAS '))
    print('')
    print('Data e Hora: {}/0{}/{}                                                        {}'.format
          (datetime.date.today().day, datetime.date.today().month, datetime.date.today().year, current_time))
    print('')
    print('|Nº|  |COMIDA|                    |PREÇO|  |  |Nº|  |BEBIDA|                    |PREÇO|')
    print('(1)   X-Burguer                   R$ 8,00  |  (11)  Refrigerante (lata)         R$ 5,00')
    print('(2)   X-Salada                    R$10,00  |  (12)  Refrigerante (2 litros)     R$ 7,00')
    print('(3)   X-Calabresa                 R$12,00  |  (13)  Cerveja (lata)              R$ 6,00')
    print('(4)   X-Coração                   R$15,00  |  (14)  Cerveja (garrafa)           R$ 8,00')
    print('(5)   X-Frango                    R$18,00  |  (15)  Suco Natural (300ml)        R$ 8,00')
    print('(6)   X-Tudo                      R$25,00  |  (16)  Taça de Vinho (200ml)       R$12,00')
    print('(7)   Porção de Aipim (500g)      R$10,00  |  (17)  Chopp de Vinho (500ml)      R$10,00')
    print('(8)   Porção de Aipim (1kg)       R$15,00  |  (18)  Caipirinha (350ml)          R$ 8,00')
    print('(9)   Porção de Fritas (500g)     R$12,00  |                                           ')
    print('(10)  Porção de Fritas (1kg)      R$20,00  |                                           ')
    print('')
    print('---------------------------------------------------------------------------------------')

    qtd = int(input('Quantidade do item: '))

    pedido = int(input('Número do Item: '))

    if pedido > 18:
        print('ITEM INVÁLIDO!')

    if pedido == 1:
        print('{}und. X-BURGUER.'.format(qtd))
        total = total + (qtd * 8)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 2:
        print('{}und. X-SALADA.'.format(qtd))
        total = total + (qtd * 10)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 3:
        print('{}und. X-CALABRESA.'.format(qtd))
        total = total + (qtd * 12)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 4:
        print('{}und. X-CORAÇÃO.'.format(qtd))
        total = total + (qtd * 15)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 5:
        print('{}und. X-FRANGO.'.format(qtd))
        total = total + (qtd * 18)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 6:
        print('{}und. X-TUDO.'.format(qtd))
        total = total + (qtd * 25)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 7:
        print('{}und. POR. AIPIM (500G).'.format(qtd))
        total = total + (qtd * 10)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 8:
        print('{}und. POR.AIPIM (1KG).'.format(qtd))
        total = total + (qtd * 15)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 9:
        print('{}und. POR. FRITAS (500G).'.format(qtd))
        total = total + (qtd * 12)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 10:
        print('{}und. POR FRITAS (1KG).'.format(qtd))
        total = total + (qtd * 20)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 11:
        print('{}und. REFRIGERANTE (LATA).'.format(qtd))
        total = total + (qtd * 5)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 12:
        print('{}und. REFRIGERANTE (2L).'.format(qtd))
        total = total + (qtd * 7)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 13:
        print('{}und. CERVEJA (LATA).'.format(qtd))
        total = total + (qtd * 6)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 14:
        print('{}und. CERVEJA (GARRAFA).'.format(qtd))
        total = total + (qtd * 8)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 15:
        print('{}und. SUCO NATURAL.'.format(qtd))
        total = total + (qtd * 8)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 16:
        print('{}und. TAÇA DE VINHO.'.format(qtd))
        total = total + (qtd * 12)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 17:
        print('{}und. CHOPP DE VINHO.'.format(qtd))
        total = total + (qtd * 10)
        print('TOTAL: R${:.2f}!'.format(total))
    elif pedido == 18:
        print('{}und. CAIPIRINHA.'.format(qtd))
        total = total + (qtd * 8)
        print('TOTAL: R${:.2f}!'.format(total))

    print('[1] Sim')
    print('[2] Não')

    algomais = input('Algo mais? ').lower()

    if algomais == '2':
        break

# ****************************************  PAGAMENTO  ****************************************

print('{:-^87}'.format(' PAGAMENTO '))
print('')
print('[1] DINHEIRO - À vista')
print('[2] CARTÃO   - À vista/Parcelado')
print('')

pagamento = int(input('Digite a forma de pagamento: '))

if pagamento == 1:
    pago = float(input('Valor pago: R$'))
    troco = pago - total
    print('TROCO: {:.2f}!'.format(troco))
else:
    print('PAGAMENTO EFETUADO NO CARTÃO. CONFIRA O IMPRESSO PELA MÁQUINA!')


# ****************************************  WHATSAPP  ****************************************

numped = ('{}' + '{}' + '{}' + '{}').format(datetime.date.today().day, datetime.date.today().month,
                                            datetime.date.today().year, now.strftime('%H%M%S'))

print('{:-^87}'.format(' WHATSAPP '))
print('')
print('[1] Sim')
print('[2] Não')
whatsapp = int(input('Deseja informar o Whatsapp? '))

if whatsapp == 1:
    contato = input('Digite o número do cliente: ')
    nome = str(input('Digite o nome do cliente: '))

    arquivo = open('clientes.txt', 'a')
    arquivo.write('{}: {}\n'.format(nome, contato))
    print('Operação concluída no arquivo')
    arquivo.close()

# ****************************************  IMPRESSÃO  ***************************************

print('{:-^87}'.format(' IMPRESSÃO '))
print('')

print('[1] Sim')
print('[2] Não')
impressao = int(input('Deseja imprimir a via do cliente? '))

if impressao == 1:
    sg.popup('Impressão à caminho!')

print('{:-^87}'.format(' FIM! '))
print('O programa se encerrará em 10 segundos*')

sleep(10)
