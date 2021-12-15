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

    def display(self):
        '''
            A method of Date class
            Prints ddd, mmm and yyy attributes of Date object
        '''
        print(self.ddd)
        print(self.mmm)
        print(self.yyy)

######################
# Main or client code starts here
start = Date()
start.display()

end = Date()
end.ddd = 31
end.mmm = 12
end.yyy = 2021
end.display()

# Copyright 2021 Sarfraaz Ahmed. All rights reserved.
