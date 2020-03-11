class MySQLServer:
    def __init__(self, srvr, user, pswd):
        self.srvr = srvr
        self.user = user
        self.pswd = pswd

    def __del__(self):
        self.ms_disconnect()

    def ms_connect(self):
        print("Connecting to MySQL server")

    def ms_disconnect(self):
        print("Disconnecting from MySQL server")

    def ms_execute(self, query):
        print("Send the SQL query")

    def ms_get_response(self, req_id):
        print("Return the response")
