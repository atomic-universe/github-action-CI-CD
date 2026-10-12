from fastapi.testclient import TestClient 
from app.main import app 
import pytest
client = TestClient(app)

def test_home():
    r = client.get('/')
    assert r.status_code == 200 
    assert r.json()['title'] == 'GitHub action workflow'


@pytest.mark.parametrize('a, b, expected',[
    (3,2.5,5.5),
    (1,93,94),
    (-5,10,5)
])
def test_add(a,b,expected):
    r = client.post('/add',json={'val_1':a,'val_2':b})
    assert r.status_code ==200
    assert r.json()['result']==expected

@pytest.mark.parametrize('a, b, expected',[
    (3,2.5,0.5),
    (1,93,-92),
    (-5,10,-15)
])
def test_sub(a,b,expected):
    r = client.post('/sub',json={'val_1':a,'val_2':b})
    assert r.status_code ==200
    assert r.json()['result']==expected


@pytest.mark.parametrize('a, b, expected',[
    (3,2.5,7.5),
    (1,93,93),
    (-5,10,-50)
])
def test_mult(a,b,expected):
    r = client.post('/mult',json={'val_1':a,'val_2':b})
    assert r.status_code ==200
    assert r.json()['result']==expected

@pytest.mark.parametrize('a, b, expected',
                        [
    (4,2.5,1.6),
    (1,93,0.0108),
    (-5,10,-0.5)
    
])
def test_div(a,b,expected):
    r = client.post('/div',json={'val_1':a,'val_2':b})
    assert r.status_code ==200
    assert round(r.json()['result'],4)==expected


def test_div_zero():
    r = client.post('/div',json={'val_1':4.6,'val_2':0})

    assert r.status_code ==400
    assert r.json()['detail'] == {"details": "Division by zero is not allowed."}


@pytest.mark.parametrize('a, b, expected',
                        [
    (4,2.5,16),
    (0,93,0),
    (-5,1.232, -5),
    (-5,-1.232,-0.2)
    
])
def test_pow(a,b,expected):
    r = client.post('/pow',json={'val_1':a,'val_2':b})
    assert r.status_code ==200
    expected = round(expected,4)
    assert round(r.json()['result'],4)==expected
