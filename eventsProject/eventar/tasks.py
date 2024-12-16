from celery import Celery

app = Celery('eventar', broker='redis://localhost')

@app.task
def add(x, y):
    return x + y