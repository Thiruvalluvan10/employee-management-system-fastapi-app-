from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.employee.employee import Employee
class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    employee_id: Optional[int] = Field(default=None,foreign_key="employee.id")
    description: Optional[str] = None
    rating: Optional[float] = None
    isAnonymous: Optional[bool] = None

    employee: Optional["Employee"] = Relationship(back_populates="reviews")
