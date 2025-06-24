from fastapi import APIRouter, HTTPException

from app.employee import employeeService
from app.employee.employeeService import EmployeeService
from app.employee.employee import Employee

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

@employeeRouter.post("/employee")
async def post(employee:Employee):
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    EmployeeService.insertEmployee(employee)
    return employee

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








