import sqlite3
from sqlite3 import Error
from os import path
from datetime import datetime

ROOT = path.dirname(path.realpath(__file__))

def create_connection():
    try:
        conn = sqlite3.connect(path.join(ROOT, "answers_small.db"))
        return conn
    except Error as e:
        print(e)

    return None

def get_questions(start, end):
    conn = create_connection()

    with conn:
        sql = " SELECT * FROM answers"
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows

def get_questions_on_hold():
    conn = create_connection()

    with conn:
        sql = " SELECT * FROM questions"
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows

def add_question_func(question_text, parameter1_text, parameter2_text, keyword1_text, keyword2_text, detailedanswer_text, category_text):
    conn = create_connection()

    with conn:
        cur = conn.cursor()
        sql  = "INSERT INTO answers(question, parameter1, parameter2, keyword1, keyword2, detailedanswer, module_ID) " \
               "VALUES('"+ question_text +"','"+parameter1_text+"','"+parameter2_text+"','"+keyword1_text+"','"+keyword2_text+"','"+detailedanswer_text+"','"+category_text+"')  "
        try:
            temp = cur.execute(sql )
            if cur.lastrowid > 0:
                return 'singup,Singup OK'
        except Error as e:
            return e

def add_question_on_hold(question_text):
    conn = create_connection()

    with conn:
        cur = conn.cursor()
        time_date_current = str(datetime.now())
        sql  = "INSERT INTO questions(question, time_date) " \
               "VALUES('"+ question_text +"','"+time_date_current+"')  "
        try:
            temp = cur.execute(sql )
            if cur.lastrowid > 0:
                return 'singup,Singup OK'
        except Error as e:
            print(e)
            return e

# while True:
#     print(add_question_func())
#     input('Added:')

# while True:
#     qn = input('Q: ')
#     add_question_on_hold(qn)

