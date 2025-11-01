import pytest
from app import app, db, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
        yield client

def test_create_user(client):
    response = client.post('/api/create_user', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 201
    assert b'User created successfully' in response.data

    # Duplicate user
    response = client.post('/api/create_user', json={
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 400
    assert b'User already exists' in response.data

    # Missing fields
    response = client.post('/api/create_user', json={
        'username': '',
        'password': ''
    })
    assert response.status_code == 400
    assert b'Username and password required' in response.data

def test_login_user(client):
    client.post('/api/create_user', json={
        'username': 'loginuser',
        'password': 'loginpass'
    })
    # Successful login
    response = client.post('/api/login', json={
        'username': 'loginuser',
        'password': 'loginpass'
    })
    assert response.status_code == 200
    assert b'Login successful' in response.data

    # Wrong password
    response = client.post('/api/login', json={
        'username': 'loginuser',
        'password': 'wrongpass'
    })
    assert response.status_code == 401
    assert b'Invalid password' in response.data

    # User not found
    response = client.post('/api/login', json={
        'username': 'nouser',
        'password': 'nopass'
    })
    assert response.status_code == 404
    assert b'User not found' in response.data

def test_show_all_users(client):
    client.post('/api/create_user', json={
        'username': 'user1',
        'password': 'pass1'
    })
    client.post('/api/create_user', json={
        'username': 'user2',
        'password': 'pass2'
    })
    response = client.get('/api/users')
    assert response.status_code == 200
    data = response.get_json()
    assert 'user1' in data['users']
    assert 'user2' in data['users']
