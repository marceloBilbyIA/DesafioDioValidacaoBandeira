# Validador de Bandeiras de Cartão de Crédito

Este projeto tem como objetivo identificar a bandeira de um cartão de crédito a partir do número informado, utilizando expressões regulares para validar os principais padrões de mercado.

## Como funciona

O script `validador.py` contém uma função chamada `identificar_bandeira`, que recebe o número do cartão (com ou sem espaços) e retorna a bandeira correspondente, como Visa, MasterCard, Elo, American Express, Discover, Hipercard, JCB, Voyager, entre outras.

A identificação é feita através de expressões regulares que verificam os prefixos e o tamanho do número do cartão, conforme as regras de cada bandeira.

## Exemplo de uso

```python
bandeira = identificar_bandeira("4011123456789012")
print(f"Bandeira do cartão: {bandeira}")
```

## Bandeiras suportadas

- Visa
- MasterCard
- Elo
- American Express
- Discover
- Hipercard
- JCB
- Voyager
- Diners Club
- Aura
- UnionPay
- Maestro
- Banrisul
- Bradesco Cartões

## Como rodar

1. Clone este repositório.
2. Execute o arquivo `validador.py` com Python 3.

---

Projeto criado para fins de estudo e demonstração de validação de cartões usando Python e regex.