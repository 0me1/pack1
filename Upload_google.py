from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build


def delete_old_file():
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = '/content/pack1/profile_google.json'
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)
    result = service.files().list(pageSize=10, fields="nextPageToken, files(id, name)",).execute()
    # print(result)
    a,b = result['files']
    file_id = a['id']
    service.files().delete(fileId=file_id).execute()





def upload_price():
    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = '/content/pack1/profile_google.json'

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)
    # result = service.files().list(pageSize=10, fields="nextPageToken, files(id, name, mimeType)").execute()
    folder_id = '1FMFy6MtI1QHH9SHCwI3KfFFPF8qxIXUT'
    file_path = '/content/dataCash.json'
    name = 'dataCash.json'
    file_metadata = {
        'name': name,
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_path, resumable=True)
    r = service.files().create(body=file_metadata, media_body=media, fields='id').execute()


