from fastapi import FastAPI
from app.employee.employeeController import employeeRouter
from app.review.reviewController import reviewRouter

app = FastAPI()
app.include_router(employeeRouter)
app.include_router(reviewRouter)

