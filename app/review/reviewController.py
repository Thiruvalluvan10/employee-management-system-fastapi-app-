from fastapi import APIRouter

from app.employee.employeeService import EmployeeService
from app.review import reviewService
from app.review.review import Review
from app.review.reviewService import ReviewService

reviewRouter=APIRouter()
@reviewRouter.get("/review")
async def get_review(employee_id: int):
    return ReviewService.getAllReviews(employee_id)

@reviewRouter.post("/review")
async def post_review(employee_id:int,review:Review):
    return ReviewService.postReview(employee_id,review)

@reviewRouter.delete("/review/{review_id}")
async def delete_review(review_id:int,employee_id:int):
    emp=ReviewService.deleteReview(employee_id,review_id)
    return emp






