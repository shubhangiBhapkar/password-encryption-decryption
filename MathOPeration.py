class MathOperation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x+self.y
    
    def sub(self):
        return self.x-self.y
    
    def mul(self):
        return self.x*self.y
    
    def div(self):
        try:
            return self.x/self.y
        except ZeroDivisionError as e:
            print(e)
        except TypeError as e:
            print("Invalid input")
        else:
            print(f"{x}/{y}={x/y}")
        finally:
            print("It is always executed:")

obj=MathOperation(100,20)
print(f"{obj.x}+{obj.y}={obj.add()}")
print(f"{obj.x}-{obj.y}={obj.sub()}")
print(f"{obj.x}*{obj.y}={obj.mul()}")
obj.div()
