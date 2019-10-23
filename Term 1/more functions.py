def math_fun(x,y):
    if x.isdigit() and y.isdigit():
        num1 = int (x)
        num2 = int (y)
        total = num1 * num2
    else:
        return"not good inputs",x,y
    return total,num1,num2

x=input("enter a number")
y=input("enter a number")
answer, num1,num2 = math_fun(x,y)
print(num1)
print(num2)
print(answer)
