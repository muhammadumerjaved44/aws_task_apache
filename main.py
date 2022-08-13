import uvicorn
from fastapi import FastAPI, FastAPI, Body, Request, File, UploadFile, HTTPException, status
from .tasks_api import create_task, get_tasks, get_task, update_task, delete_task


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "API is working"}


@app.post("/tasks/new")
def task_post(task_name):

    response, status = create_task(task_name)
    print('response------->', response)
    print('status------->', status)
    if status != 201:
        raise HTTPException(status_code=status, detail=response)
    return {"status": status, "detail": "Task created successfully", "data": response}



@app.get("/tasks")
def task_all():

    response, status = get_tasks()
    print('response------->', response)
    print('status------->', status)
    if status != 200:
        raise HTTPException(status_code=status, detail=response)
    return {"status": status, "detail": "All tasks reterieved", "data": response}


@app.get("/tasks/{id}")
def task_all(id):

    response, status = get_task(id)
    print('response------->', response)
    print('status------->', status)
    if status != 200:
        raise HTTPException(status_code=status, detail="Task not found")
    return {"status": status, "detail": "Single task reterieved", "data": response}


@app.put("/tasks/update")
def task_update(task_id, task_name):
    response, status = update_task(task_id, task_name)
    print('response------->', response)
    print('status------->', status)
    if status != 200:
        raise HTTPException(status_code=status, detail=response)
    return {"status": status, "detail": "Task updated successfully", "data": response}

@app.delete("/tasks/delete")
def task_delete(id):
    response, status = delete_task(id)
    if status != 200:
        raise HTTPException(status_code=status, detail=response)
    return {"status": status, "detail": "Task deleted successfully", "data": response}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)