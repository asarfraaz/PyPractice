from server import MySQLServer

class Student:
    def __init__(self, name, marks):
        self.stu_name = name
        self.stu_marks = marks

    def __del__(self):
        #self.db.ms_disconnect()
        del self.db

    def create_db(self, host, user, pswd):
        self.db = MySQLServer(host, user, pswd)
        self.db.ms_connect()

    def store(self):
        sql_cmd = f"add info {self.stu_name}"
        ack_id = self.db.ms_execute(sql_cmd)
        resp = self.db.ms_get_response(ack_id)

# Main
stu1 = Student("Ajay", 90)
stu1.create_db("akash", "admin", "12345")
stu1.store()
del stu1
