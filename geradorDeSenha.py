import random
import string
import pyperclip


def generate_password(length, uppercase, lowercase, numbers, special_chars):
    # Define os caracteres disponíveis para cada critério
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    # Verifica se foram fornecidos critérios válidos
    if not characters:
        print("Erro: Nenhum critério válido fornecido.")
        return None

    # Gera a senha aleatória
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Bem-vindo ao Gerador de Senhas Seguras!")

    # Solicita os critérios para a geração da senha
    length = int(input("Comprimento mínimo da senha: "))
    uppercase = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    lowercase = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    numbers = input("Incluir números? (s/n): ").lower() == 's'
    special_chars = input(
        "Incluir caracteres especiais? (s/n): ").lower() == 's'

    # Gera a senha
    password = generate_password(
        length, uppercase, lowercase, numbers, special_chars)

    if password:
        print("Senha gerada:", password)
        copy_to_clipboard = input(
            "Deseja copiar a senha para a área de transferência? (s/n): ").lower() == 's'
        if copy_to_clipboard:
            pyperclip.copy(password)
            print("A senha foi copiada para a área de transferência.")


if __name__ == "__main__":
    main()
