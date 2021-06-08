import pytest
import tempfile
import io
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_upload(client):
    data = {
        'tgz_file': (io.BytesIO(b"abcdef"), 'test.tgz')
    }

    response = client.post("/api/v1/upload/test/", data=data)
    
    r_data = response.json

    assert response.status == '200 OK' and r_data.get('success') == True

def test_list(client):
    
    response = client.get("/api/v1/list/test/")
    
    r_data = response.json

    assert response.status == '200 OK' and r_data.get('success') == True

def test_download(client):

    response = client.get("/api/v1/download/test/file_test.tgz/")
    
    print(response)
    print(type(response.data))
    r_data = response.json

    print(r_data)

    assert response.status == '200 OK' and type(response.data) == bytes