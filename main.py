import os


class Calculator():
    def __init__(self):
        self.a = 0
        self.b = 0
        self.sign=''
        self.sum = 0

    def inputVar(self):
        self.a = eval(raw_input("Enter a: "))
        self.sign=(raw_input("Enter operation: "))
        self.b = eval(raw_input("Enter b: "))

    def operate(self):
        if self.sign == '+':
            self.add()
        elif self.sign == '-':
            self.subtract()
        elif self.sign == '*':
            self.multiply()
        elif self.sign == '/':
            self.divide()
        elif self.sign == '%':
            self.modulo()

    def add(self):
        self.sum= self.a+self.b

    def subtract(self):
        self.sum= self.a-self.b

    def multiply(self):
        self.sum= self.a * self.b

    def divide(self):
        self.sum= ((self.a / self.b) if self.b != 0 else 0)

    def modulo(self):
        self.sum= ((self.a % self.b) if self.b != 0 else 0)

    def showResult(self):
        print "Result: "+str(self.sum)


def main():
    x='a'
    while (x!='z'):
        obj1 = Calculator()
        obj1.inputVar()
        obj1.operate()
        obj1.showResult()
        x = (raw_input("\nEnter any key to continue (z to exit)"))
        print chr(12)



if __name__ == "__main__":
    main()
