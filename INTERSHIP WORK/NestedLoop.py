noOfStudent = int(input("Enter No. Of Students : "))

for i in range(noOfStudent):
    #print(i)
    subjectNameArray = []
    markArray = []
    averageMark = 0
    studentName = input("Enter Student Name : ")
    noOfSubject = int(input("Enter No. Of Subject : "))
    for j in range(noOfSubject):
        #print(j)
        subjectName = input("Enter Subject Name : ")
        mark = int(input("Enter Mark : "))
        subjectNameArray.append(subjectName)
        markArray.append(mark)
        averageMark = averageMark+mark
        #print(subjectName,mark)
    print(studentName,subjectNameArray,markArray,averageMark,averageMark/noOfSubject,(averageMark/(noOfSubject*100))*100)
    subjectNameArray.reverse()
    markArray.reverse()
    print(studentName,subjectNameArray,markArray)
    markArray.clear()
    print(studentName,subjectNameArray,markArray)