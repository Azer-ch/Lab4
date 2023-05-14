import re
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
class Ocr :
    def __init__(self,user_id):
        load_dotenv()
        self.connection_string = os.getenv("CONNECTION_STRING")
        self.container_name = os.getenv("CONTAINER_NAME")
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        container_client = blob_service_client.get_container_client(self.container_name)
        blob_client = container_client.get_blob_client(user_id)
        self.blob_content = blob_client.download_blob().content_as_text()
        #pattern for a decimal number
        self.salary_pattern=r"\d+(\.\d+)?"
    def getSalary(self):
        return re.findall(self.salary_pattern,self.blob_content)[0]
