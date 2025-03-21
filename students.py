students = [
    {
        'first_name': 'irmak',
        'last_name': 'bicerbay',
        'index_number': 35451,
        'nationality': 'Turkish',
        'starting_date': '13.03.2025',
        'courses': ["Math", "OOP", "Polish", "İntro digi tech", "Telecommunications", "Marketing"]
    },
    {
        'first_name': 'kayra',
        'last_name': 'celikoglu',
        'index_number': 35357,
        'nationality': 'Turkish',
        'starting_date': '28.11.2025',
        'courses': ["Math", "Physics", "Programming", "History"]
    },
    {
        'first_name': 'kuzey',
        'last_name': 'kizilkaya',
        'index_number': 35450,
        'nationality': 'Turkish',
        'starting_date': '21.04.2025',
        'courses': ["Marketing", "Economics", "Business Law", "Statistics"]
    }
]
def add_student(first_name, last_name, index_number, nationality, starting_date, courses):
    new_student = {
        'first_name': first_name,
        'last_name': last_name,
        'index_number': index_number,
        'nationality': nationality,
        'starting_date': starting_date,
        'courses': courses
    }
    students.append(new_student)
    print(f"Student {first_name} {last_name} is added")
def display_students():
    for student in students:
        print(f"Name: {student['first_name']} {student['last_name']}, Index: {student['index_number']}")
