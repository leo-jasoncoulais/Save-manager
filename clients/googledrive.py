
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

class Service:

    def __init__(self, name, version, creds):
        self.service = build(name, version, credentials=creds)

    def upload(self, file, name=None):

        if not name:
            name = os.path.basename(file)
        
        self.service.files().create(
            body={"name": name},
            media_body=MediaFileUpload(file),
            fields="id"
        ).execute()

class GoogleClient:

    def __init__(self, scopes: list[str]):
        self.creds = None
        self.scopes = scopes

    def init(self):

        if os.path.exists("tokens/google.json"):
            self.creds = Credentials.from_authorized_user_file("tokens/google.json", self.scopes)

        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:

            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("keys/google.json", self.scopes)
                self.creds = flow.run_local_server(port=0)                

        # Save the credentials for the next run
        with open("tokens/google.json", "w") as token:
            token.write(self.creds.to_json())

    def get_service(self, name: str, version: str):
        return Service(name, version, self.creds)
