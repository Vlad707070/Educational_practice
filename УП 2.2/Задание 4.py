class Counter:
    def __init__(self, count):
        self.count = count

    def shows_the_current_number(self):
        print(f"{self.count} - начальное число")

    def increases_by_one(self):
        enlarged = self.count + 1
        print(f"{enlarged} - новое число увеличенное на один")

    def decreases_by_one(self):
        reduced = self.count - 1
        print(f"{reduced} - новое число уменьшенное на один")


def checks_the_number():
    while True:
        user_input = input("Введите число(начальное значение счетчика). В противном случае значение по умолчанию будет 0: ")
        if not user_input:
            print("Начальное значение взято как по умолчанию и равно 0")
            return 0

        try:
            return int(user_input)
        except ValueError:
            print(f"вы ввели {type(user_input)}, а надо ввести число. Попробуйте еще раз")

value = checks_the_number()
counter = Counter(value)
counter.shows_the_current_number()
counter.increases_by_one()
counter.decrease_by_one()