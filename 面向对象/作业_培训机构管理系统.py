class Course:
    def __init__(self,name,price):
        self.name=name
        self.price=price


class Class:
    def __init__(self,name,campus):
        self.name=name
        self.__course={}
        self.__student={}
        self.__teacher={}
        self.__campus=campus
        campus.add_cls(self)

    def add_course(self,course):
        self.__course[course.name]=course

    def enroll(self,student):
        self.__student[student.name]=student
        self.__campus.balance+=self.charge()


    def charge(self):
        all_ch=0
        for c in self.__course.values():
            all_ch+=c.price
        return all_ch
    
    def all_student(self):
        student_list=[]
        for i in self.__student:
            student_list.append(i)
        print(student_list)

    def all_course(self):
        course_list=[]
        for i in self.__course:
            course_list.append(i)
        print(course_list)

    def add_teacher(self,teacher):
        self.__teacher[teacher.name]=teacher

    def get_all_price(self):
        total=self.all_price()
        print(f'{self.name}目前已招{len(self.__student)}人,收费{total}元')

    def all_price(self):
        all_p=0   
        number=len(self.__student)
        all_p=self.charge()*number
        
        return all_p
        
    def get_students(self):
        return list(self.__student.keys())


class Student:
    def __init__(self,name):
        self.name=name
        
    def sign_up(self,cls):
        cls.enroll(self)
        print(f'{self.name}已经缴费{cls.charge()},恭喜{self.name}报名班级{cls.name}')

    


class Teacher:
    def __init__(self,name,cls):
        self.name=name
        self.cls=cls
        cls.add_teacher(self)


    

class Campus:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.__cls={}
        self.__staff={}

    def add_cls(self,cls):
        self.__cls[cls.name]=cls

    def add_staff(self,staff):
        self.__staff[staff.name]=staff

    

    def __all_balance(self):
        all_b=self.balance
        for cls_ in self.__cls.values():
            all_b+=cls_.all_price()
        print(f'{self.name}的账户余额为{all_b}')

    def __all_staff(self):
        staff_list=[]
        for i in self.__staff:
            staff_list.append(i)
        print(f'{self.name}的员工有{staff_list}')

    def __all_cls(self):
        cls_list=[]
        for i in self.__cls:
            cls_list.append(i)
        print(f'{self.name}的班级有{cls_list}')

    def __all_student(self):
        student_list=[]
        for i in self.__cls.values():
            student_list.extend(i.get_students())
        print(f'{self.name}的学员有{student_list}')

    def get_all_student(self):
        self.__all_student()

    def get_all_cls(self):
        self.__all_cls()

    def get_all_balance(self):
        self.__all_balance()

    def get_all_staff(self):
        self.__all_staff()
 

class Staff:
    def __init__(self,name,campus):
        self.name=name
        self.campus=campus
        campus.add_staff(self)
    
    def statistic_student(self,campus0):
        campus0.get_all_student()

    def statistic_cls(self,campus0):
        campus0.get_all_cls()

    def statistic_staff(self,campus0):
        campus0.get_all_staff()
    
    def statistic_balance(self,campus0):
        campus0.get_all_balance()

    


campus1=Campus('东部校区',20000)
campus2=Campus('西部校区',30000)
course1=Course('语文',500)
course2=Course('数学',200)
course3=Course('英语',300)
class1=Class('火箭班',campus1)
class2=Class('超级班',campus1)
s1=Student('刘备')
s2=Student('关羽')
s3=Student('张飞')
st1=Staff('诸葛亮',campus1)
st2=Staff('庞统',campus2)
t1=Teacher('水镜先生',class1)

class1.add_course(course1)
class1.add_course(course2)
class2.add_course(course3)
s1.sign_up(class1)
s2.sign_up(class2)
s3.sign_up(class2)
class1.all_price()
class2.all_price()
class1.all_course()
class1.all_student()
class2.all_course()
class2.all_student()
st2.statistic_balance(campus1)
st2.statistic_cls(campus1)
st2.statistic_staff(campus1)
st2.statistic_student(campus1)

#红色 绿色 蓝色 红色  





        
        


    
        

    