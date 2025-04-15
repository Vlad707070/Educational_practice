class StorageOfTwoNumbers:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def output_of_numbers(self):
        print(f"{self.number_1}, {self.number_2} - изначальные числа")

    def changing_the_numbers(self, new_number_1, new_number_2):
        self.number_1 = new_number_1
        self.number_2 = new_number_2
        print(f"{self.number_1}, {self.number_2} - измененные числа")

    def the_sum_of_the_numbers(self):
        sum_number = self.number_1 + self.number_2
        return sum_number

    def max_number(self):
        hight_number = max(self.number_1, self.number_2)
        return hight_number

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
storage = StorageOfTwoNumbers(number1, number2)
storage.output_of_numbers()

new_number1 = int(input("Введите новое первое число: "))
new_number2 = int(input("Введите новое второе число: "))
storage.changing_the_numbers(new_number1, new_number2)

print(f"Сумма этих чисел:", storage.the_sum_of_the_numbers())

print(f"Наибольшое значение:", storage.max_number())


