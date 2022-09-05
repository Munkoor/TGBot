from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from database import SessionLocal
from models import Category
from schemas import CategoryView


app = FastAPI()


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()


router = SQLAlchemyCRUDRouter(
    schema=CategoryView,
    create_schema=CategoryView,
    db_model=Category,
    db=get_db,
    prefix='categories',
    delete_all_route=False,
    delete_one_route=False,
    create_route=False,
    update_route=False
)
app.include_router(router)
