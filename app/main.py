from fastapi import FastAPI

from app.DB.db import init_db
from app.employee.employeeController import employeeRouter
from app.review.reviewController import reviewRouter
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(employeeRouter)
app.include_router(reviewRouter)

