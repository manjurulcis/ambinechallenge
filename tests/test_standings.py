# TODO: Implement your test cases for the standings endpoint here.

from standings.main import app


def test_returns_200_OK():
    with app.test_client() as client:
        response = client.get('/standing/4242342')
        assert response.status_code == 200
        #assert response.get_data(as_text=True) == 'Hello, World!'


def test_returns_valid_season():
    with app.test_client() as client:
        response = client.get('/standing/4242342sdfsd')
        assert response.status_code == 200
        assert response.get_data(as_text=True) == 'Invalid season id'
