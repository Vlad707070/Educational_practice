class Student:
    def __init__(self, surname, date_of_birth, group, grade):
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.group = group
        self.grade = grade

    def output_of_student_information(self):
        print(self.surname, self.date_of_birth, self.group, self.grade)

students =\
[
    Student("Самоделов", "09.09.2006", "643", [5, 4, 4, 5, 3]),
    Student("Афанасьев", "21.08.2006", "643", [3, 4, 5, 4, 4])
]
input_surname = input("Фамилия: ")
input_the_date_of_birth = input("Дата рождения: ")

for student in students:
    if student.surname == input_surname and student.date_of_birth == input_the_date_of_birth:
        student.output_of_student_information()

        question = input("Хотите изменить данные? да/нет: ")
        if question == "да":
            change_input_surname = input("Изменить фамилию? да/нет: ")
            if change_input_surname == "да":
                new_surname = input("Введите новую фамилию: ")
                student.surname = new_surname

            change_the_date_of_birth = input("Хотите изменить дату рождения? да/нет: ")
            if change_the_date_of_birth == "да":
                new_the_date_of_birth = input("Введите новую дату рождения: ")
                student.date_of_birth = new_the_date_of_birth

            print("Обновленная информация о студенте:")
            student.output_of_student_information()
        break
else:
    print("Студент не найден")