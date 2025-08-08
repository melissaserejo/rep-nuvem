def verificar_acesso(cargo, dia_semana):
    # Normaliza as entradas para evitar problemas com maiúsculas/minúsculas
    cargo = cargo.lower()
    dia_semana = dia_semana.lower()

    # Regras de acesso
    if cargo == "gerente":
        return "Acesso permitido."
    elif cargo == "analista":
        if dia_semana in ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]:
            return "Acesso permitido."
        else:
            return "Acesso negado. Analistas só têm acesso em dias úteis."
    elif cargo == "estagiário":
        if dia_semana in ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]:
            return "Acesso permitido."
        else:
            return "Acesso negado. Estagiários só têm acesso em dias úteis."
    else:
        return "Acesso negado. Cargo não reconhecido."

# Entrada do usuário
cargo = input("Digite o cargo do funcionário (gerente, analista, estagiário): ")
dia_semana = input("Digite o dia da semana (ex: segunda-feira, sábado): ")

# Resultado
resultado = verificar_acesso(cargo, dia_semana)
print(resultado)
