import os
import pytest
from main import app


@pytest.fixture
def client():
    app_client = app.test_client()
    return app_client


def test_simple(client):
    r = client.get("/api/v1/Simple")
    assert r.json is not None
