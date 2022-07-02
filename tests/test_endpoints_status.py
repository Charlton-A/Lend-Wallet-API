import pytest
from apps import init_app
from conf import DevelopmentConfig


@pytest.fixture()
def app():
    app = init_app(DevelopmentConfig)
    return app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.mark.unit
def test_ping(client):
    response = client.get("/api/v1/ping")
    assert response.status_code == 200


@pytest.mark.unit
def test_login(client):
    response = client.get("/api/v1/login")
    assert response.status_code == 405


@pytest.mark.unit
def test_profile(client):
    response = client.get("/api/v1/profile")
    assert response.status_code == 401


@pytest.mark.unit
def test_date_filter(client):
    response = client.get("/api/v1/filter/date")
    assert response.status_code == 401
