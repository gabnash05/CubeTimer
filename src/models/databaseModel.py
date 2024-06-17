import mysql.connector
from config import DATABASE_CONNECTION
from src.util.addZeroToTime import add_zero_to_time

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
  

  def deleteTimeRecord(self, solve_id):
    self._refresh_connection()

    try:
      query = f'DELETE FROM three_cube_times WHERE id = {solve_id}'
      self.cursor.execute(query)
      self.connection.commit()
    except Exception as e:
      return e
  

  def plus2TimeRecord(self, solve_id):
    self._refresh_connection()

    solve_time_query = f'SELECT solve_time, is_plus_2 FROM three_cube_times WHERE id = {solve_id}'
    self.cursor.execute(solve_time_query)
    query_result = self.cursor.fetchall()

    if query_result[0][1] == 0:
      time_plus2 = float(query_result[0][0]) + 2
      time_plus2_formatted = add_zero_to_time(str(time_plus2))

      update_time_query = f'UPDATE three_cube_times SET solve_time = {time_plus2_formatted}, is_plus_2 = True WHERE id = {solve_id}'
      self.cursor.execute(update_time_query)
    else:
      time_plus2 = float(query_result[0][0]) - 2
      time_plus2_formatted = add_zero_to_time(str(time_plus2))

      update_time_query = f'UPDATE three_cube_times SET solve_time = {time_plus2_formatted}, is_plus_2 = False WHERE id = {solve_id}'
      self.cursor.execute(update_time_query)
    
    self.connection.commit()
  
  
  def dnfTimeRecord(self, solve_id):
    self._refresh_connection()

    solve_dnf_query = f'SELECT is_DNF FROM three_cube_times WHERE id = {solve_id}'
    self.cursor.execute(solve_dnf_query)
    query_result = self.cursor.fetchall()

    if query_result[0][0] == 0:
      update_time_query = f'UPDATE three_cube_times SET is_DNF = True WHERE id = {solve_id}'
      self.cursor.execute(update_time_query)
    else:
      update_time_query = f'UPDATE three_cube_times SET is_DNF = False WHERE id = {solve_id}'
      self.cursor.execute(update_time_query)
    
    self.connection.commit()
