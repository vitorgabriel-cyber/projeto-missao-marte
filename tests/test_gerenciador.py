
import pytest
from unittest.mock import MagicMock

from src.gerenciador_recursos import (
    OxigenioInsuficienteError,
    NivelEmergenciaInvalidoError
)


@pytest.mark.parametrize(
    "astronautas, oxigenio_esperado, agua_esperada",
    [
        (1, 0.84, 3.0),
        (2, 1.68, 6.0),
        (4, 3.36, 12.0),
        (6, 5.04, 18.0),
    ]
)
def test_calcular_consumo_diario(
    gerenciador,
    astronautas,
    oxigenio_esperado,
    agua_esperada
):
    resultado = gerenciador.calcular_consumo_diario(astronautas)

    assert resultado["oxigenio"] == pytest.approx(oxigenio_esperado)
    assert resultado["agua"] == pytest.approx(agua_esperada)


def test_verificar_estoque_suficiente(gerenciador):
    assert gerenciador.verificar_estoque(4) is True


def test_oxigenio_insuficiente(gerenciador):
    gerenciador.estoque_oxigenio = 1

    with pytest.raises(OxigenioInsuficienteError):
        gerenciador.verificar_estoque(4)


def test_nivel_emergencia_invalido(gerenciador):
    with pytest.raises(NivelEmergenciaInvalidoError):
        gerenciador.calcular_taxa_emergencia(6)


def test_calcular_taxa_emergencia(gerenciador):
    resultado = gerenciador.calcular_taxa_emergencia(3)

    assert resultado == pytest.approx(1.5)
    

def test_enviar_relatorio_com_mock(gerenciador):
    telemetria = MagicMock()
    gerenciador.servico_telemetria = telemetria

    gerenciador.enviar_status_telemetria("Oxigênio normal")

    telemetria.enviar_relatorio.assert_called_once_with(
        "Oxigênio normal"
    )


def test_disparar_alerta_com_mock(gerenciador):
    telemetria = MagicMock()
    gerenciador.servico_telemetria = telemetria

    gerenciador.acionar_alerta_emergencia(
        5,
        "Oxigênio crítico"
    )

    telemetria.disparar_alerta.assert_called_once_with(
        5,
        "Oxigênio crítico"
    )

