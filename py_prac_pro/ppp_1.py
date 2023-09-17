# code that shows student's data of a class.
# expected data: total student of a class, name, roll, present or absent status, 
# total present, total absent, percentage of present and absent. 

# source of data
data = [
    {'name': 'Hans', 'status': 'present', 'roll': 3},
    {'name': 'Éléonore', 'status': 'absent', 'roll': 4},
    {'name': '景太郎', 'status': 'present', 'roll': 1},
    {'name': 'John', 'status': 'present', 'roll': 2}
    ]
# total student, total present and absent, percentage of present and absent
def attendence_percent(attendence_status, data):
    return (len(attendence_status) / len(data)) * 100
    
present_student, absent_student = [], []
# deviding present and absent student
for student in data:
    if student['status'] == 'present':
        present_student.append(student)
    elif student['status'] == 'absent':
        absent_student.append(student)

print(f"Total present student: {len(present_student)} ({round(attendence_percent(present_student, data))}% percent)")
print(f"Total absent student: {len(absent_student)} ({round(attendence_percent(absent_student, data))}% percent)")

# name, roll, present status
print("Present student's data:")
for student in present_student:
    print(f"Name: {student['name']}, Roll: {student['roll']}, Status: {student['status']}")
print("Absent student's data:")
for student in absent_student:
    print(f"Name: {student['name']}, Roll: {student['roll']}, Status: {student['status']}")
