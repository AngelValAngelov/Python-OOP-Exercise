from classes_and_objects_exercise.to_do_list.project.task import Task


class Section:
    tasks = []

    def __init__(self, name: str):
        self.name = name

    def add_task(self, new_task: Task):
        if new_task in Section.tasks:
            return f"Task is already in the section {self.name}"
        Section.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        task_list_exist = [t for t in self.tasks if task_name == t.name]
        if task_list_exist:
            task_list_exist[0].completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        amount_of_removed_tasks = 0
        for task in self.tasks:
            if task.completed:
                amount_of_removed_tasks += 1
                Section.tasks.remove(task)
        return f"Cleared {amount_of_removed_tasks} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for task in Section.tasks:
            result += task.details() + "\n"

        return result

# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())
