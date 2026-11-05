
class OxigenioInsuficienteError(Exception):
    pass


class NivelEmergenciaInvalidoError(Exception):
    pass


class GerenciadorRecursosMarte:

    def __init__(
        self,
        estoque_oxigenio,
        estoque_agua,
        servico_telemetria=None
):
        self.estoque_oxigenio = estoque_oxigenio
        self.estoque_agua = estoque_agua
        self.servico_telemetria = servico_telemetria

        self.consumo_oxigenio = 0.84
        self.consumo_agua = 3.0
        
    
    def enviar_status_telemetria(self, status):
        if self.servico_telemetria is not None:
            return self.servico_telemetria.enviar_relatorio(status)

    def acionar_alerta_emergencia(self, nivel, mensagem):
        if self.servico_telemetria is not None:
            return self.servico_telemetria.disparar_alerta(
                nivel,
                mensagem
            )


    def calcular_consumo_diario(self, astronautas):
        if astronautas <= 0:
            raise ValueError("Número de astronautas inválido")

        oxigenio = astronautas * self.consumo_oxigenio
        agua = astronautas * self.consumo_agua

        return {
            "oxigenio": oxigenio,
            "agua": agua
        }

    def verificar_estoque(self, astronautas):
        consumo = self.calcular_consumo_diario(astronautas)

        if self.estoque_oxigenio < consumo["oxigenio"]:
            raise OxigenioInsuficienteError(
                "Estoque de oxigênio insuficiente!"
            )

        return True

    def calcular_taxa_emergencia(self, nivel):
        if nivel < 1 or nivel > 5:
            raise NivelEmergenciaInvalidoError(
                "O nível de emergência deve estar entre 1 e 5."
            )

        return 1 + (nivel - 1) * 0.25

    def aplicar_racionamento(self, consumo, nivel):
        taxa = self.calcular_taxa_emergencia(nivel)

        return consumo / taxa
