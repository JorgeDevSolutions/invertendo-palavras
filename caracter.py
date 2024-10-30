def inverter_string(texto):
    """
    Inverte os caracteres de uma string sem usar funções prontas.
    
    Args:
    texto (str): A string que será invertida.
    
    Returns:
    str: A string invertida.
    """
    if not isinstance(texto, str):
        raise ValueError("O valor fornecido deve ser uma string.")
    
    # Inicializa a string invertida
    texto_invertido = ""
    # Percorre o texto de trás para frente
    for i in range(len(texto) - 1, -1, -1):
        texto_invertido += texto[i]
    return texto_invertido

def main():
    """
    Função principal que solicita a entrada do usuário e exibe a string invertida,
    com a opção de inverter mais strings.
    """
    while True:
        # Solicita a entrada do usuário
        texto = input("Digite uma string para inverter: ").strip()
        
        # Verifica se a string não está vazia
        if not texto:
            print("Erro: A entrada não pode estar vazia.")
        else:
            # Tenta inverter a string e exibir o resultado
            try:
                resultado = inverter_string(texto)
                print("String invertida:", resultado)
            except ValueError as e:
                print(f"Erro: {e}")

        # Pergunta ao usuário se deseja continuar
        repetir = input("Deseja inverter outra string? (s/n): ").strip().lower()
        if repetir != 's':
            print("Programa finalizado.")
            break

# Executa o programa
if __name__ == "__main__":
    main()
