from pydantic import BaseModel


class ReviewIn(BaseModel):
    employee_id: int
    description: str
    rating: float
    isAnonymous: bool