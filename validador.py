import re

def identificar_bandeira(numero_cartao: str) -> str:
    numero = re.sub(r'\D', '', numero_cartao)

    padroes = [
        ("Visa", r"^4\d{12}(\d{3})?$"),
        ("MasterCard", r"^(5[1-5]\d{14}|222[1-9]\d{12}|22[3-9]\d{13}|2[3-6]\d{14}|27[01]\d{13}|2720\d{12})$"),
        ("Elo", r"^(4011|4312|4389)\d+"),
        ("American Express", r"^3[47]\d{13}$"),
        ("Discover", r"^(6011\d{12}|65\d{14}|64[4-9]\d{13})$"),
        ("Hipercard", r"^6062\d+"),
        ("JCB", r"^35[2-8][0-9]{3}[0-9]{10,13}$"),
        ("Voyager", r"^8699\d{11}$"),
        ("Diners Club", r"^3(?:0[0-5]|[68]\d)\d{11}$"),
        ("Aura", r"^50\d{14}$"),
        ("UnionPay", r"^(62|81)\d{14,17}$"),
        ("Maestro", r"^(5018|5020|5038|6304|6759|6761|6763)\d{10,15}$"),
        ("Banrisul", r"^6030\d{10}$"),
        ("Bradesco Cartões", r"^6014\d{12}$"),
    ]

    for bandeira, padrao in padroes:
        if re.match(padrao, numero):
            return bandeira
    return "Bandeira desconhecida"

bandeira = identificar_bandeira("5063339571090286")
print(f"Bandeira do cartão: {bandeira}")