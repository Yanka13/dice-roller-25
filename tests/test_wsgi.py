from wsgi import app 


def test_roll():
    app.testing = True 
    client = app.test_client()
    request = client.get("/").json["roll"]
    assert type(request) == int 
    assert request > 0 
    assert request < 7
    
    