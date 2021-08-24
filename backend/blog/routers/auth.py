from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from backend.blog import schemas, database
from backend.blog.repository import user as user_repo
router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query

