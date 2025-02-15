from fastapi import FastAPI, HTTPException
from src.agent import process_task
from pathlib import Path

app = FastAPI()
DATA_DIR = Path("/data")

@app.post("/run")
def run_task(task: str):
    try:
        response = process_task(task)
        return {"status": "success", "message": response}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
def read_file(path: str):
    file_path = DATA_DIR / path
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return file_path.read_text()
