class DBServer:
    def __init__(self, srvr, user, pswd):
        self.remote = srvr
        self.userid = user
        self.passwd = pswd

    def __str__(self):
        return f"{self.remote} : {self.userid}, {self.passwd}"

    def connect(self):
        raise NotImplementedError

    def disconnect(self):
        raise NotImplementedError

    def execute(self, query):
        print("Send the SQL query")
        #req_id = self.conn.send(query)
        #return req_id

    def get_response(self, req_id):
        print("Return the response")
