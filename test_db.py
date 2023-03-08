#%%
import sqlite3
import pandas as pd

# %%
sqliteConnection = sqlite3.connect('ee_db.sqlite3')
cursor = sqliteConnection.cursor()
#%%
query = 'select * from participants;'
df = pd.read_sql_query(query, sqliteConnection)

#%%
cursor.execute('''INSERT INTO participants VALUES ('ee', '0', 'test user', 'm', 16, 123, 'email', 'test em', 124, 'addr, 700', 'a+', 'bike', 0, 'True')''')
# %%
sqliteConnection.commit()
sqliteConnection.close()
# %%
x = "ee|0|test user|m|16|123|mail@domain.com|test em|124|11, street name, city, 7012345|700|A+|bike_type|0|True"
z = x.split("|")
# %%
q = 'INSERT INTO participants VALUES (' + str(z)[1:-1] + ')'
# %%
