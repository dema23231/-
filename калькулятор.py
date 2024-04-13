print('калькулятор')
print("Введите q для выхода")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == 'q': break
    if s in ('+', '-', '*', '/'):
        x = float(input("x= "))
        y = float(input("y= "))
        if s == "+":
            print("%.1f" % (x+y))
        elif s == "-":
            print("%.1f" % (x-y))
        elif s == "*":
            print("%.1f" % (x*y))
        elif s == "/":
            print("%.1f" % (x/y))
        else:
            print("Неверный знак!")




