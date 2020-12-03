#__name__ = "__main__"
current_value = 0
mem = current_value
prev = current_value

def display_current_value():
    print(current_value)

def initialize():
    global current_value
    current_value = 0
    global mem
    global prev
    mem = current_value
    prev = current_value
def get_current_value():
    return current_value
def add(to_add):
    global current_value
    global prev
    prev = current_value
    current_value = current_value + to_add
    #print(current_value)
def subtract(num):
    global current_value
    global prev
    prev = current_value

    current_value = current_value - num
    #print(current_value)

def multiply(num):
    global current_value
    global prev
    prev = current_value
    current_value = current_value * num
    #print(current_value)


def divide(num):
    global current_value

    if num == 0:
        print("Math Error")
    else:
        global prev
        prev = current_value
        current_value = current_value / num
        #print(current_value)

def memory():
    global mem
    global current_value
    mem =  current_value

def recall():
    global mem
    print(mem)
    return mem
def undo():
    global current_value
    global prev
    temp = current_value
    current_value = prev
    prev = temp

    #print(current_value)



if __name__ == "__main__":
    print("Welcome to the calculator program.")
    print("Current value:", current_value)
    #display_current_value()
    display_current_value() # 0
    add(5) # 5
    subtract(2)
    display_current_value() # 3
    undo()
    display_current_value() # 5
    undo()
    display_current_value() # 3
    multiply(10)
    display_current_value() # 30
    undo()
    undo()
    display_current_value() # 30
    undo()
    undo()
    undo()
    display_current_value() # 3
