from app.employee.employee import Employee

class EmployeeService:
    EmployeeDB=[]
    primaryKey=1

    @staticmethod
    def getAllEmployee():
        return EmployeeService.EmployeeDB

    @staticmethod
    def getEmployeeById(id):
        index=1
        for employee in EmployeeService.EmployeeDB:
            if index == id:
                return employee
            index+=1
        return None

    @staticmethod
    def insertEmployee(employee):
        employee.id=EmployeeService.primaryKey
        EmployeeService.primaryKey+=1
        EmployeeService.EmployeeDB.append(employee)

    @staticmethod
    def deleteEmployee(id):
        employee = EmployeeService.getEmployeeById(id)
        if employee is not None:
            EmployeeService.EmployeeDB.remove(employee)
            return employee
        return None

    @staticmethod
    def updateEmployee(id,employee):
        for emp in EmployeeService.EmployeeDB:
            if emp.id == id:
                emp.name=employee.name if employee.name is not None else emp.name
                emp.department=employee.department if employee.department is not None else emp.department
                emp.salary=employee.salary if employee.salary is not None else emp.salary
                emp.age=employee.age if employee.age is not None else emp.age
                emp.mail=employee.mail if employee.mail is not None else emp.mail
                emp.phone=employee.phone if employee.phone is not None else emp.phone
                emp.date_of_join=employee.date_of_join if employee.date_of_join is not None else emp.date_of_join
                return emp
        return None