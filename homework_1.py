import pandas as pd

# Пункт 1
# Створіть DataFrame з ім'ям "students", який містить такі стовпці:
# "Name" (ім'я студента)
# "Age" (вік студента)
# "Gender" (стать студента)
# "Score" (оцінка студента за певний предмет)
data = {
    "Name": ["Олег", "Оксана", "Олександр", "Ольга", "Джон"],
    "Age": [20, 22, 21, 19, 23],
    "Gender": ["чоловіча", "жіноча", "чоловіча", "жіноча", "чоловіча"],
    "Score": [85, 92, 69, 95, 76]
}

students = pd.DataFrame(data)

# Пункт 2
# Додайте в DataFrame "students" декілька рядків з інформацією про різних студентів.
# new_data = {
#     "Name": ["Анна", "Василь", "Тетяна"],
#     "Age": [20, 22, 21],
#     "Gender": ["жіноча", "чоловіча", "жіноча"],
#     "Score": [90, 85, 95]
# }
#
# new_data = pd.DataFrame(new_data)
# students = pd.concat([students, new_data], ignore_index=True)

# Пункт 3
# Виведіть перші 5 рядків з DataFrame "students".
# first_five_string = students.head(5)
# print(first_five_string)

# Пункт 4
# Обчисліть середній вік студентів.
# average_age = students["Age"].mean()
# print(f"Середній вік студентів: {average_age}")

# Пункт 5
# Виведіть студентів, які отримали оцінку вище 80.
# mark_where_score_over_80 = students[students['Score'] > 80]
# print(mark_where_score_over_80)

# Пункт 6
# Змініть оцінку студента з іменем "Anna" на 95.
# refresh_mark = students.loc[students['Name'] == 'Анна', 'Score'] = 95
# print(f'Змінена оцінка для студента з іменем Анна на оцінку {refresh_mark}')

# Пункт 7
# Створіть Series з ім'ям "ages" на основі стовпця "Age" з DataFrame "students".
# ages = students['Age']
# print(ages)

# Пункт 8
# Знайдіть максимальний вік серед студентів.
# max_age = students['Age'].max()
# print(f'Максимальний вік студента: {max_age}')

# Пункт 9
# Видаліть рядок з іменем "John" з DataFrame "students".
# students = students[students['Name'] != 'Джон']
# print(students)

# Пункт 10
# students.to_csv('students.csv', index=False)
