import mysql.connector
from config import DATABASE_CONNECTION

class DatabaseModel():
  def __init__(self):
    self._connect()
  

  def _connect(self):
    self.connection = mysql.connector.connect(**DATABASE_CONNECTION)
    self.cursor = self.connection.cursor()
    self._create_table()


  def _refresh_connection(self):
    self.cursor.close()
    self.connection.close()
    self._connect()

  
  def _create_table(self):
    query = """
          CREATE TABLE IF NOT EXISTS three_cube_times (
          id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
          solve_time VARCHAR(255) NOT NULL,
          scramble VARCHAR(255) NOT NULL,
          solve_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
          is_plus_2 BOOL NOT NULL DEFAULT FALSE,
          is_DNF BOOL NOT NULL DEFAULT FALSE
          ); """
    
    self.cursor.execute(query)
    self.connection.commit()


  def saveTimeRecord(self, solve_time, scramble):
    self._refresh_connection()

    query = "INSERT INTO three_cube_times (solve_time, scramble) VALUES (%s, %s)"
    values = (solve_time, scramble)

    self.cursor.execute(query, values)
    self.connection.commit()


  def getTimeRecords(self):
    self._refresh_connection()

    query = "SELECT * FROM three_cube_times ORDER BY id DESC LIMIT 20"
    self.cursor.execute(query)
    result = self.cursor.fetchall()

    return result


  def getTimeRecordsPage(self, page):
    self._refresh_connection()

    if page > 0:
      query = f"SELECT * FROM three_cube_times ORDER BY id DESC LIMIT 20 OFFSET {(page - 1) * 20}"

      self.cursor.execute(query)
      result = self.cursor.fetchall()

      return result
  
  
