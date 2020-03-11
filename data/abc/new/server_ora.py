from server import DBServer

class OracleServer(DBServer):
    def connect(self):
        print("Connect to Oracle server")
        #return "connection object"
