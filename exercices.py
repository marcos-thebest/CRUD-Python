while True:

    try: 
        a = int(input("\nDigite o primeiro número: "))
        b = int(input("Digite o segundo número: "))

        # Operações
        adicao = a + b
        sub = a - b
        multi = a * b
        divi = a / b 
        
    except ValueError:
        print("\nSomente aceito números!")
    
    except ZeroDivisionError:
        print("\nNão é possível dividir por zero!")
    
    else:
        print(f"\n{a} + {b} = {adicao}")
        print(f"\n{a} - {b} = {sub}")
        print(f"\n{a} x {b} = {multi}")
        print(f"\n{a} / {b} = {divi:.2f}")

    opc = int(input("\nDeseja fazer mais operações? (1 - Sim / 2 - Não): "))
    if opc == 2:
        print("\nFinalizando a calculadora. Até logo!")
        break