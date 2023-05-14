from database_manager.database_manager import DatabaseManager
class CreditService:
    def __init__(self,user_id):
        self.initial_score , self.final_score = DatabaseManager.getScores(user_id)
        self.is_loan_eligible = self.assess_eligibility(self.initial_score,self.final_score)
    def assess_eligiblity(self,initial_score,final_score):
        return initial_score >= 75 and final_score >= 1500