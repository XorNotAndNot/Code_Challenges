def t24_game(l):
    
    # setting up w,x,y,z
    w,x,y,z = l[0], l[1], l[2], l[3]

    # range rule
    for val in l:
        if not(1 <= val <= 9):
            print("{0} not in range.".format(val))
            break
        continue
        
    # truth check
    truth = True if ((w*x-y)*z == 24) else False
    print(truth)

# list creation with exception handling for invalid inputs.
l = []
try:
    for i in range(1,5):
        val = int(input("Enter value{0}: ".format(i)))
        l.append(val)
except (NameError, SyntaxError, ValueError):
    print("Invalid input")

t24_game(l) # function call
