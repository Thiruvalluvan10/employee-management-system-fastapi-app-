from fastapi import APIRouter

from app.employee.employee_schema import ReviewIn
from app.review.reviewService import ReviewService

reviewRouter=APIRouter()
@reviewRouter.get("/review")
async def get_review(employee_id: int):
    return ReviewService.getAllReviews(employee_id)

@reviewRouter.post("/review")
async def post_review(review:ReviewIn):
    temp= ReviewService.postReview(review)
    return temp
    # return

@reviewRouter.delete("/review/{review_id}")
async def delete_review(review_id:int):
    emp=ReviewService.deleteReview(review_id)
    return emp






