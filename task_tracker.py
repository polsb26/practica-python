import sys
import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "status": "not_done"})
    save_tasks(tasks)
    print("Tarea agregada.")

def update_task(index, new_title):
    tasks = load_tasks()
    try:
        tasks[index - 1]['title'] = new_title
        save_tasks(tasks)
        print("Tarea actualizada.")
    except IndexError:
        print("Índice inválido.")

def delete_task(index):
    tasks = load_tasks()
    try:
        tasks.pop(index - 1)
        save_tasks(tasks)
        print("Tarea eliminada.")
    except IndexError:
        print("Índice inválido.")

def set_status(index, status):
    if status not in ["not_done", "in_progress", "done"]:
        print("Estado inválido. Usa: not_done, in_progress o done.")
        return
    tasks = load_tasks()
    try:
        tasks[index - 1]['status'] = status
        save_tasks(tasks)
        print("Estado actualizado.")
    except IndexError:
        print("Índice inválido.")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status and filter_status not in ["done", "not_done", "in_progress"]:
        print("Filtro inválido.")
        return
    for i, task in enumerate(tasks, 1):
        if not filter_status or task['status'] == filter_status:
            status_symbol = {
                "done": "✅",
                "not_done": "❌",
                "in_progress": "🔄"
            }[task['status']]
            print(f"{i}. {status_symbol} {task['title']}")

def show_help():
    print("""
Uso:
  python task.py add "tarea"
  python task.py update INDEX "nuevo texto"
  python task.py delete INDEX
  python task.py set_status INDEX [not_done|in_progress|done]
  python task.py list
  python task.py list [done|not_done|in_progress]
""")

def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) >= 3:
        add_task(sys.argv[2])
    elif command == "update" and len(sys.argv) >= 4:
        update_task(int(sys.argv[2]), sys.argv[3])
    elif command == "delete" and len(sys.argv) == 3:
        delete_task(int(sys.argv[2]))
    elif command == "set_status" and len(sys.argv) == 4:
        set_status(int(sys.argv[2]), sys.argv[3])
    elif command == "list":
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    else:
        show_help()

if __name__ == "__main__":
    main()
