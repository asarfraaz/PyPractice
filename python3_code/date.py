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

    def display(val):
        '''
            A method to print ddd, mmm and yyy attributes of Date class
        '''
        print(val.ddd)
        print(val.mmm)
        print(val.yyy)

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
