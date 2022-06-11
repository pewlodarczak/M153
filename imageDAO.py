from asyncio.windows_events import NULL
import psycopg2
from config import config
import dbGUI
from rich import print as rprint
from rich.console import Console
from os import system

console = Console()

class imageDAO():
    
    def create_table(self):
        sql = """CREATE TABLE images (
                IMG_ID                        SERIAL PRIMARY KEY,
                title                         VARCHAR(255), 
                description                   VARCHAR(255),
                image_file                    BYTEA 
            )"""

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


    def drop_table(self):
        sql = """DROP TABLE images; 
            """

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

    def insert_image(self, title, path_to_file, description):
        sql = "INSERT INTO images(title,image_file,description) VALUES(%s,%s,%s)"
    
        img = open(path_to_file, 'rb').read()
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql, (title, psycopg2.Binary(img), description))
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def read_image(self, title):
        sql = "SELECT title, description, image_file FROM images WHERE images.title = %s "
        
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql, (title,))
            blob = cur.fetchone()
            open('download/' + blob[0] + '.gif', 'wb').write(blob[2])
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


    def delete_image(self, id):
        sql = "DELETE FROM images WHERE images.img_id = %s"
        self.execute(sql, id)


    def execute(self, sql, id):
        conn = None
        blob = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql, (id,))
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

def main():
    imgDAO = imageDAO()
    toDo = ''
    num = 0
    while toDo != '4':
        ''''
        print('What do you want to do:')
        print('c    create table')
        print('d    drop table')
        print('i    insert image')
        print('r    read image')
        print('del  delete image')
        print('q    quit')
        '''

        dbGUI.printMenu(num)

        toDo = input()
        if toDo == 'c':
            imgDAO.create_table()
        elif toDo == 'd':
            imgDAO.drop_table()
        elif toDo == '1':
            imgDAO.insert_image("Cola", 'img/Cola.gif', "Cocacola")
            num = 1
            system('cls')
        elif toDo == '2':
            imgDAO.read_image('Cola')
            num = 2
            system('cls')
        elif toDo == '3':
            imgDAO.delete_image(7)
        elif toDo == '4':
            print()
            #rprint(['Au revoir', '😎'])
            print('👋')
            #console.print(":thumbs_up: Hasta la vista, baby")
            #rprint('Hasta la vista, baby', '👽')
            console.print('Hasta la vista, baby', style="blink bold red underline on white")
            print()
        else:
            print('wrong command')


if __name__ == '__main__':
    main()
