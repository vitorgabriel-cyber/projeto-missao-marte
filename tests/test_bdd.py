
import pytest

from pytest_bdd import scenario, given, when, then

from src.gerenciador_recursos import OxigenioInsuficienteError


@pytest.fixture
def contexto_bdd():
    return {}


@scenario(
    "features/solicitacao_oxigenio.feature",
    "Solicitação normal de suprimentos"
)
def test_solicitacao_normal():
    pass


@scenario(
    "features/solicitacao_oxigenio.feature",
    "Solicitação em situação de crise"
)
def test_solicitacao_crise():
    pass


@given("que o habitat possui estoque suficiente de oxigênio")
def estoque_suficiente(gerenciador):
    gerenciador.estoque_oxigenio = 1000


@given("que o habitat possui estoque insuficiente de oxigênio")
def estoque_insuficiente(gerenciador):
    gerenciador.estoque_oxigenio = 1


@when("o sistema verifica o estoque para 4 astronautas")
def verificar_estoque_bdd(gerenciador, contexto_bdd):
    try:
        contexto_bdd["resultado"] = gerenciador.verificar_estoque(4)
    except OxigenioInsuficienteError as erro:
        contexto_bdd["erro"] = erro


@then("a solicitação deve ser aprovada")
def verificar_aprovacao(contexto_bdd):
    assert contexto_bdd["resultado"] is True


@then("deve ocorrer um erro de oxigênio insuficiente")
def verificar_erro(contexto_bdd):
    assert isinstance(
        contexto_bdd.get("erro"),
        OxigenioInsuficienteError
    )
