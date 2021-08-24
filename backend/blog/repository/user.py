from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.blog import schemas, database, models, hashing


def create(request: schemas.User, db: Session = Depends(database.get_db)):
    user = models.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def show(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} is not available')
    return user
