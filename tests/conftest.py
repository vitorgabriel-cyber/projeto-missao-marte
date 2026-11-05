
import pytest

from src.gerenciador_recursos import GerenciadorRecursosMarte


@pytest.fixture(scope="module")
def parametros_habitat():
    """
    Carrega os parâmetros iniciais do habitat.
    """
    return {
        "estoque_oxigenio": 1000,
        "estoque_agua": 2000
    }


@pytest.fixture(scope="function")
def gerenciador(parametros_habitat):
    """
    Cria uma instância limpa para cada teste.
    """
    sistema = GerenciadorRecursosMarte(
        estoque_oxigenio=parametros_habitat["estoque_oxigenio"],
        estoque_agua=parametros_habitat["estoque_agua"]
    )

    yield sistema

    # Limpeza após cada teste
    sistema.estoque_oxigenio = 0
    sistema.estoque_agua = 0
