# here we are trying to to generate the accesst token from the google Oauth using the
#  auth code and understadning the three diffferent version 

#using the flow from the google auth library and run_local_server method to access token

import os 
import dotenv
from google_auth_oauthlib.flow import InstalledAppFlow

dotenv.load_dotenv()

#assigning the client data from the envb file
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

#defining the scope of the access token - means which api we want to access and want the permission for 
SCOPES = ["https://mail.google.com/"]

#making the client config dictionary
client_config ={
    "installed":{
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uris": ["http://localhost:3000/"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token"
    }
}

#creating the flow start point 
flow = InstalledAppFlow.from_client_config(client_config , SCOPES)

#getting the credentials using the run_local_server method after running the flow
cred = flow.run_local_server(port = 3000)

access_token = cred.token
refresh_token = cred.refresh_token 
token_expiry = cred.expiry

print("Access Token:", access_token)
print("Refresh Token:", refresh_token)
print("Token URI:", token_expiry)
