import mysql.connector
from config import DATABASE_CONNECTION

class DatabaseModel():
  def __init__(self):
    self.connection = mysql.connector.connect(**DATABASE_CONNECTION)
    self.cursor = self.connection.cursor()
    self._create_table()
  
  def _create_table(self):
    query = """
          CREATE TABLE IF NOT EXISTS three_cube_times (
          id INT AUTO_INCREMENT PRIMARY KEY,
              user_id INT NOT NULL,
          solve_time FLOAT NOT NULL,
          scramble VARCHAR(255) NOT NULL,
          solve_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
          is_plus_2 BOOL NOT NULL,
          is_DNF BOOL NOT NULL
          ); """
    
    self.cursor.execute(query)
    self.connection.commit()

  def saveTimeRecord(self, solve_time, scramble):
    query = "INSERT INTO three_cube_times (solve_time, scramble) VALUES (%s, %s)"
    values = (solve_time, scramble)

    self.cursor.execute(query, values)
    self.connection.commit()
  