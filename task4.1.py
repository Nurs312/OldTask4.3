students = {
    'О.Иванов': 4,
    'И.Петров': 3,
    'Н.Дмитриев': 2,
    'О.Смирнова': 4,
    'В.Керченских': 5,
    'Д.Котов': 2,
    'Н.Бирюкова': 1,
    'П.Данилов': 3,
    'В.Аранских': 5,
    'Ю.Лемонов': 2,
    'Ю.Олегова': 4
}
for student, mark in students.items():
    if mark < 3:
        print(student)
for mark in students.values():
    print(sum(mark))
