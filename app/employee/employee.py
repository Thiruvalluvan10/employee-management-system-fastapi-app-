from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship

if TYPE_CHECKING:
    from app.review.review import Review


class EmployeeBase(SQLModel):
    name: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[float] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    mail: Optional[str] = None
    phone: Optional[str] = None
    date_of_join: Optional[str] = None

class Employee(EmployeeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    reviews: List["Review"] = Relationship(back_populates="employee")
