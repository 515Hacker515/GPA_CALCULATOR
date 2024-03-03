def count_GPA():

    grades = input("Please write your all grades: ")
    grades = grades.replace(" ", "")
    count = 0
    grade_dictionary = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}

    for i in grades:
        i = i.upper()
        if i in grade_dictionary.keys():
            count += grade_dictionary[i]
        if i not in grade_dictionary.keys():
            return "You wrote invalid grade, please rewrite it!"
    return count/len(grades)


while True:

    gpa = count_GPA()

    if type(gpa) == str:
        print(gpa)
        continue
    if gpa <= 2.2:
        print(gpa)
        print('Your GPA is low, please do your work better to raise it up')
    elif gpa >= 2.3 and gpa <= 3.4:
        print(gpa)
        print("Your GPA is normal, you are doing okay")
    elif gpa >= 3.5:
        print(gpa)
        print("Your GPA is so good, you are one of the best students in the school, good job!")
    finished_or_not = input('If you done with counting your GPA please write Done, if you want to continue write anything: ')
    if finished_or_not.lower() == 'done':
        break