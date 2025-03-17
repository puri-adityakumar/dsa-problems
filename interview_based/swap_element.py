a = int(input("First element: "))
b = int(input("Second element: "))

def method_a(a,b):
    return b,a

def method_b(a,b):
    a = a + b
    b = a - b
    a = a - b
    
    return a,b


a,b = method_b(a,b)
print(f"first element is {a} & second element is {b} after swapping.")