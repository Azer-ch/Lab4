from dotenv import load_dotenv
import requests
from database_manager.database_manager import DatabaseManager
from ocr.ocr import Ocr

class RiskManagementService:
    def __init__(user_id,self):
        self.api_key = os.getenv("CENTRAL_BANK_API_KEY")
        self.url = os.getenv("CENTRAL_BANK_API_URL")
        self.final_score = self.compute_final_score()
        self.annual_salary = Ocr(user_id).getSalary()
        if self.final_score:
            database_manager = DatabaseManager()
            database_manager.insertFinalScore(user_id,self.final_score)

    def get_banking_info_from_api(self):
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                print("Failed to retrieve banking information from the API.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to the API: {str(e)}")
    def compute_final_score(self):
        self.banking_info = self.get_banking_info_from_api()
        if self.banking_info:
            account_balance = self.banking_info.get("account_balance", 0)
            transaction_count = self.banking_info.get("transaction_count", 0)
            credit_score = self.banking_info.get("credit_score", 0)
            return account_balance * 0.4 + transaction_count *0.3+credit_score*0.3
        else:
            return None
            



