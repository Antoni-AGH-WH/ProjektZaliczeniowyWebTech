import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import students

app = FastAPI()

app.include_router(students.router, prefix="/students")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


#uvicorn main:app --reload
#cd "folder"