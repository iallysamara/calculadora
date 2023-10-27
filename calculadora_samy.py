# Calculadora em Python
count = 1

while count == 1:
    operacao = int(input("Selecione o número da operação desejada:\n\n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n\n Digite sua opção (1/2/3/4): "))
    while operacao > 4 or operacao < 1:
        print("\n******** Operação inválida!!! ********\n")
        operacao = int(input("Selecione o número da operação desejada:\n\n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n\n Digite sua opção (1/2/3/4): "))
    else:
        if operacao == 1:
            num1 = int(input("\nDigite um número: "))
            num2 = int(input("\nDigite outro número: "))
    
            soma = num1 + num2
    
            print("\n%d + %d = %d \n" %(num1, num2, soma))
            count = int(input("\nVocê deseja fazer mais alguma operação?\n 1 - Sim \n 0 - Não \n\n Digite sua opção (1/0):"))
        elif operacao == 2:
            num1 = int(input("\nDigite um número: "))
            num2 = int(input("\nDigite outro número: "))
    
            subt = num1 - num2
    
            print("\n%d - %d = %d \n" %(num1, num2, subt))
            count = int(input("\nVocê deseja fazer mais alguma operação?\n 1 - Sim \n 0 - Não \n\n Digite sua opção (1/0):"))
        elif operacao == 3:
            num1 = int(input("\nDigite um número: "))
            num2 = int(input("\nDigite outro número: "))
    
            mult = num1 * num2
    
            print("\n%d * %d = %d \n" %(num1, num2, mult))
            count = int(input("\nVocê deseja fazer mais alguma operação?\n 1 - Sim \n 0 - Não \n\n Digite sua opção (1/0):"))
        elif operacao == 4:
            num1 = int(input("\nDigite um número: "))
            num2 = int(input("\nDigite outro número: "))
    
            div = num1 / num2
    
            print("\n%d / %d = %d \n" %(num1, num2, div))
            count = int(input("V\nocê deseja fazer mais alguma operação?\n 1 - Sim \n 0 - Não \n\n Digite sua opção (1/0):"))
else:
    print("\nObrigada por usar minha calculadora!\n TE AMO MUITO, coisinha mais preciosa <3")
