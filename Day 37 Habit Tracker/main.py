import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "rb96"
TOKEN = "iamnotdoneyetuntiliwin"
# create_user_params = {
#     "token": TOKEN,
#     "username": "rb96",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = requests.post(url=pixela_endpoint, json=create_user_params)
# response.raise_for_status()
# print(response.json())

# Create a graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID="graph-1"
graph_params = {
    "id": GRAPH_ID,
    "name": "cycling",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

request_header={
'X-USER-TOKEN':TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=request_header)
# response.raise_for_status()
# print(response.text)


# Post a pixel

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
now = datetime.now()
formatted_date_time = now.strftime("%Y%m%d")

pixel_data = {
    'date':str(formatted_date_time),
    'quantity':"10"
}

response =requests.post(url=pixel_endpoint, json=pixel_data, headers=request_header)
print(response.text)