import os
import base64

API_KEY = "XG1P28NN5Z3HZM84W1PLMSHFBDUABMV4"

API_URL = "http://localhost:8080/api"
HEADERS = {
    'Authorization': f'Basic {base64.b64encode(f"{API_KEY}:".encode()).decode()}'
}