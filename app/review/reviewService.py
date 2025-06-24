from app.employee.employeeService import EmployeeService
from app.review.review import Review


class ReviewService:

    @staticmethod
    def getAllReviews(employee_id: int):
        temp=[]
        emp=EmployeeService.getEmployeeById(employee_id)
        for review in emp.review:
            temp.append(review)
        return temp

    @staticmethod
    def postReview(employee_id, review: Review):
        emp=EmployeeService.getEmployeeById(employee_id)
        if emp.review_id==None:
            emp.review_id=1
        temp=review
        temp.employee_id=employee_id
        temp.review_id=emp.review_id
        emp.review_id=emp.review_id+1
        emp.review.append(temp)
        return temp

    @staticmethod
    def deleteReview(employee_id, review_id: int):
        emp=EmployeeService.getEmployeeById(employee_id)
        print(emp.name)
        for temp in emp.review:
            if temp.review_id==review_id:
                emp.review.remove(temp)
                return temp
        return None








