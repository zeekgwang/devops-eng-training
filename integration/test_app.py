# TODO(everyone): 웹서버의 healthz가 response code 200 확인
import pytest
from app import create_app


@pytest.fixture
def api():
    app = create_app()
    return app.test_client()


def test_healthCheck(api):
    response = api.get("/healthz")
    assert response.status == '200 OK'


