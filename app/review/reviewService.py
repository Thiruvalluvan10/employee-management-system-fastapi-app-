from sqlmodel import Session, select
from sqlmodel.orm import session

from app.DB.db import engine
from app.employee.employee import Employee
from app.employee.employeeService import EmployeeService
from app.review.review import Review
from app.review.review_schema import ReviewIn

class ReviewService:
    @staticmethod
    def getAllReviews(employee_id: int):
        with Session(engine) as session:
            statement = select(Review).where(Review.employee_id == employee_id)
            results = session.exec(statement)
            return results.all()

    @staticmethod
    def postReview(review_in: ReviewIn):
        review=Review(employee_id=review_in.employee_id,
                      description=review_in.description,
                      rating=review_in.rating,
                      isAnonymous=review_in.isAnonymous)
        with Session(engine) as session:
            session.add(review)
            session.commit()
            return review

    @staticmethod
    def deleteReview(review_id: int):
        with Session(engine) as session:
            review=session.get(Review, review_id)
            if review:
                session.delete(review)
                session.commit()
                return review
            return None







