import pymssql
import datetime



conn = pymssql.connect(host='127.0.0.1:1433', user='yhc', password='111111', database='zhihuDataBase', charset="UTF-8")
cur = conn.cursor()

def insertUser(cur,user_name,mobile,Email,Passwd,SEX,SignDetail):
    insertAccount(cur, Passwd,mobile)
    sql_insert = '''
    INSERT INTO user_info(username,mobile,Email,SEX,Regtime,signDetail)
    VALUES (%s,%d,%s,%s,%s,%s);
    '''
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute(sql_insert, (user_name,mobile, Email,SEX,dt,SignDetail))


def insertAccount(cur,mobile,Passwd):
    sql_insert = '''
    INSERT INTO Account_info
    VALUES (%s,%d);
    '''
    cur.execute(sql_insert, (Passwd,mobile))

def insertQuestion(cur,user_ID,Q_title, Q_text):
    sql_insert = '''
    INSERT INTO question_info(u_id,Q_title,Q_text,Posttime)
    VALUES (%s,%s,%s,%s);
    '''
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute(sql_insert, (user_ID, Q_title,Q_text, dt))

def insertAnswer(cur,Q_ID,user_ID,A_text):
    sql_insert = '''
    INSERT INTO Answer_info(Q_ID,user_ID,A_text)
    VALUES (%d,%d,%d);
    '''
    cur.execute(sql_insert, (Q_ID,user_ID,A_text))

def insertComment(cur,A_ID,user_ID, C_text):
    sql_insert = '''
    INSERT INTO Comment_info(A_ID,user_ID,C_text)
    VALUES (%d,%d,%d);
    '''
    cur.execute(sql_insert, (A_ID,user_ID,C_text))


def insertCollection(cur,Q_ID,user_ID):
    sql_insert = '''
    INSERT INTO Collection_info
    VALUES (%d,%d);
    '''
    cur.execute(sql_insert, (Q_ID,user_ID))

def insertFocus(cur,Auser_ID,Buser_ID):
    sql_insert = '''
    INSERT INTO Focus_info
    VALUES (%d,%d);
    '''
    cur.execute(sql_insert, (Auser_ID,Buser_ID))

def selectAllUser(cur):
    SQL = 'select * from User_info'
    cur.execute(SQL)
    data = cur.fetchall()
    d = []
    for i in data:
        d.append(list(i))
    return  d

def selectAllQuestion(cur):
    SQL = 'select * from Question_info'
    cur.execute(SQL)
    data = cur.fetchall()
    d = []
    for i in data:
        d.append(list(i))
    return  d
def selectALLAnswer(cur):
    SQL = 'select * from Answer_info'
    cur.execute(SQL)
    data = cur.fetchall()
    d = []
    for i in data:
        d.append(list(i))
    return  d
def selectALLComment(cur):
    SQL = 'select * from Comment_info'
    cur.execute(SQL)
    data = cur.fetchall()
    d = []
    for i in data:
        d.append(list(i))
    return  d
def selectAnswerOfQuestion(cur,Q_ID):
    SQL = '''select A_text from Answer_info
             where Q_ID = (%d) '''
    cur.execute(SQL,(Q_ID))
    data = cur.fetchall()
    d = []
    for i in data:
        d.append(list(i))
    return  d


def selectUserTologin(cur,telephone,passwd):
    sql = '''
    SELECT * FROM user_info
    WHERE email ='{}' and mobile = '{}'
    '''.format(passwd,telephone)
    cur.execute(sql)
    data = cur.fetchall()
    d = []
    for i in data:
        d.append(list(i))
    return d

def questionAndfirstAuestion():
    questions = selectAllQuestion(cur)
    # print(questions)
    # print(answers)
    for i in range(len(questions)):
        data = selectAnswerOfQuestion(cur, questions[i][0])
        questions[i].append(data[0])
    return questions

# insertUser(cur,'Yanghc','18800000007','16281053@bjtu.edu.cn','111111','女','脚踏实地，仰望星空')
# print(selectAllUser(cur))

insertQuestion()
cur.close()
conn.commit()
conn.close()