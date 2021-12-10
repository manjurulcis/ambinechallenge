from standings.main import app


def test_returns_200_OK():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.get_data(as_text=True) == 'Hello, World!'
