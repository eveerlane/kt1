#КТ1 Перцев Александр ИТ-6

class Quadrilateral:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def perimeter(self):
        return self.a + self.b + self.c + self.d


class Rectangle(Quadrilateral):
    def __init__(self, length, width):
        Quadrilateral.__init__(self,length, width, length, width)


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self,side, side)



if __name__ == "__main__":
    a = 0
    b = 0
    c = 0
    d = 0
    while a<=0 or b<=0 or c <=0 or d<=0:
        a = int(input("Введите первую сторону четырехугольника: "))
        b = int(input("Введите вторую сторону четырехугольника: "))
        c = int(input("Введите третью сторону четырехугольника: "))
        d = int(input("Введите четвертую сторону четырехугольника: "))
        if a<=0 or b<=0 or c <=0 or d<=0:
            print("Сторона четырехугольника не может быть отрицательной или равна нулю!")
            
    quad = Quadrilateral(a, b, c, d)
    print(f"Периметр четырехугольника: {quad.perimeter()}")  
    
    a = 0
    b = 0
    
    while a<=0 or b<=0:
        a = int(input("Введите первую сторону прямоугольника: "))
        b = int(input("Введите вторую сторону прямоугольника: "))
        if a<=0 or b<=0 or c <=0 or d<=0:
            print("Сторона прямоугольника не может быть отрицательной или равна нулю!")
    
    rect = Rectangle(a,b)
    print(f"Периметр прямоугольника: {rect.perimeter()}")  
    
    a = 0
    while a<=0:
        a = int(input("Введите сторону квадрата: "))
        if a<=0:
            print("Сторона квадрата не может быть отрицательной или равна нулю!")
    
    square = Square(a)
    print(f"Периметр квадрата: {square.perimeter()}")  
    
    
'''
TEST1
Введите первую сторону четырехугольника: 1
Введите вторую сторону четырехугольника: 2
Введите третью сторону четырехугольника: 3
Введите четвертую сторону четырехугольника: 4
Периметр четырехугольника: 10
Введите первую сторону прямоугольника: 2
Введите вторую сторону прямоугольника: 4
Периметр прямоугольника: 12
Введите сторону квадрата: 5
Периметр квадрата: 20 


TEST2

'''