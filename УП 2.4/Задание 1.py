import sqlite3
import json


class Student:
    def __init__(self, name: str, surname: str, patronymic: str, group: str, grades: list[int]):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.group = group

        if len(grades) == 4:
            self.grades = grades
        else:
            raise ValueError("Вы ввели больше оценок, нужно четыре")


class StudentStorage:
    def __init__(self, data_base: str):
        self.data_base = data_base
        self.connection = sqlite3.connect(self.data_base)
        self.cursor = self.connection.cursor()
        self._create_data_table()


    def _create_data_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Students
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                            name TEXT, 
                            surname TEXT,
                            patronymic TEXT,
                            group_name TEXT,
                            grades TEXT)
                        """)

    def add_new_student(self, student:Student):
        self.cursor.execute(
            "INSERT INTO Students (name, surname, patronymic, group_name, grades) VALUES (?, ?, ?, ?, ?)",
            (student.name, student.surname, student.patronymic, student.group, json.dumps(student.grades))
        )
        self.connection.commit()

    def get_all_students(self):
        self.cursor.execute("SELECT * FROM Students")
        return self.cursor.fetchall()

    def get_average_grade_by_student_name(self, student:Student):
        self.cursor.execute("SELECT * FROM Students WHERE name=? AND surname=? AND patronymic=?", (student.name, student.surname, student.patronymic))
        data = self.cursor.fetchone()
        student_data = Student(
            name = data[1], surname = data[2], patronymic = data[3], group = data[4], grades = json.loads(data[5])
        )
        average_grade = (sum(student_data.grades) / len(student_data.grades))
        return average_grade, student_data.name, student_data.surname

    def edit_student(self, old_student:Student, new_student:Student):
        self.cursor.execute("UPDATE Students SET name=?, surname=?, patronymic=?, group_name=?, grades=?"
                            "WHERE name=? AND surname=? AND  patronymic=? AND  group_name=? AND grades=?",
                            (new_student.name, new_student.surname, new_student.patronymic, new_student.group, json.dumps(new_student.grades),
                            old_student.name, old_student.surname, old_student.patronymic, old_student.group, json.dumps(old_student.grades)))
        self.connection.commit()

    def delete_student(self, student:Student):
        self.cursor.execute("DELETE FROM Students WHERE name=? AND surname=? AND patronymic=?", (student.name, student.surname, student.patronymic))
        self.connection.commit()

    def get_average_grade_by_group_name(self, group_name: str):
        self.cursor.execute("SELECT * FROM Students WHERE group_name=?", (group_name,))
        data = self.cursor.fetchall()
        average_grades_all_students = []
        for row in data:
            student_grades = json.loads(row[5])
            average_grade = (sum(student_grades) / len(student_grades))
            average_grades_all_students.append(average_grade)

        return sum(average_grades_all_students) / len(average_grades_all_students)


if __name__ == "__main__":
    ivan_ivanov = Student("Ivan", "Ivanov", "Ivanovich", "333", [3, 3, 5, 4])
    petr_ivanov = Student("Petr", "Ivanov", "Ivanovich", "222", [4, 4, 5, 4])
    artem_ivanov = Student("Artem", "Ivanov", "Ivanovich", "333", [3, 3, 5, 4])

    # student_storage = StudentStorage("Students")
    # # student_storage.add_new_student(ivan_ivanov)
    # # student_storage.add_new_student(petr_ivanov)
    # # student_storage.add_new_student(artem_ivanov)
    # # print(student_storage.get_all_students())
    # # student_storage.delete_student(ivan_ivanov)
    # print(student_storage.get_all_students())
    # # print(student_storage.get_average_grade_by_student_name(petr_ivanov))
    # # print(student_storage.get_average_grade_by_student_name(petr_ivanov))
    # # print(student_storage.get_average_grade_by_group_name("333"))
    # new_petr_ivanov = Student("Petr", "Samodelov", "Andreevich", "222", [4, 4, 5, 4])
    # print(student_storage.edit_student(petr_ivanov, new_petr_ivanov))
    # print(student_storage.get_average_grade_by_student_name(new_petr_ivanov))
    # new_petr_vasilevich = Student("Petr", "Samodelov", "Vasilevich", "223", [2, 3, 4, 5, ])
    # print(new_petr_vasilevich)