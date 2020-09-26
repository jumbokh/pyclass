class ElectiveCourses():
    def __init__(self, name):
        self.__name = name
        self.__course = []
        
    def get_name(self):
        return self.__name

    def addcounse(self, course):
        self.__course.append(course)

    def dropcourse(self, course):
        self.__course.remove(course)
    
    def getcourse(self):
        return self.__course
    
student = ElectiveCourses("陳元俊")
student.addcounse("機器學習")
student.addcounse("人工智慧")
student.addcounse("大數據")
student.addcounse("電子商務")
student.addcounse("物聯網")
student.addcounse("自動控制")
student.addcounse("Python程式設計")
student.dropcourse("物聯網")
student.dropcourse("電子商務")
print("本學期 {0} 同學的選修課程有：".format(student.get_name()))
print(student.getcourse())



    


