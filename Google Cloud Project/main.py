import functions_framework
import pandas as pd
import sqlalchemy

@functions_framework.http
def insert(request):
  connection_string = connection()
  insert_into_test_table(connection_string)
  return "Data successfully added"

def connection():
  schema = "test_schema"
  host = "12.23.34.45"
  user = "root"
  password = "482382373"
  port = 1234
  db = f"mysql+pymysql://{user}:{password}@{host}:{port}/{schema}"
  return db

def insert_into_test_table(con_str):
  data = {"FirstName": ["Function", "Test"],
          "City": ["Cloud", "Complete"]}
  df = pd.DataFrame(data)
  df.to_sql(name="test_table", con=con_str, if_exists="append", index=False)
