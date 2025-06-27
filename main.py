import sqlite3

def get_connection(db_name):
    try:
        return sqlite3.connect(db_name)
    except Exception as e:
        print(f"Error: {e}")
        raise

def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
    """
    try :
        with connection:
            connection.execute(query)
        print("table was created!")
    except Exception as e :
        print(e)


def insert_user(connection, name:str, age:int, email:str):
    query = "Insert INTO users (name, age, email) VALUES(?,?,?)"
    try:
        with connection:connection.execute(query, (name, age, email))
        print(f"User: {name} was added to your database!")
    except Exception as e:
        print(e)
    

def fetch_users(connection, condition: str = None) -> list[tuple]:
    query = "SELECT * FROM users"
    if condition :
        query += f"WHERE{condition}"
    
    try:
        with connection:
            rows = connection.execute(query).fetchall()
            return rows
        
    except Exception as e:
        print(e)

def delete_user(connection, user_id:int):
    query = "DELETE FROM user WHERE id = ?"
    try:
        with connection:
            connection.execute(query,(user_id))
        print(f"USER ID: {user_id} was deleted!")
    except Exception as e:
        print(e)

def update_user(connection, user_id:int, email:str):
    query = "UPDATE user SET email = ? WHERE id = ?"
    try :
        with connection:
            connection.execute(query, (email, user_id))
        print(f"User ID {user_id} has new email of {email}")
    except Exception as e:
        print(e)
    
def insert_user(connection, users:list[tuple[str, int, str]]):
    query = "INSERT INTO users (name, age, email) VALUES (?,?,?)"
    try:
        with connection:
            connection.executemany(query, users)
            print(f"{len(users)} users were added to the database!")
    except Exception as e:
        print(e)

def main():
    connection = get_connection("subscribe.db")
    try:
        create_table(connection)

        start = input("Enter Option (Add, Delete, Update, Search, Add Many)").lower()
        if start == "add":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            insert_user(connection, name, age, email)
        
        elif start == "search":
            print("ALL Users:")
            for user in fetch_users(connection):
                print(user)

        elif start == "delete":
            user_id = int(input("Enter User id: "))
            delete_user(connection, user_id)
        elif start == "update":
            user_id = int(input("Enter User id: "))
            new_email = input("Enter new email: ")
            update_user(connection, user_id, email)
        
        elif start == "add many":
            users = [("Chandler", 29, "none@gmail.com"),
                     ("Jinja", 24, "jinja@gmail.com"),
                     ("fuska", 20, "fuska@gmail.com")]
            insert_user(connection, users)

    finally:
        connection.close()


if __name__ == "__main__":
    main()