# bibliotecas
import os

# declaração de lista
usuarios = []

# limpa console
os.system("cls")

while True:
    # menu
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuários")
    print("3 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls")
    match opcao:
        case "1":
            usuario = {}
            usuario['nome'] = input("Informe o nome do usuário: ").strip().title()
            usuario['idade'] = int(input("Informe a idade do usuário: ").strip())
            usuario['email'] = input("Informe o e-mail do usuário: ").strip().lower()
            usuarios.append(usuario)
            os.system("cls")
            print("Novo usuário inserido com sucesso.")
            continue
        case "2":
            for usuario in usuarios:
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario[chave]}")
                print(f"{'-'*40}")
            continue
        case "3":
            break
        case _:
            print("Opção inválida.")
            continue