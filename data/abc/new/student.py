from server_mysql import MySQLServer

class Student:
    def __init__(self, name, marks):
        self.stu_name = name
        self.stu_marks = marks

    def __del__(self):
        #self.db.ms_disconnect()
        self.db.disconnect()

    def set_db(self, srvr):
        self.db = srvr
        self.db.connect()

    def store(self):
        sql_cmd = f"add info {self.stu_name}"
        #res = self.db.ms_execute(sql_cmd)
        ack_id = self.db.execute(sql_cmd)
        resp = self.db.get_response(ack_id)

# Main
stu1 = Student("Ajay", 90)
srvr = MySQLServer("akash", "admin", "12345")
stu1.set_db(srvr)
stu1.store()
del stu1
