import psycopg2
from config import config

def create_tables():
    sql = """CREATE TABLE employees (
    employee_name                 VARCHAR(255),
    employee_role1                VARCHAR(255),
    employee_role2                VARCHAR(255),
    employee_role3                VARCHAR(255),
    employee_address              VARCHAR(255),
    employee_manager              VARCHAR(255),
    industry                      VARCHAR(255),
    employee_id                   INTEGER,
    customer_project1    		  VARCHAR(255),
    customer_project1_feedback    TEXT,
    customer_project2    		  VARCHAR(255),
    customer_project2_feedback    TEXT,
    customer_contact_person       VARCHAR(255),
    phone_number                  INTEGER,
    customer1_address             VARCHAR(255),
    customer2_address             VARCHAR(255)        )"""

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()