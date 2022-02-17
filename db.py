import pymysql


username = "root"
host="localhost"
password= ""
dbname = "student_db"



def connect():
    db = pymysql.connect(user=username,host=host,password=password,db=dbname)
    return db


# get students
def get_students():
    
    try:
        db = connect()
        cs = db.cursor()
        sql = "select * from students"
        cs.execute(sql)
        students = cs.fetchall()
        return students
    except:
        return False
    finally:
        db.close()
        
        
# insert student  
def insert_student(name,marks):    
    
    try:
        db = connect()
        cs = db.cursor()
        sql = "insert into students (name,marks) values (%s,%s)"
        values = (name,marks)
        cs.execute(sql,values)
        db.commit()
        return True       
    except:
        return False
    finally:
        db.close()
       


# update student marks 

def update_marks(id,marks):    
    
    try:
        db = connect()
        cs = db.cursor()
        sql = "update students set marks=%s where id=%s"
        values = (marks,id)
        cs.execute(sql,values)
        db.commit()
        return True       
    except:
        return False
    finally:
        db.close()


# single student

def get_student(id):
    
    try:
        db = connect()
        cs = db.cursor()
        sql = "select * from students where id=%s"
        value=(id,)
        cs.execute(sql,value)
        student = cs.fetchone()
        return student
    except:
        return False
    finally:
        db.close()


# delete student

def delete_student(id):
    try:
        db = connect()
        cs = db.cursor()
        sql = "delete from students where id=%s"
        value = (id,)
        cs.execute(sql,value)
        db.commit()
        return True
    except:
        return False
    finally:
        db.close()



    




























