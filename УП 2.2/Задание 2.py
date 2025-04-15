class Trains:
    def __init__(self, destination_point, train_number, departure_time):
        self.destination_point = destination_point
        self.train_number = train_number
        self.departure_time = departure_time

    def train_information_output(self):
        print(self.destination_point, self.train_number, self.departure_time)

trains =\
    [
        Trains("Асино", "101", "13:10"),
        Trains("Болотное", "102", "13:30")
    ]
input_the_train_number = input("Введите номер поезда, чтоб получить информацию о нем: ")

for train in trains:
    if train.train_number == input_the_train_number:
        train.train_information_output()
        break
else:
    print("Номер такого поезда не существует")


