import sys
import psycopg2
import psycopg2.extras
from pprint import pprint


def connect():
    user = "postgres"
    password = "1337"
    host = "127.0.0.1"
    database = "postgres"
    port = "5432"
    connection = psycopg2.connect(host=host,
                                  user=user,
                                  password=password,
                                  database=database,
                                  port=port
                                  )
    connection.autocommit = True
    return connection


def reqDictn(script):
    connection = connect()
    cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(script)
    result = cur.fetchall()
    connection.close()
    cur.close()
    return result

def reqSimp(script):
    connection = connect()
    cur = connection.cursor()
    cur.execute(script)
    connection.close()
    cur.close()

"""
Остальные виды запросов закоменчены на будущее
"""
# def reqDict1(script):
#     connection = connect()
#     cur = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
#     cur.execute(script)
#     result = cur.fetchone()
#     connection.close()
#     cur.close()
#     return result


