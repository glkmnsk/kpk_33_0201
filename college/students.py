from college import Human, Student, Group

# students_source = [
#     {
#         'first_name': 'Петр',
#         'last_name': 'Игнаитев',
#         'patronymic': 'Ильич',
#         'date_birth': '10.09.1998',
#         'gender': 'M'
#     },
# ]
#
# print(students_source[0])
#
# student_1 = Student(**students_source[0])
# print(student_1)

# student_1 = Student('Петр', 'Игнатьев', 'Ильич')
# student_2 = Student('Артём', 'Мосин', 'Игоревич')
# student_3 = Student('Дмитрий', 'Ануленко', 'Николаевич')
# student_4 = Student('Никита', 'Муругов', 'Сергеевич')
# student_5 = Student('Роман', 'Косарев', 'Владимирович')
#
#
# group_1 = Group('33', 'Прикладная информатика 09.02.05')
# group_2 = Group('23', 'Прикладная информатика 09.02.05')
# student_1.set_group(group_1)
# student_2.set_group(group_1)
# student_3.set_group(group_1)
# student_4.set_group(group_2)
# student_5.set_group(group_2)
#
# students = [student_1, student_2, student_3, student_4, student_5]
#
# print(f'\nВ мероприятии участвовал:')
# for student in students:
#     print(f'\t{student} ({student.group})')

students_source = open('students.src', 'r', encoding='utf-8').readlines()
students_source = list(map(lambda x: x.replace('\n', '').split(', '), students_source))


students_schema = students_source.pop(0)


students_source_as_dict = list(map(lambda x: dict(zip(students_schema, x)), students_source))


students = []
for student_dict in students_source_as_dict:
    _student = Student(**student_dict)
    students.append(_student)

[print(el) for el in students]
