# ****************************************  MENU  ****************************************

print('')
print('{:*^80}'.format(' COMIDAS E BEBIDAS '))
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
print('(9)   Porção de Fritas (500g)     R$12,00  |                                          ')
print('(10)  Porção de Fritas (1kg)      R$20,00  |                                          ')
print('')

print('--------------------------------------------------------------------------------------')

pedido = int(input('Número do Item: '))
qtd = int(input('Quantidade: '))
total = 0

if pedido > 18:
    print('\033[32mITEM INVÁLIDO!\033[m')

if pedido == 1:
    print('\033[31m{}und. X-BURGUER.\033[m'.format(qtd))
    total = qtd * 8
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 2:
    print('\033[31m{}und. X-SALADA.\033[m'.format(qtd))
    total = qtd * 10
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 3:
    print('\033[31m{}und. X-CALABRESA.\033[m'.format(qtd))
    total = qtd * 12
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 4:
    print('\033[31m{}und. X-CORAÇÃO.\033[m'.format(qtd))
    total = qtd * 15
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 5:
    print('\033[31m{}und. X-FRANGO.\033[m'.format(qtd))
    total = qtd * 18
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 6:
    print('\033[31m{}und. X-TUDO.\033[m'.format(qtd))
    total = qtd * 25
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 7:
    print('\033[31m{}und. POR. AIPIM (500G).\033[m'.format(qtd))
    total = qtd * 10
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 8:
    print('\033[31m{}und. POR.AIPIM (1KG).\033[m'.format(qtd))
    total = qtd * 15
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 9:
    print('\033[31m{}und. POR. FRITAS (500G).\033[m'.format(qtd))
    total = qtd * 12
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 10:
    print('\033[31m{}und. POR FRITAS (1KG).\033[m'.format(qtd))
    total = qtd * 20
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 11:
    print('\033[31m{}und. REFRIGERANTE (LATA).\033[m'.format(qtd))
    total = qtd * 5
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 12:
    print('\033[31m{}und. REFRIGERANTE (2L).\033[m'.format(qtd))
    total = qtd * 7
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 13:
    print('\033[31m{}und. CERVEJA (LATA).\033[m'.format(qtd))
    total = qtd * 6
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 14:
    print('\033[31m{}und. CERVEJA (GARRAFA).\033[m'.format(qtd))
    total = qtd * 8
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 15:
    print('\033[31m{}und. SUCO NATURAL.\033[m'.format(qtd))
    total = qtd * 8
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 16:
    print('\033[31m{}und. TAÇA DE VINHO.\033[m'.format(qtd))
    total = qtd * 12
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 17:
    print('\033[31m{}und. CHOPP DE VINHO.\033[m'.format(qtd))
    total = qtd * 10
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))
elif pedido == 18:
    print('\033[31m{}und. CAIPIRINHA.\033[m'.format(qtd))
    total = qtd * 8
    print('\033[32mTOTAL: R${:.2f}!\033[m'.format(total))


# ****************************************  PAGAMENTO  ****************************************


print('{:-^86}'.format(' PAGAMENTO '))
print('')
print('[1] DINHEIRO - À vista')
print('[2] CARTÃO   - À vista/Parcelado')
print('')

pagamento = int(input('Digite a forma de pagamento: '))

if pagamento == 1:
    pago = float(input('Valor pago: R$'))
    troco = pago - total
    print('\033[32mTROCO: {:.2f}!\033[m'.format(troco))
else:
    print('\033[32mPAGAMENTO EFETUADO NO CARTÃO. CONFIRA O IMPRESSO PELA MÁQUINA!\033[m')

print('{:-^86}'.format(' FIM! '))
