import pytest
from tests.web.pages.login_page import LoginPage

@pytest.mark.web
class TestLogin:
    def test_login_campos_vacios(self, driver, config):
        """Verificar que no se permite login con campos vacíos."""
        page = LoginPage(driver)
        page.open(config.BASE_URL)
        page.login("", "")
        assert page.get_error() != ""

    def test_login_credenciales_invalidas(self, driver, config):
        """Verificar mensaje de error con credenciales incorrectas."""
        page = LoginPage(driver)
        page.open(config.BASE_URL)
        page.login("usuario_invalido", "password_invalido")
        error = page.get_error()
        assert error, "Debe mostrarse un mensaje de error"
