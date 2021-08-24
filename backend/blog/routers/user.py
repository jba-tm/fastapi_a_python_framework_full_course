from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends
from backend.blog import database, schemas
from backend.blog.repository import user as user_repo

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post('/', response_model=schemas.ShowUser, )
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user_repo.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user_repo.show(id, db)
