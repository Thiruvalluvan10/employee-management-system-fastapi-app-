from fastapi import APIRouter, HTTPException

from app.employee.employeeService import EmployeeService
from app.employee.employee import Employee
from app.employee.employee_schema import EmployeeIn

employeeRouter = APIRouter()

@employeeRouter.get("/employee")
async def getAll():
    return EmployeeService.getAllEmployee()

@employeeRouter.get("/employee/{id}")
async def getById(id: int):
    employee=EmployeeService.getEmployeeById(id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

#
# @employeeRouter.post("/employee")
# async def postAll(employees:list[Employee]):
#     if employees is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     EmployeeService.insertAllEmployee(employees)
#     return employees



@employeeRouter.post("/employee")
async def post(employee: EmployeeIn):
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return EmployeeService.insertEmployee(employee)


@employeeRouter.delete("/employee/{id}")
async def delete(id: int):
    emp=EmployeeService.deleteEmployee(id)
    if emp is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp


@employeeRouter.patch("/employee/{id}")
async def update(id:int,employee:Employee):
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    emp=EmployeeService.updateEmployee(id,employee)
    return emp








