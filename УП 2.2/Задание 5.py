class Example:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print(f"Объект создан: x = {self.x}, y = {self.y}")

    def show(self):
        print(f"x = {self.x}, y = {self.y}")

    def __del__(self):
        print(f"Объект с x = {self.x}, y = {self.y} удалён")

print("Создание объекта с заданными значениями:")
obj1 = Example(5, 10)
obj1.show()

print("\nСоздание объекта со значениями по умолчанию:")
obj2 = Example()  # x=0, y=0
obj2.show()

print("\nУдаление объектов:")
del obj1
del obj2

print("Программа завершена.")
