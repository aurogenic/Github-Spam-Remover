import sqlite3
import json

DATABASE_NAME = "data.db"

def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS repositories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                owner VARCHAR(39) NOT NULL,
                name VARCHAR(100) NOT NULL,
                token VARCHAR(40) NOT NULL,
                last_discussion_cursor VARCHAR(64) NOT NULL,
                last_issue_cursor VARCHAR(64) NOT NULL,
                last_pullrequest_cursor VARCHAR(64) NOT NULL
            )
        """
    )
    conn.commit()
    conn.close()

def add_repository(owner, repo, token):
    try: 
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(
            """
                INSERT INTO repositories (owner, name, token, last_discussion_cursor, last_issue_cursor, last_pullrequest_cursor)
                VALUES (?, ?,  ?, '', '', '')
            """, [owner, repo, token]
        )
        print(json.dumps(cursor.lastrowid, indent=2))
        return True
    except Exception as e:
        print("Error Addding repository")
        raise e
        return False
    finally:
        conn.commit()
        conn.close()
    
def dlt_repository(owner, repo):
    try: 
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(
            """
                DELETE FROM repositories WHERE (owner = ?) AND (name=?)
            """, [owner, repo]
        )
        print()
        return True
    except Exception as e:
        print("Error Addding repository")
        raise e
        # return False
    finally:
        conn.commit()
        conn.close()
    
def update_token():
    #todo
    pass

def fetch_repository(owner, repo):
    try: 
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(
            """
                SELECT * FROM repositories WHERE (owner = ?) AND ( name = ?)
            """, [owner, repo]
        )
        result = cursor.fetchall()
        if result:
            return result[0]
        else:
            return []
    except Exception as e:
        print("Error Addding repository")
        raise e
        # return False
    finally:
        conn.commit()
        conn.close()

def fetch_all_repositories():
    try: 
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(
            """
                SELECT * FROM repositories
            """
        )
        return cursor.fetchall()
    except Exception as e:
        print("Error Addding repository")
        raise e
        # return False
    finally:
        conn.commit()
        conn.close()

def update_token(id, token):
    try: 
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(
            """
                UPDATE repositories SET token = ? WHERE id=?
            """, [id, token]
        )
        return cursor.fetchall()
    except Exception as e:
        print("Error Addding repository")
        raise e
        # return False
    finally:
        conn.commit()
        conn.close()

def fetch_repository_by_id(id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT * FROM repositories WHERE id = ?
        """, [id])
        return cursor.fetchone()
    except Exception as e:
        print("Error getting repository")
        raise e
    finally:
        conn.commit()
        conn.close()

def update_discussion_cursor(id, discussion_cursor):
    try: 
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(
            """
                UPDATE repositories SET last_discussion_cursor = ? WHERE id=?
            """, [discussion_cursor, id]
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print("Error Addding repository")
        raise e

def update_issue_cursor(id, discussion_cursor):
    try: 
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(
            """
                UPDATE repositories SET last_issue_cursor = ? WHERE id=?
            """, [discussion_cursor, id]
        )
        return True
    except Exception as e:
        print("Error Addding repository")
        raise e
        # return False
    finally:
        conn.commit()
        conn.close()


def update_pullrequest_cursor(id, discussion_cursor):
    try: 
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute(
            """
                UPDATE repositories SET last_pullrequest_cursor = ? WHERE id=?
            """, [discussion_cursor, id]
        )
        return True
    except Exception as e:
        print("Error Addding repository")
        raise e
        # return False
    finally:
        conn.commit()
        conn.close()
create_table()