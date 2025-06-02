def customer_success_balancing(customer_success, customers, customer_success_away):
    cs_disponiveis = [
        cs for cs in customer_success
        if cs['id'] not in customer_success_away
    ]

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


# Teste rápido
if __name__ == "__main__":
    customer_success = [
        {'id': 1, 'nivel': 60},
        {'id': 2, 'nivel': 20},
        {'id': 3, 'nivel': 95},
        {'id': 4, 'nivel': 75}
    ]

    customers = [
        {'id': 1, 'tamanho': 90},
        {'id': 2, 'tamanho': 20},
        {'id': 3, 'tamanho': 70},
        {'id': 4, 'tamanho': 40},
        {'id': 5, 'tamanho': 60},
        {'id': 6, 'tamanho': 10}
    ]

    customer_success_away = [2, 4]

    print("Resultado:", customer_success_balancing(customer_success, customers, customer_success_away))
