class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_rate(self):
        return self.__rate

    def get_days(self):
        return self.__days

    def GetSalary(self):
        salary = self.__rate * self.__days
        print(f"Зарплата {self.__name} {self.__surname} = {salary} руб.")

workers =\
    [
        Worker("Владислав", "Самоделов", 5000, 22),
        Worker("Сергей", "Петров", 3500, 21)
    ]

for worker in workers:
    worker.GetSalary()