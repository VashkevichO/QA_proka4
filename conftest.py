import requests
import pytest
from config.headers import Headers
import os

STAGE = "https://dev-gs.qa-playground.com/api/v1" if os.environ["STAGE"] == "dev" else "https://release-gs.qa-playground.com/api/v1"


@pytest.fixture(scope="session")
def data_init():
    response = requests.post(
        url=f"{STAGE}/setup",
        headers=Headers.basic
    )
    assert response.status_code == 205

