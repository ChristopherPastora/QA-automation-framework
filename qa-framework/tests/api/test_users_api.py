import pytest
from tests.api.clients.base_client import BaseClient

@pytest.mark.api
class TestUsersAPI:
    @pytest.fixture(autouse=True)
    def setup(self, config):
        self.client = BaseClient(config.API_URL)

    def test_get_usuarios_retorna_200(self):
        """GET /users debe retornar status 200."""
        response = self.client.get("/users")
        assert response.status_code == 200

    def test_get_usuarios_retorna_lista(self):
        """GET /users debe retornar una lista no vacía."""
        response = self.client.get("/users")
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0

    def test_get_usuario_por_id(self):
        """GET /users/1 debe retornar el usuario con id=1."""
        response = self.client.get("/users/1")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert "name" in data
        assert "email" in data

    def test_crear_usuario(self):
        """POST /users debe crear un usuario y retornar 201."""
        payload = {"name": "Christopher Pastora", "email": "cp@qa.com", "username": "cpastora"}
        response = self.client.post("/users", payload)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == payload["name"]

    def test_actualizar_usuario(self):
        """PUT /users/1 debe actualizar y retornar 200."""
        payload = {"name": "Christopher Updated"}
        response = self.client.put("/users/1", payload)
        assert response.status_code == 200

    def test_eliminar_usuario(self):
        """DELETE /users/1 debe retornar 200."""
        response = self.client.delete("/users/1")
        assert response.status_code == 200
