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
end.ddd = 31
end.mmm = 12
end.yyy = 2021
end.display("xml")

# Copyright 2021 Sarfraaz Ahmed. All rights reserved.
