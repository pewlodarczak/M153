import psycopg2
from config import config

def alter_table_NF3():

    commands = (
        """
        ALTER TABLE customers
            DROP COLUMN city;
        """,
        """
        CREATE TABLE zips (
            zip             VARCHAR(5) PRIMARY KEY,
            city            VARCHAR(300)
        );
        """
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
    alter_table_NF3()