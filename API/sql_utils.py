import mysql.connector

class sql_database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pV=nRt89",
        database = "animal_data")
        self.mycursor = self.mydb.cursor()
    
    def reset_database(self):
        self.mycursor.execute("DROP TABLE IF EXISTS animal_data")
        self.mycursor.execute("DROP TABLE IF EXISTS people_data")
        self.mycursor.execute("CREATE TABLE animal_data (animal_id CHAR(10), is_lost BOOL, animal_name VARCHAR(50), sex CHAR(1))")
        self.mycursor.execute("CREATE INDEX idx_id on animal_data (animal_id)")
    
    def save_animal(self, animal):
        sql = "INSERT INTO animal_data (animal_id, is_lost, animal_name, sex) VALUES (%s, %s, %s, %s)"
        val = [("0000000001", True, "Jerry", "m")]
        print(f"Attempting to execute {sql}, {val}")
        self.mycursor.executemany(sql, val)
        self.mydb.commit()

