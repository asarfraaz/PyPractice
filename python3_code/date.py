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

######################

# Below code is outside of Date class
def display(val):
    print(val.ddd)
    print(val.mmm)
    print(val.yyy)

# Main or client code starts here
start = Date()
display(start)

end = Date()
end.ddd = 31
end.mmm = 12
end.yyy = 2021
display(end)

# Copyright 2021 Sarfraaz Ahmed. All rights reserved.
