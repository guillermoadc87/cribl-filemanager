# pylint: disable=redefined-outer-name,missing-module-docstring
import io
import pytest
from main import app

@pytest.fixture
def client():
    """
    Creates an app client instance to query the api
    """

    with app.test_client() as client:
        yield client

def test_upload(client):
    """
    Test the Upload endpoint /api/v1/upload/<customer>
    """

    data = {
        'tgz_file': (io.BytesIO(b"abcdef"), 'test.tgz')
    }

    response = client.post("/api/v1/upload/test/", data=data)

    r_data = response.json

    assert response.status == '200 OK' and r_data.get('success') is True

def test_list(client):
    """
    Test the List endpoint /api/v1/list/<customer>
    """

    response = client.get("/api/v1/list/test/")

    r_data = response.json

    assert response.status == '200 OK' and r_data.get('success') is True

def test_download(client):
    """
    Test the Upload endpoint /api/v1/download/<customer>/<filename>
    """

    response = client.get("/api/v1/download/test/file_test.tgz/")

    print(response)
    print(type(response.data))
    r_data = response.json

    print(r_data)

    assert response.status == '200 OK' and isinstance(response.data, bytes)
