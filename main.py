# Analisador de Desempenho de Elenco - eFootball Simulator

def analisar_time():
    print("=" * 50)
    print("📊 ANALISADOR DE DESEMPENHO DE ELENCO (eFootball) 📊")
    print("=" * 50)
    
    jogadores = {}
    
    while True:
        nome = input("\nDigite o nome do jogador (ou 'sair' para finalizar): ").strip()
        if nome.lower() == 'sair':
            break
            
        try:
            nota = float(input(f"Digite a nota técnica de {nome} (0 a 10): "))
            if 0 <= nota <= 10:
                jogadores[nome] = nota
            else:
                print("❌ Erro: A nota deve ser entre 0 e 10.")
        except ValueError:
            print("❌ Erro: Digite um número válido para a nota.")

    if not jogadores:
        print("\nNenhum jogador foi cadastrado.")
        return

    # Cálculos Estatísticos
    total_jogadores = len(jogadores)
    media_time = sum(jogadores.values()) / total_jogadores
    melhor_jogador = max(jogadores, key=jogadores.get)
    precisa_treinar = [nome for nome, nota in jogadores.items() if nota < 6.0]

    # Relatório Final no Console
    print("\n" + "=" * 40)
    print("📋 RELATÓRIO TÉCNICO DO TIME")
    print("=" * 40)
    print(f"Total de jogadores analisados: {total_jogadores}")
    print(f"Média técnica do elenco: {media_time:.2f}")
    print(f"⭐ Craque do Time: {melhor_jogador} (Nota: {jogadores[melhor_jogador]})")
    
    print("\n⚠️ Jogadores que precisam de treino (Nota < 6.0):")
    if precisa_treinar:
        for j in precisa_treinar:
            print(f" - {j} (Nota: {jogadores[j]})")
    else:
        print(" - Nenhum! Todo o elenco está operando em alto nível.")
    print("=" * 40)

if __name__ == "__main__":
    analisar_time()
