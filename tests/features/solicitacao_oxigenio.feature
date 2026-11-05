
# language: pt

Funcionalidade: Solicitação de suprimentos no habitat de Marte

  Cenário: Solicitação normal de suprimentos
    Dado que o habitat possui estoque suficiente de oxigênio
    Quando o sistema verifica o estoque para 4 astronautas
    Então a solicitação deve ser aprovada

  Cenário: Solicitação em situação de crise
    Dado que o habitat possui estoque insuficiente de oxigênio
    Quando o sistema verifica o estoque para 4 astronautas
    Então deve ocorrer um erro de oxigênio insuficiente
