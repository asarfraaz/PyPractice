from server import DBServer

class MySQLServer(DBServer):
    def connect(self):
        print("Connect to MySQL server")
        #return "connection object"
