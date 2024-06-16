import sqlite3
import os
import re

db = sqlite3.connect('Nikita_Pushnov_a.sqlite')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS recording_logs(
 ip TEXT,
 text_block TEXT,
 username TEXT,
 data_time TEXT,
 file_route TEXT,
 code_and_number_of_bytes TEXT
)""")

def function_1(text):
  return list(map(lambda x: [x.group(1),x.group(2),x.group(3),x.group(4),x.group(5),x.group(6)], text))
def parsing():
  separation = re.compile(r'(\d*[.]\d*[.]\d*[.]\d*) (.*) (.*) [[](.*)[]] "(.*)" (\d* \d*)')
  f = open(os.path.dirname(os.path.abspath(file))+"\\test.log", 'r')
  mas =function_1(separation.finditer(f.read()))
  for i in range(len(mas)):
   sql.execute(f"INSERT INTO recording_logs VALUES ('{mas[i][0]}', '{mas[i][1]}', '{mas[i][2]}', '{mas[i][3]}','{mas[i][4]}','{mas[i][5]}')")
  print("парсинг успешно сделон")
#=======================================2
def viewing():
 for i in sql.execute("SELECT * FROM recording_logs"):# я фильтр
  if i[3] < "16"    print(i)
def viewing(): for i in sql.execute("SELECT * FROM recording_logs"):
  if i[3] < "16"    print(i)
for i in sql.execute("SELECT * FROM recording_logs"):
    if i[3] < "16":
        print(i)
#=======================================
start_end = True
while(start_end):
 main_menu=input("1.парсинг, 2.просмотр, 3.закончить программу")
 if main_menu=='1':
  parsing()
 elif main_menu=='2':
  viewing()
 elif main_menu=='3':
  start_end=False
db.commit()