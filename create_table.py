import psycopg2
from config import config

def create_tables():
    sql = """CREATE TABLE customers (
            name                          VARCHAR(255), 
            industry                      VARCHAR(255), 
            project1_id                   INTEGER, 
            project1_feedback             TEXT, 
            project2_id                   INTEGER,
            project2_feedback             TEXT,
            contact_person_id             INTEGER,
            contact_person_and_role       VARCHAR(300),
            phone_number                  VARCHAR(12),
            address                       VARCHAR(255),
            city                          VARCHAR(255),
            zip                           VARCHAR(5)
        )"""

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute(sql)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()