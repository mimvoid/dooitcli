import sqlite3

#  CREATE TABLE todo (
#          id INTEGER NOT NULL,
#          order_index INTEGER NOT NULL,
#          description VARCHAR NOT NULL,
#          due DATETIME,
#          effort INTEGER NOT NULL,
#          recurrence DATETIME,
#          urgency INTEGER NOT NULL,
#          pending BOOLEAN NOT NULL,
#          parent_workspace_id INTEGER,
#          parent_todo_id INTEGER,
#          PRIMARY KEY (id),
#          FOREIGN KEY(parent_workspace_id) REFERENCES workspace (id),
#          FOREIGN KEY(parent_todo_id) REFERENCES todo (id)
#  tableworkspaceworkspace
#  CREATE TABLE workspace (
#          id INTEGER NOT NULL,
#          order_index INTEGER NOT NULL,
#          description VARCHAR NOT NULL,
#          is_root BOOLEAN NOT NULL,
#          parent_workspace_id INTEGER,
#          PRIMARY KEY (id),
#          FOREIGN KEY(parent_workspace_id) REFERENCES workspace (id)

# Connect to the dooit database
connection = sqlite3.connect('dooit.db')
cursor = connection.cursor()

# Read the table contents
def read_table(table: str):
    result = cursor.execute(f"SELECT * FROM {table}")
    rows = result.fetchall()
    return rows

workspaces_table = read_table("workspace")
print(workspaces_table)

todos_table = read_table("todo")
print(todos_table)

connection.close()

# ---------

workspaces = dict()

for i in workspaces_table:
    id = i[0]
    parent_id = i[4]

    if parent_id == 1:
        workspaces[id] = {
            "description" : i[2],
            "order_index" : i[1],
        }
    print(i)
