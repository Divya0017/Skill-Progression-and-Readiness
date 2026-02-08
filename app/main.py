from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main_page():
    return "Welcome to Skill Progression & Readiness"

@app.get("/health")
def health_check():
    return "OK"
