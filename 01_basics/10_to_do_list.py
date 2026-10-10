"""10_to_do_list.py - A tiny to-do list that lives in memory."""

tasks = []


def add_task(title: str) -> None:
    tasks.append({"title": title, "done": False})
    print(f"Added: {title}")


def complete_task(number: int) -> None:
    """Mark a task done using its list number (starting at 1)."""
    if 1 <= number <= len(tasks):
        tasks[number - 1]["done"] = True
        print(f"Completed: {tasks[number - 1]['title']}")
    else:
        print("No task with that number.")


def show_tasks() -> None:
    print("\nYour tasks:")
    if not tasks:
        print("  (nothing yet)")
    for i, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"  {i}. [{mark}] {task['title']}")
    print()


if __name__ == "__main__":
    add_task("Learn variables")
    add_task("Practice loops")
    add_task("Build a project")
    complete_task(1)
    complete_task(9)
    show_tasks()
