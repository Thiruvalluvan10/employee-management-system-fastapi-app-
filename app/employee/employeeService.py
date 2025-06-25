from typing import List, Optional
from sqlmodel import Session, select
from app.DB.db import engine
from app.employee.employee import Employee
from app.review.review import Review
from app.thread.data_process import DataProcess
from app.employee.employee_schema import EmployeeIn


class EmployeeService:

    @staticmethod
    def getAllEmployee():
        with Session(engine) as session:
            statement = select(Employee)
            results = session.exec(statement)
            return results.all()

    @staticmethod
    def getEmployeeById(id: int):
        with Session(engine) as session:
            return session.get(Employee, id)

    # @staticmethod
    # def insertAllEmployee(employees: List[EmployeeIn]) -> None:
    #     for employee_in in employees:
    #         EmployeeService.insertEmployee(employee_in)

    @staticmethod
    def insertEmployee(employee_in: EmployeeIn):
        reviews = []
        employee = Employee(
            name=employee_in.name,
            department=employee_in.department,
            salary=employee_in.salary,
            age=employee_in.age,
            gender=employee_in.gender,
            mail=employee_in.mail,
            phone=employee_in.phone,
            date_of_join=employee_in.date_of_join,
            reviews=reviews
        )
        DataProcess.threadDataProcess(employee)

        with Session(engine) as session:
            session.add(employee)
            session.commit()
            session.refresh(employee)
            return employee

    @staticmethod
    def deleteEmployee(id: int):
        with Session(engine) as session:
            employee = session.get(Employee, id)
            if employee:
                session.delete(employee)
                session.commit()
                return employee
            return None

    @staticmethod
    def updateEmployee(id: int, new_data: EmployeeIn): # -> Optional[Employee]:
        with Session(engine) as session:
            employee = session.get(Employee, id)
            if not employee:
                return None
            for field in ['name', 'department', 'salary', 'age', 'gender', 'mail', 'phone', 'date_of_join']:
                new_value = getattr(new_data, field)
                if new_value is not None:
                    setattr(employee, field, new_value)

            session.add(employee)
            session.commit()
            session.refresh(employee)
            return employee

