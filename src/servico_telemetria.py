
class ServicoTelemetriaEspacial:

    def enviar_relatorio(self, status):
        print(f"Relatório enviado para a Terra: {status}")
        return True

    def disparar_alerta(self, nivel, mensagem):
        print(f"ALERTA DE EMERGÊNCIA!")
        print(f"Nível: {nivel}")
        print(f"Mensagem: {mensagem}")
        return True
