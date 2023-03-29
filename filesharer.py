from dotenv import load_dotenv

load_dotenv()

class FileSharer:

    def __init__(self, filepath, api_key='API_KEY'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
