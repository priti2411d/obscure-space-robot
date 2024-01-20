import app
import json
import warnings

#  def test_hello_world():
#     response=app.app.test_client()().get('/hello')
#     assert response.status_code == 200
#     assert response.data == b'Hello,World!'

# def test_goodbye():
#     response = app.app.test_client().get('/goodbye')
#     assert response.status_code == 404

def test_name():
    response=app.app.test_client().get('/name')
    assert response.status_code == 200
    assert response.data == b'Priti'

def test_age():
    response=app.app.test_client().get('/age')
    assert response.status_code == 200
    assert response.data == b'18'

