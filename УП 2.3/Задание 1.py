class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def GetSalary(self):
        salary = self.rate * self.days
        print(f"Зарплата {self.name} {self.surname} = {salary} руб.")

workers =\
    [
        Worker("Владислав", "Самоделов", 5000, 22),
        Worker("Сергей", "Петров", 3500, 21)
    ]

for worker in workers:
    worker.GetSalary()