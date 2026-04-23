# Neste primeiro def, criamos uma função para retornar o nome do plano com base no código fornecido. A função verifica o código do plano e retorna o nome correspondente. Se o código for inválido, retorna uma mensagem de erro.
def nome_plano(cod_plano):
    if cod_plano == 1:
       return "Plano básico"
    elif cod_plano == 2:
        return "Plano PRO"
    elif cod_plano == 3:
        return "Plano Premium"
    else:
        return "Código de plano inválido"
    # Nesta segunda função, criamos uma função para retornar o valor inicial do plano com base no código fornecido. A função verifica o código do plano e retorna o valor correspondente. Se o código for inválido, retorna None.
    def valor_inicial_plano(cod_plano):
        if cod_plano == 1:
            return 39.90
        elif cod_plano == 2:
            return 59.90
        elif cod_plano == 3:
            return 79.90
        else:
            return None
        # Nesta terceira função, criamos uma função para calcular o imposto com base no valor e no tipo de cliente. A função verifica o tipo de cliente (PF ou PJ) e calcula o imposto correspondente. Se o tipo de cliente for inválido, retorna None.
        def calcular_imposto(valor, tipo_cliente):
            tipo_cliente = tipo_cliente.upper()
            if tipo_cliente == "PF":
                return valor * 0.10
            elif tipo_cliente == "PJ":
                return valor * 0.15
            else:
                return None
            # Nesta quarta função, criamos uma função para calcular o valor total da fatura com base no código do plano e no tipo de cliente. A função utiliza as funções anteriores para obter o valor inicial do plano e calcular o imposto, e depois soma ambos para obter o total. Se o código do plano ou o tipo de cliente forem inválidos, retorna None.
        def calcular_fatura_total(cod_plano, tipo_cliente):
            valor_inicial = valor_inicial_plano(cod_plano)
            if valor_inicial is None:
                return None
            imposto = calcular_imposto(valor_inicial, tipo_cliente)
            if imposto is None:
                return None
            total = valor_inicial + imposto
            return total
            