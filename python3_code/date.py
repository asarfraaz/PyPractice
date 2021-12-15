# Copyright 2021 Sarfraaz Ahmed. All rights reserved.

'''
    Date class implementation
'''

#####################
class Date:
    '''
        Represents a date with day,month and year attributes
    '''
    ddd = 1
    mmm = 1
    yyy = 1970

    def set_date(self, d, m, y):
        '''
            A method of Date class that takes 3 parameters
            Set the 3 parameters as the 3 attributes of the Date object
        '''
        self.ddd = d
        self.mmm = m
        self.yyy = y

    def display(self, fmt):
        '''
            A method of Date class that takes "fmt" as a parameter
            Prints ddd, mmm and yyy attributes of Date object
            "fmt" parameter specifies the format to print
        '''        
        print("Printing in", fmt, "format")
        print(self.ddd)
        print(self.mmm)
        print(self.yyy)

######################
# Main or client code starts here
start = Date()
start.display("html")

end = Date()
end.set_date(31, 12, 2021)
end.display("txt")

# Copyright 2021 Sarfraaz Ahmed. All rights reserved.
