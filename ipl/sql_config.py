import psycopg2
import logging
logging.basicConfig(filename='ipl_project.log', level=logging.DEBUG,
                    format='%(asctime)s:%(module)s:%(funcName)s:%(message)s')


def sql(statement):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        conn = psycopg2.connect(host='localhost',
                                database='postgres',
                                user='postgres',
                                password='121')
        cur = conn.cursor()
        cur.execute(statement)
        output = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        logging.debug(error)
    finally:
        if conn is not None:
            conn.close()
            logging.debug('Database connection closed.')

    return output
