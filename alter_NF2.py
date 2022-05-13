import psycopg2
from config import config

def alter_table_NF2():

    commands = (
        """
        ALTER TABLE customers
            DROP COLUMN contact_person;
        """,
        """
        ALTER TABLE customers
            DROP COLUMN contact_person_role;
        """,
        """
        ALTER TABLE customers
            DROP COLUMN phone_number;
        """,
        """
        CREATE TABLE contact_persons (
            id              SERIAL PRIMARY KEY,
            name            VARCHAR(300),
            role            VARCHAR(300),
            phone_number    VARCHAR(15)
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
    alter_table_NF2()