from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

# Credentials setup
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'path_to_credentials.json', 
    scopes=['https://www.googleapis.com/auth/webmasters']
)

# Initialize API client
service = build('webmasters', 'v3', credentials=credentials)

# URLs to remove
urls_to_remove = ['url1', 'url2', 'url3']

for url in urls_to_remove:
    request = {
        'url': url,
        'type': 'URL_REMOVAL'
    }
    response = service.urlRemovals().insert(siteUrl='https://your-website.com', body=request).execute()
    print(response)

