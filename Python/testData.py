import random

teacherId = []
classNo = []
subjectId = []
studentId = []

def getId(types, num):
    postfix = str(random.randint(0, 99999)).zfill(5)
    if types == 'teacher':
        prefix = random.randint(1, 2)
        while (str(prefix) + postfix) in teacherId:
            postfix = str(random.randint(0, 99999)).zfill(5)
        teacherId.append(str(prefix) + postfix)
    elif types == 'student':
        prefix = random.randint(3, 9)
        while (str(prefix) + postfix) in studentId:
            postfix = str(random.randint(0, 99999)).zfill(5)
        studentId.append(str(prefix) + postfix)
    elif types == 'class':
        classNo.append(num)
        return str(num).zfill(6)
    else:
        prefix = random.randint(0, 9)
        while (str(prefix) + postfix) in subjectId:
            postfix = str(random.randint(0, 99999)).zfill(5)
        subjectId.append(str(prefix) + postfix)

    return str(prefix) + postfix

def name(types, num):
    name = "'test" + types.capitalize() + str(num).zfill(3) + "'"
    #for i in range(random.randint(2, 2)):
    #    name += chr(random.randint(ord('A'), ord('Z')))
    if types == 'class':
        random.shuffle(teacherId)
        name = teacherId.pop()
    return  name

def printInsert(types, num):
    other = ''
    if types == 'student':
        random.shuffle(classNo)
        other = ', ' + str(classNo[0]).zfill(6)
    print("INSERT INTO %s VALUES (%s, %s%s);" % (types.upper(), getId(types, num), name(types, num), other))

def main():
    for i in range(2):
        printInsert('teacher', i + 1)

    print('\t')

    for i in range(1):
        printInsert('class', i + 1)

    print('\t')

    for i in range(2):
        printInsert('subject', i + 1)

    print('\t')

    for i in range(5):
        printInsert('student', i + 1)

    print('\t')

    for i in range(5):
        printInsert('offered_in', i + 1)

    print('\t')

    for i in range(5):
        printInsert('teach_in', i + 1)

    print('\t')

    for i in range(5):
        printInsert('teach_for', i + 1)

if __name__=="__main__":
    main()
