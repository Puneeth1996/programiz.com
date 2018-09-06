def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
printer("Hello")




"""

The Folowing shows the output



his will give the output.


******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Hello
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************
The above syntax of,

@star
@percent
def printer(msg):
    print(msg)
is equivalent to

def printer(msg):
    print(msg)
printer = star(percent(printer))
The order in which we chain decorators matter. If we had reversed the order as,

@percent
@star
def printer(msg):
    print(msg)
The execution would take place as,

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************
Hello
******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
