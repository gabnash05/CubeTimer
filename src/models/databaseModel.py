import threading
import mysql.connector
from config import DATABASE_CONNECTION

class DatabaseModel():
  def __init__(self):
    self.TABLE = "three_cube_times"
    self._connect()

  def _connect(self):
    self.connection = mysql.connector.connect(**DATABASE_CONNECTION)
    self.cursor = self.connection.cursor()
    self._create_tables()

  def _refresh_connection(self):
    self.cursor.close()
    self.connection.close()
    self.connection = mysql.connector.connect(**DATABASE_CONNECTION)
    self.cursor = self.connection.cursor()

  def _create_tables(self):
    # three_cube_times table
    query = """
          CREATE TABLE IF NOT EXISTS three_cube_times (
          id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
          solve_time FLOAT NOT NULL,
          scramble VARCHAR(255),
          solve_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
          is_plus_2 BOOL NOT NULL DEFAULT FALSE,
          is_DNF BOOL NOT NULL DEFAULT FALSE
          ); """
    
    self.cursor.execute(query)
    self.connection.commit()

    # three_cube_ao5 table
    query = """
          CREATE TABLE IF NOT EXISTS three_cube_ao5 (
          id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
          ao5 FLOAT NOT NULL,
          ao5_date TIMESTAMP
          ); """
    
    self.cursor.execute(query)
    self.connection.commit()

    # three_cube_ao12 table
    query = """
          CREATE TABLE IF NOT EXISTS three_cube_ao12 (
          id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
          ao12 FLOAT NOT NULL,
          ao12_date TIMESTAMP
          ); """
    
    self.cursor.execute(query)
    self.connection.commit()

  def saveTimeRecord(self, solve_time, scramble):
    self._refresh_connection()

    query = "INSERT INTO three_cube_times (solve_time, scramble) VALUES (%s, %s)"

    self.cursor.execute(query, (solve_time, scramble))
    self.connection.commit()

  def getTimeRecords(self):
    self._refresh_connection()

    query = "SELECT * FROM three_cube_times ORDER BY id DESC LIMIT 20"
    self.cursor.execute(query)
    result = self.cursor.fetchall()

    return result

  def getTimeRecordsPage(self, page):
    self._refresh_connection()

    offset = page * 20

    if page > 0:
      query = "SELECT * FROM three_cube_times ORDER BY id DESC LIMIT 20 OFFSET (%s)"

      self.cursor.execute(query, offset)
      result = self.cursor.fetchall()

      return result
  
  def deleteTimeRecord(self, solve_id):
    self._refresh_connection()

    try:
      query = 'DELETE FROM three_cube_times WHERE id = (%s)'
      self.cursor.execute(query, (solve_id,))
      self.connection.commit()
    except Exception as e:
      return e
  
  def plus2TimeRecord(self, solve_id):
    self._refresh_connection()

    solve_time_query = 'SELECT solve_time, is_plus_2 FROM three_cube_times WHERE id = (%s)'
    self.cursor.execute(solve_time_query, (solve_id,))
    query_result = self.cursor.fetchall()

    if query_result[0][1] == 0:
      time_plus2 = query_result[0][0] + 2.0

      update_time_query = 'UPDATE three_cube_times SET solve_time = (%s), is_plus_2 = True WHERE id = (%s)'
      self.cursor.execute(update_time_query, (time_plus2, solve_id))
    else:
      time_plus2 = query_result[0][0] - 2.0

      update_time_query = 'UPDATE three_cube_times SET solve_time = (%s), is_plus_2 = False WHERE id = (%s)'
      self.cursor.execute(update_time_query, (time_plus2, solve_id))
    
    self.connection.commit()
  
  def dnfTimeRecord(self, solve_id):
    self._refresh_connection()

    solve_dnf_query = 'SELECT is_DNF FROM three_cube_times WHERE id = (%s)'
    self.cursor.execute(solve_dnf_query, (solve_id,))
    query_result = self.cursor.fetchall()

    if query_result[0][0] == 0:
      update_time_query = 'UPDATE three_cube_times SET is_DNF = True WHERE id = (%s)'
      self.cursor.execute(update_time_query, (solve_id,))
    else:
      update_time_query = 'UPDATE three_cube_times SET is_DNF = False WHERE id = (%s)'
      self.cursor.execute(update_time_query, (solve_id,))
    
    self.connection.commit()

  def getPbRecord(self):
    self._refresh_connection()

    try:
      pb_query = 'SELECT solve_time FROM three_cube_times WHERE is_DNF = FALSE ORDER BY solve_time LIMIT 1;'
      self.cursor.execute(pb_query)
      query_result = self.cursor.fetchall()

      return query_result[0][0]
    except:
      return 0
    
  def getWorstRecord(self):
    self._refresh_connection()

    try:
      worst_query = 'SELECT solve_time FROM three_cube_times WHERE is_DNF = FALSE ORDER BY solve_time DESC LIMIT 1;'
      self.cursor.execute(worst_query)
      query_result = self.cursor.fetchall()

      return query_result[0][0]
    except:
      return 0

  def updateAo5Records(self):
    self._refresh_connection()

    query = "SELECT solve_time, solve_date FROM three_cube_times WHERE is_DNF = FALSE ORDER BY id"
    self.cursor.execute(query)
    results = self.cursor.fetchall()

    ao5_list = []
    for i in range(len(results) - 4):
      five_solves = results[i:i+5]
      ao5_date = five_solves[4][1]
      middle_three = sorted(five_solves)[1:4]
      ao5_time = sum([time[0] for time in middle_three]) / 3.0
      ao5_list.append((ao5_time, ao5_date))

    return ao5_list

  def saveAo5Records(self):
    ao5_list = self.updateAo5Records()

    self.cursor.execute("DELETE FROM three_cube_ao5 WHERE 1=1")
    self.connection.commit()

    query = "INSERT INTO three_cube_ao5 (ao5, ao5_date) VALUES (%s, %s)"
    for ao5 in ao5_list:
      self.cursor.execute(query, (ao5[0], ao5[1]))
    self.connection.commit()
  
  def updateAo12Records(self):
    self._refresh_connection()

    query = "SELECT solve_time, solve_date FROM three_cube_times WHERE is_DNF = FALSE ORDER BY id"
    self.cursor.execute(query)
    results = self.cursor.fetchall()

    ao12_list = []
    for i in range(len(results) - 11):
      five_solves = results[i:i+12]
      ao12_date = five_solves[11][1]
      middle_ten = sorted(five_solves)[1:11]
      ao12_time = sum([time[0] for time in middle_ten]) / 10.0
      ao12_list.append((ao12_time, ao12_date))

    return ao12_list

  def saveAo12Records(self):
    ao12_list = self.updateAo12Records()

    self.cursor.execute("DELETE FROM three_cube_ao12 WHERE 1=1")
    self.connection.commit()

    query = "INSERT INTO three_cube_ao12 (ao12, ao12_date) VALUES (%s, %s)"
    for ao12 in ao12_list:
      self.cursor.execute(query, (ao12[0], ao12[1]))
    self.connection.commit()

  def getAo5Record(self):
    self._refresh_connection()

    try:
      self.cursor.execute("SELECT ao5 FROM three_cube_ao5 ORDER BY id DESC LIMIT 1")
      ao5 = self.cursor.fetchall()
      return ao5[0][0]
    except:
      return 0
    
  def getAo12Record(self):
    self._refresh_connection()

    try:
      self.cursor.execute("SELECT ao12 FROM three_cube_ao12 ORDER BY id DESC LIMIT 1")
      ao12 = self.cursor.fetchall()
      return ao12[0][0]
    except:
      return 0

  def getAo5PbRecord(self):
    self._refresh_connection()

    try:
      self.cursor.execute("SELECT ao5 FROM three_cube_ao5 ORDER BY ao5 LIMIT 1")
      ao5Pb = self.cursor.fetchall()
      return ao5Pb[0][0]
    except:
      return 0
  
  def getAo12PbRecord(self):
    self._refresh_connection()

    try:
      self.cursor.execute("SELECT ao12 FROM three_cube_ao12 ORDER BY ao12 LIMIT 1")
      ao12Pb = self.cursor.fetchall()
      return ao12Pb[0][0]
    except:
      return 0
  
  def getTotalAverageRecord(self):
    self._refresh_connection()

    try:
      self.cursor.execute("SELECT AVG(solve_time) FROM three_cube_times WHERE is_DNF = FALSE")
      total_average = self.cursor.fetchall()

      if total_average[0][0]:
        return total_average[0][0]
      return 0
    except:
      return 0