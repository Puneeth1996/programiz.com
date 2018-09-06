
# Scopes of local variables 

def outer_function():
    a = 20
    def inner_function():
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)
     
a = 10
outer_function()
print('a =',a)


# scope of variable when a global space is created 

def outer_function():
    global a
    a = 20
    def inner_function():
        global a
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)
     
a = 10
outer_function()
print('a =',a)
