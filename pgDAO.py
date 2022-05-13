import psycopg2
from config import config

class pgDAO():
    
    def saveCustomer(self, name, industry):
        sql = """INSERT INTO customers(name, industry)
             VALUES(%s,%s) RETURNING id;
        """
        record_to_insert = (name, industry)
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql, record_to_insert)
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def saveContact(self, name, role):
        sql = """INSERT INTO contact_persons(name, role)
             VALUES(%s,%s) RETURNING id;
        """
        record_to_insert = (name, role)
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql, record_to_insert)
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def addContact(self, name, customer):

        sql_select = """SELECT id from contact_persons where name = %s"""

        sql_update = """UPDATE customers set contact_person_id =%s where name = %s;"""

        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            cur.execute(sql_select, (name,))
            id = cur.fetchone()
            print(id)
            cur.execute(sql_update, (id, customer))
            count = cur.rowcount
            print(count, "Record Updated successfully ")
            cur.close()
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


daoObj = pgDAO()

#daoObj.saveCustomer('ACME', 'Manufacture')
#daoObj.saveContact('Smith', 'PL')
daoObj.addContact('Smith', 'ACME')

