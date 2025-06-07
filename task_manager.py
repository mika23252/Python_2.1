class Task:
    def __init__(self, id, title, priority, status=False):
        self.id = id
        self.title = title
        self.priority = priority
        self.status = status

    def __str__(self):
        status_str = "Выполнено" if self.status else "Не выполнено"
        return f"[{self.id}] {self.title} | Приоритет: {self.priority} | Статус: {status_str}"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, priority):
        task = Task(self.next_id, title, priority)
        self.tasks.append(task)
        self.next_id += 1
        print(f"Задача добавлена: {task}")

    def list_tasks(self, tasks=None):
        if tasks is None:
            tasks = self.tasks
        if not tasks:
            print("Нет задач для отображения.")
            return
        for t in tasks:
            print(t)

    def delete_task(self, id):
        for t in self.tasks:
            if t.id == id:
                self.tasks.remove(t)
                print(f"Задача с ID {id} удалена.")
                return
        print(f"Задача с ID {id} не найдена.")

    def change_status(self, id):
        for t in self.tasks:
            if t.id == id:
                t.status = not t.status
                print(f"Статус задачи {id} изменен на {'Выполнено' if t.status else 'Не выполнено'}.")
                return
        print(f"Задача с ID {id} не найдена.")

    def filter_by_status(self, done=True):
        filtered = [t for t in self.tasks if t.status == done]
        self.list_tasks(filtered)

    def sort_by_priority(self):
        sorted_tasks = sorted(self.tasks, key=lambda x: x.priority, reverse=True)
        self.list_tasks(sorted_tasks)


def main():
    manager = TaskManager()
    menu = (
        "\nМеню:\n"
        "1. Добавить задачу\n"
        "2. Показать все задачи\n"
        "3. Удалить задачу по ID\n"
        "4. Изменить статус задачи\n"
        "5. Показать только выполненные задачи\n"
        "6. Показать только невыполненные задачи\n"
        "7. Отсортировать задачи по приоритету\n"
        "0. Выход\n"
    )
    while True:
        print(menu)
        choice = input("Выберите пункт: ")
        if choice == '1':
            title = input("Название задачи: ")
            try:
                pr = int(input("Приоритет (1-5): "))
                if pr < 1 or pr > 5:
                    raise ValueError
            except ValueError:
                print("Приоритет должен быть целым от 1 до 5.")
                continue
            manager.add_task(title, pr)
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            try:
                id = int(input("ID задачи для удаления: "))
            except ValueError:
                print("Неверный ID.")
                continue
            manager.delete_task(id)
        elif choice == '4':
            try:
                id = int(input("ID задачи для смены статуса: "))
            except ValueError:
                print("Неверный ID.")
                continue
            manager.change_status(id)
        elif choice == '5':
            print("Выполненные задачи:")
            manager.filter_by_status(done=True)
        elif choice == '6':
            print("Невыполненные задачи:")
            manager.filter_by_status(done=False)
        elif choice == '7':
            print("Задачи, отсортированные по приоритету (по убыванию):")
            manager.sort_by_priority()
        elif choice == '0':
            print("Выход. До свидания!")
            break
        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    main()
