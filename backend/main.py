from fastapi import FastAPI

app = FastAPI()

__all__ = ('index',)


@app.get('/')
def index():
    return {
        'data': {
            'name': 'Stark'
        }
    }


@app.get('/about')
def about():
    return {
        'data': {
            'name': 'about page'
        }
    }
