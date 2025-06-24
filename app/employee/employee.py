import decimal
from typing import Optional

from pydantic import BaseModel

from app.review.review import Review


class Employee(BaseModel):
  id: Optional[int] = None
  name: Optional[str] = None
  department: Optional[str] = None
  salary: Optional[float] = None
  age: Optional[int] = None
  gender: Optional[str] = None
  mail: Optional[str] = None
  phone: Optional[str] = None
  date_of_join: Optional[str] = None
  review_id: Optional[int] = None
  review: Optional[list[Review]]=None




