from fastapi import FastAPI

app = FastAPI()

Students = {
    1 : {
        "name": "Maamoun"
        , "age": "23"
        , "tall": "164 cm"
    }
}

@app.get("/")
def index():
    return {"name": "Maamoun Haj Najeeb"}


@app.get("/student/{student_id}")
def get_student(student_id: int):
    return Students[student_id]
