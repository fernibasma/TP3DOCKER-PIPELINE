tasks = ["task1", "task2"]

def get_tasks():
    return tasks

def add_task(task):
    tasks.append(task)
    return task

def delete_task(task):
    tasks.remove(task)