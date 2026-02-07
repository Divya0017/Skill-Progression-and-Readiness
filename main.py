from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return "Welcome to Skill Progression & Readiness"
