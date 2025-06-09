def customer_success_balancing(customer_success, customers, customer_success_away):
    cs_disponiveis = [cs for cs in customer_success if cs['id'] not in customer_success_away]
    cs_disponiveis.sort(key=lambda cs: cs['nivel'])
    customers.sort(key=lambda c: c['tamanho'])
    atendimentos = {cs['id']: 0 for cs in cs_disponiveis}
    for cliente in customers:
        for cs in cs_disponiveis:
            if cs['nivel'] >= cliente['tamanho']:
                atendimentos[cs['id']] += 1
                break
    if not atendimentos:
        return 0
    max_atendimentos = max(atendimentos.values())
    cs_mais_solicitado = [cs_id for cs_id, qtd in atendimentos.items() if qtd == max_atendimentos]
    return cs_mais_solicitado[0] if len(cs_mais_solicitado) == 1 else 0

def input_lista_de_dicts(nome_lista, campos):
    print(f"\nDigite os dados de {nome_lista} no formato: id,nivel (um por linha). Digite ENTER em branco para terminar.")
    lista = []
    while True:
        linha = input("> ")
        if not linha.strip():
            break
        try:
            partes = linha.split(",")
            item = {campo: int(valor) for campo, valor in zip(campos, partes)}
            lista.append(item)
        except:
            print("⚠️ Formato inválido. Tente novamente (ex: 1,60)")
    return lista

def input_lista_inteiros(nome_lista):
    linha = input(f"\nDigite os IDs de {nome_lista} separados por vírgula: ")
    try:
        return [int(x.strip()) for x in linha.split(",") if x.strip()]
    except:
        print("⚠️ Erro ao processar os dados.")
        return []

def main():
    print("=== Customer Success Balancing - Interface de Teste ===")

    cs = input_lista_de_dicts("Customer Success", ["id", "nivel"])
    clientes = input_lista_de_dicts("Clientes", ["id", "tamanho"])
    indisponiveis = input_lista_inteiros("CSs Indisponíveis")

    resultado = customer_success_balancing(cs, clientes, indisponiveis)
    print(f"\n📊 Resultado: O CS que atendeu mais clientes foi o ID {resultado}" if resultado else "\n📊 Resultado: Houve empate ou ninguém atendeu.")

if __name__ == "__main__":
    main()

