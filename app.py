import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from example1.main import routes_eg1
from example2.main import routes_eg2

app = FastAPI()

app.include_router(routes_eg1)
app.include_router(routes_eg2)

app.mount('/', StaticFiles(directory='static', html=True))

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')