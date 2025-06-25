from pydantic import BaseModel
from typing import Optional, List

from app.review.review_schema import ReviewIn


class EmployeeIn(BaseModel):
    name: Optional[str]
    department: Optional[str]
    salary: Optional[float]
    age: Optional[int]
    gender: Optional[str]
    mail: Optional[str]
    phone: Optional[str]
    date_of_join: Optional[str]
    reviews: Optional[List[ReviewIn]] = []
