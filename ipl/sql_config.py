import psycopg2
import logging
logging.basicConfig(filename='ipl_project.log', level=logging.INFO,
                    format='%(asctime)s:%(module)s:%(funcName)s:%(message)s')


def sql(statement):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        conn = psycopg2.connect(host='localhost',
                                database='Ipl_project',
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
            logging.info('Database connection closed.')

    return output
