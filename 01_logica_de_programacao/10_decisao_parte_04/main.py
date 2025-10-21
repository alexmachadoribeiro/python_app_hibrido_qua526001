# declaração de variáveis
x = float(input("Informe o 1º número: ").strip().replace(",","."))
y = float(input("Informe o 2º número: ").strip().replace(",","."))

# menu
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operador = input("Informe a operação desejada: ").strip()

# decisão
match operador:
    case "1":
        print(f"A soma é {x+y}")
    case "2":
        print(f"A subtração é {x-y}")
    case "3":
        print(f"A multiplicação é {x*y}")
    case "4":
        print(f"A divisão é {x/y}")
    case _:
        print("Operação inválida.")