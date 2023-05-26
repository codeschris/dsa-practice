#the fibonacci sequence generator itself
def fibonacci(range):
    n1, n2 = 0, 1
    count = 0
    if range <= 0:
        return 0
    elif range == 1:
        return "Enter number greater than 1"
    else:
        while count < range:
            print(n1)
            res = n1 + n2
            n1 = n2
            n2 = res
            count += 1

#getting fibonacci sequence value at position provided by the user (Recursion)
def fibfind(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return (fibfind(position - 2) + fibfind(position - 1))

#test cases
print(fibfind(11))
fibonacci(7)
