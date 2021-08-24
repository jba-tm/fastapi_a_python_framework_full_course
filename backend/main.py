import uvicorn
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


app = FastAPI()

__all__ = ('app',)


@app.get('/blog')
def index(limit: int = 10, offset: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {
            'data': f'{limit} published blog list'
        }
    else:
        return {
            'data': f'{limit} blog list'
        }


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return {
        'data': id
    }


@app.get('/blog/{id}/comments')
def comments(id: int, limit):
    return {
        'data':
            {
                'comments':
                    {
                        '1', '2'
                    }
            }
    }


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is created {request.title}'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


