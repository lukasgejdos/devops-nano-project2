from app import app
from flask import json

def test_predict():        
    response = app.test_client().post(
        '/predict',
        data=json.dumps({
          "CHAS":{
            "0":0
          },
          "RM":{
            "0":6.575
          },
          "TAX":{
            "0":296.0
          },
          "PTRATIO":{
            "0":15.3
          },
          "B":{
            "0":396.9
          },
          "LSTAT":{
            "0":4.98
        }}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['prediction'] == [20.35373177134412]
