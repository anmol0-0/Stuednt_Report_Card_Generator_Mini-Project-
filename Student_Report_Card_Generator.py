def get_student_data():
    how = int(input('Enter number of students: '))
    student_list = []


    for i in range(how):
        name = input('Enter student name: ')
        score1 = int(input('Enter score1:'))
        score2 = int(input('Enter score2: '))
        score3 = int(input('Enter score3: '))

        students = {
            'name':name,
            'scores':[score1,score2,score3]
        }

        student_list.append(students)

    return student_list


def calculate_average(scores):
    total = 0 
    for i in scores:
        total += i
    return total / len(scores)

def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    else:
        return 'Fail'


def main():
    students = get_student_data()
    for student in students:
        avg = calculate_average(student['scores'])
        grade = get_grade(avg)

        student['average'] = avg
        student['grade'] = grade

    print('----- Report ------')

    for student in students:
        print(f'{student['name']}: Average = {student['average']:.2f}, Grade = {student['grade']}')


main()