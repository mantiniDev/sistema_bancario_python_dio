# Desafio - Sistema Bancário

menu = """
BEM VINDO AO BANCO DIO.
DIGITE UMA DAS OPÇÕES PARA CONTINUAR:

[d] DEPOSITAR
[s] SACAR
[e] EXTRATO
[q] SAIR

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

MENSAGEM_ERRO = """
========================================
      #### OPERAÇÃO INVÁLIDA #### 
# SELECIONE UMAS DAS OPÇÕES NOVAMENTE #]
========================================

"""
MENSAGEM_ERRO_VALOR = """
========================================
      #### OPERAÇÃO INVÁLIDA #### 
     # VALOR INSERIDO INCORRETO #]
========================================

"""
MENSAGEM_LIMITE_SAQUES = """
======================================
     #### ERRO NA OPERAÇÃO #### 
# LIMITE DE SAQUES DIÁRIOS EXCEDIDO # 
======================================

"""
MENSAGEM_MAIOR_LIMITE = """
================================================
            #### ERRO NA OPERAÇÃO #### 
# VALOR DE SAQUE DEVE SER MENOR QUE R$ 500.00 #
================================================

"""
MENSAGEM_MAIOR_SALDO = """
=============================
  #### ERRO NA OPERAÇÃO #### 
# VALOR MAIOR QUE O SALDO #
=============================

"""
MENSAGEM_SUCESSO = """
===============================
#### OPERAÇÃO BEM SUCEDIDA #### 
===============================

"""

# ------funções
def func_deposito(valor_deposito):
    global saldo
    global extrato
    global MENSAGEM_ERRO_VALOR
    global MENSAGEM_SUCESSO
    
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"  
        print(MENSAGEM_SUCESSO) 
    else:
        print(MENSAGEM_ERRO_VALOR)
    
def func_saque(valor_saque):
    global saldo
    global numero_saques
    global limite
    global extrato
    global MENSAGEM_LIMITE_SAQUES
    global MENSAGEM_MAIOR_LIMITE
    global MENSAGEM_MAIOR_SALDO
    global MENSAGEM_SAQUE_SUCESSO
    
    saque_maior_saldo = valor_saque > saldo
    saque_maior_limite = valor_saque > limite
    saque_maior_diario = numero_saques >= LIMITES_SAQUES
    
    if saque_maior_saldo:
        print(MENSAGEM_MAIOR_SALDO)
    
    elif saque_maior_limite:
       print(MENSAGEM_MAIOR_LIMITE)
    
    elif saque_maior_diario:
        print(MENSAGEM_LIMITE_SAQUES)
    
    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        numero_saques += 1
        print(MENSAGEM_SUCESSO)
    
    else:
        print(MENSAGEM_ERRO_VALOR)

def func_extrato():
    print("\n==========================================")
    print("\n--> EXTRATO")
    print("--> Não foram realizadas movimentações." if not extrato else extrato)
    print(f"--> Saldo atual é de: R$ {saldo:.2f}\n")
    print("==========================================")

while True:
    
    opcao = input(menu + "DIGITE: ")
    
    if opcao == "d":
        print(" --> DEPOSITO")
        valor_deposito = float(input(" --> DIGITE O VALOR A SER DEPOSITADO: "))
        func_deposito(valor_deposito)
        
    elif opcao == "s":
        print(" --> SAQUE")
        valor_saque = float(input(" --> DIGITE O VALOR A SER SACADO: "))
        func_saque(valor_saque)
        
    
    elif opcao == "e":
        func_extrato()
        
    
    elif opcao == "q":
        break
    
    else:
        print(MENSAGEM_ERRO)
    