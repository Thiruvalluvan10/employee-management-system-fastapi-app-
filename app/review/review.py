from typing import Optional

from pydantic import BaseModel


class Review(BaseModel):
    review_id: Optional[int] = None
    employee_id: Optional[int] = None
    description: Optional[str] = None
    rating: Optional[float] = None
    isAnonymous: Optional[bool] = None


