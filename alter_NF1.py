import psycopg2
from config import config

def alter_table_NF1():

    commands = (
        """ ALTER TABLE customers
            ADD COLUMN id SERIAL PRIMARY KEY;
        """,
        """
        ALTER TABLE customers
    DROP COLUMN contact_person_and_role;
""",
"""
ALTER TABLE customers
    ADD COLUMN contact_person VARCHAR(300);
        """,
"""
ALTER TABLE customers
    ADD COLUMN contact_person_role VARCHAR(300);
        """
        ,
        """
        ALTER TABLE customers
    DROP COLUMN project1_id;
""",
"""
        ALTER TABLE customers
    DROP COLUMN project1_feedback;
""",
        """
        ALTER TABLE customers
    DROP COLUMN project2_id;
""",
"""
        ALTER TABLE customers
    DROP COLUMN project2_feedback;
""",

        """
        CREATE TABLE project_feedbacks (
    id                  SERIAL PRIMARY KEY,
    project_id          INTEGER, 
    customer_id         INTEGER,
    project_feedback    TEXT
);
"""
,
"""
CREATE TABLE projects (
    id                  SERIAL PRIMARY KEY,
    name                VARCHAR(300),
    start_date          DATE,
    end_date            DATE
);"""
        )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
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
    alter_table_NF1()