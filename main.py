import sqlite3

def get_connection(db_name):
    try:
        return sqlite3.connect(db_name)
    except Exception as e:
        print(f"Error: {e}")
        raise
    

def main():
    connection = get_connection("subscribe.db")

if __name__ == "__main__":
    main()