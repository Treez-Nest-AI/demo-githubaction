from handler import hello

def test_status_code():
    response = hello()
    assert response['statusCode'] == 200

def test_message():
    response = hello()
    assert response['body'] == "Hello from python demo service!"