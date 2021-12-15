# Copyright 2021 Sarfraaz Ahmed. All rights reserved.

'''
    Date class implementation
'''

#####################
class Date:
    '''
        Represents a date with day,month and year attributes
    '''
    def __init__(self, d=1, m=1, y=1970):
        '''
            A constructor/initialiser of Date class that takes 3 parameters
            Set the 3 parameters as the 3 attributes of the Date object
        '''
        self.ddd = d
        self.mmm = m
        self.yyy = y
        
    def __str__(self):
        '''
            Invoked when user passes Date object as argument to "print()" function
            __str__ method takes higher precedence than __repr__
            This should return a string
        '''
        return f"Str: {self.ddd}-{self.mmm}-{self.yyy}"        
    
    def __repr__(self):
        '''
            Invoked when user passes Date object as argument to "repr()" function
            This should be used to display the internal representation of the object
            This should also return a string
        '''
        return f"Repr: Date({self.ddd}, {self.mmm}, {self.yyy})"    

    def __lt__(self, other):
        '''
            Comparison method for checking this object is less than the other
            This should return a Boolean value
            This is an incomplete implementation and shown only as dummy sample
        '''
        return self.ddd < other.ddd
    
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
print(start)
print(repr(start))

end = Date(31, 12, 2021)
end.display("txt")
print(end)
print(repr(end)) # Simlar to typing ```>>> end ``` on Python Shell

print(start < end)

# Copyright 2021 Sarfraaz Ahmed. All rights reserved.
