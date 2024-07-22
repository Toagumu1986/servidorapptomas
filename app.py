from fastapi import FastAPI 

from starlette.staticfiles import CORSMiddleware

from routes.rutasAPI import rutas

app=FastAPI()

app.add_middleware
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

app.include_router(rutas)
