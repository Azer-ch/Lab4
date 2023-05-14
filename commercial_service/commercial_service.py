from ocr.ocr import Ocr
from database_manager.database_manager import DatabaseManager
class CommercialService :
    def __init__(self,user_id) :
        # Use the OCR service to extract user's information like annual saluary
        annual_salary = Ocr(user_id).getSalary()
        self.score = self.compute_score(annual_salary)
        database_manager = DatabaseManager()
        database_manager.insertInitialScore(user_id,self.score)

    def compute_score(annual_salary):
        if annual_salary < 30000:
            return 0 
        elif annual_salary < 50000:
            return 50 
        elif annual_salary < 100000:
            return 75
        else:
            return 100


    