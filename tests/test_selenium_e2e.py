
import pytest

from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()

    # Executa o Chrome sem abrir a janela visual
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    navegador = webdriver.Chrome(options=options)

    yield navegador

    navegador.quit()


def test_solicitar_oxigenio(driver):

    caminho = (
        Path(__file__).resolve().parents[1]
        / "web"
        / "painel.html"
    )

    driver.get(caminho.as_uri())

    try:
        espera = WebDriverWait(driver, 10)

        # Localiza o campo de quantidade
        campo = espera.until(
            EC.visibility_of_element_located(
                (By.ID, "quantidade")
            )
        )

        campo.send_keys("100")

        # Localiza e clica no botão
        botao = driver.find_element(
            By.XPATH,
            "//button[@type='submit']"
        )

        botao.click()

        # Aguarda a atualização do estoque
        espera.until(
            EC.text_to_be_present_in_element(
                (By.ID, "nivel_oxigenio"),
                "900"
            )
        )

        # Verifica a mensagem de sucesso
        mensagem = espera.until(
            EC.visibility_of_element_located(
                (By.ID, "mensagem")
            )
        )

        assert mensagem.text == (
            "Solicitação realizada com sucesso!"
        )

    except Exception:
        # Salva evidência se o teste falhar
        driver.save_screenshot(
            str(
                Path(__file__).resolve().parent
                / "falha_selenium.png"
            )
        )

        raise
