from dotenv import load_dotenv
import psycopg2

class DatabaseManager:
    def __init__(self):
        load_dotenv()
        self.host = os.getenv("DB_HOST")
        self.database =os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
    def insertInitialScore(self,user_id,initial_score):
        try :
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            query = "INSERT INTO user_scores (user_id, initial_score) VALUES (%s, %s);"
            self.cursor.execute(query,(user_id,initial_score))
        except:
            print("Error connecting to database")
        finally:
            self.connection.close()
            self.cursor.close()
    def insertFinalScore(self,user_id,final_score):
        try :
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            query = "INSERT INTO user_scores (user_id, final_score) VALUES (%s, %s);"
            self.cursor.execute(query,(user_id,final_score))
        except:
            print("Error connecting to database")
        finally:
            self.connection.close()
            self.cursor.close()
    def getScores(self,user_id):
        try :
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            query = "SELECT initial_score, final_score FROM user_scores WHERE user_id = %s;"
            self.cursor.execute(query,(user_id))
            row = self.cursor.fetchone()
            if row:
                return row[0],row[1]
        except:
            print("Error connecting to database")
        finally:
            self.connection.close()
            self.cursor.close()

        