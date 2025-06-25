
import queue
import threading
from app.employee.employee import Employee

#MQs
nameQueue = queue.Queue()
salaryQueue = queue.Queue()
mailQueue = queue.Queue()
phoneQueue = queue.Queue()
dateQueue = queue.Queue()
departmentQueue = queue.Queue()
genderQueue = queue.Queue()

class DataProcess:

    @staticmethod
    def nameProcess(str): #name
        l=str.split(' ')
        temp=''
        for i in l:
            temp=temp+i.capitalize()+" "
        temp=temp.strip()
        # return temp
        nameQueue.put(temp)


    @staticmethod   #department
    def departmentProcess(department):
        l=department.split(' ')
        temp=''
        for i in l:
            temp=temp+i.capitalize()+" "
        temp=temp.strip()
        # return temp
        departmentQueue.put(temp)

    @staticmethod
    def salaryProcess(salary):
        # return float(salary)
        salaryQueue.put(float(salary))

    @staticmethod
    def genderProcess(gender):
        gender=gender.upper().strip()
        # return gender
        genderQueue.put(gender)

    @staticmethod
    def mailProcess(mail):
        mail=mail.lower().strip()
        # return mail
        mailQueue.put(mail)

    @staticmethod
    def phoneProcess(phone):
        str=phone
        str=str[::-1]
        temp=''
        for i in str:
            if i.isdigit():
                temp=temp+i
        temp=temp[::-1]
        # return temp
        phoneQueue.put(temp)

    @staticmethod
    def dateProcess(date):
        str=date
        str.replace('/','-')
        l=str.split('-')
        temp=''
        if len(l[0])==4:
            temp=l[2]+'-'+l[1]+'-'+l[0]
        temp=temp.strip()
        # return temp
        dateQueue.put(temp)

    @staticmethod
    def employeeDataProcess(employee):
        employee.name=DataProcess.nameProcess(employee.name)
        employee.department=DataProcess.departmentProcess(employee.department)
        employee.salary=DataProcess.salaryProcess(employee.salary)
        employee.gender=DataProcess.genderProcess(employee.gender)
        employee.mail=DataProcess.mailProcess(employee.mail)
        employee.phone=DataProcess.phoneProcess(employee.phone)
        employee.date_of_join=DataProcess.dateProcess(employee.date_of_join)
        return employee

    @staticmethod
    def threadDataProcess(employee):
        t1=threading.Thread(target=DataProcess.nameProcess(employee.name,))
        t2=threading.Thread(target=DataProcess.salaryProcess(employee.salary))
        t3=threading.Thread(target=DataProcess.mailProcess(employee.mail))
        t4=threading.Thread(target=DataProcess.phoneProcess(employee.phone))
        t5=threading.Thread(target=DataProcess.dateProcess(employee.date_of_join))
        t6=threading.Thread(target=DataProcess.departmentProcess(employee.department))
        t7=threading.Thread(target=DataProcess.genderProcess(employee.gender))
        t7.start()
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        employee.name=nameQueue.get()
        employee.salary=salaryQueue.get()
        employee.mail=mailQueue.get()
        employee.phone=phoneQueue.get()
        employee.date_of_join=dateQueue.get()
        employee.department=departmentQueue.get()
        employee.gender=genderQueue.get()
        return employee













