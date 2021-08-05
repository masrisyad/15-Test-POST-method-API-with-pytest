import requests
import json
import pytest
import jsonpath

# test by risyad abdala ramadhan

def test_post_method():
    url = 'https://api.trello.com/1/boards/'
    
    query = {
        'key':'inputyourkey',
        'token':'inputyourtoken',
        'name':'Test 1 with pytest'
    }
    
    response = requests.post(url,params=query)
    
    code = response.status_code
    
    assert code == 200
    
    json_response = json.loads(response.text)
    
    Name = jsonpath.jsonpath(json_response,'name')
    
    assert Name[0] == 'Test 1 with pytest'