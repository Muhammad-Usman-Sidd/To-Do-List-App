import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

class ToDoListGUI:
    def __init__(self, root):
        self.all_tasks = []
        self.completed_tasks = []
        self.urgent_tasks = []
        self.root = root

        #creating a frame to organize the widgets.
        self.frame = tk.Frame(root)
        self.frame.pack()

        #adding a label for our welcome message
        self.label = tk.Label(self.frame, text="Welcome to the To-Do List Application", font=("Arial", 14))
        self.label.pack(pady=10)
        # We'll change the color to something more appealing.
        self.root.configure(bg='light slate gray')
        self.frame.configure(bg='light slate gray')
        self.label.configure(bg='light slate gray', fg='black')

        #buttons for various actions.
        self.view_tasks_button = tk.Button(self.frame, text="View All Tasks", command=self.view_all_tasks, bg='lavender', fg='black')
        self.view_tasks_button.pack(pady=15, padx=10)
        self.view_urgent_button = tk.Button(self.frame, text="View Urgent Tasks", command=self.view_urgent_tasks, bg='lavender', fg='black')
        self.view_urgent_button.pack(pady=15, padx=10)
        self.view_completed_button = tk.Button(self.frame, text="View Completed Tasks", command=self.view_completed_tasks, bg='lavender', fg='black')
        self.view_completed_button.pack(pady=15, padx=10)
        self.add_task_button = tk.Button(self.frame, text="Add a Task", command=self.add_task, bg='lavender', fg='black')
        self.add_task_button.pack(pady=15, padx=10)
        self.add_urgent_task_button = tk.Button(self.frame, text="Add an Urgent Task", command=self.add_urgent_task, bg='lavender', fg='black')
        self.add_urgent_task_button.pack(pady=15, padx=10)
        self.remove_task_button = tk.Button(self.frame, text="Remove a Task", command=self.remove_task, bg='lavender', fg='black')
        self.remove_task_button.pack(pady=15, padx=10)
        self.complete_task_button = tk.Button(self.frame, text="Mark a Task as Completed", command=self.complete_task, bg='lavender', fg='black')
        self.complete_task_button.pack(pady=15, padx=10)
        self.quit_button = tk.Button(self.frame, text="Quit", command=root.quit, bg='lavender', fg='black')
        self.quit_button.pack(pady=15, padx=10)

    def view_all_tasks(self):
        if self.all_tasks:
            task_list_text = "\nHere's the list of your tasks:\n"
            for i, task in enumerate(self.all_tasks):
                task_list_text += f"{i + 1}: {task}\n"
            messagebox.showinfo("All Tasks", task_list_text)
        else:
            choice = messagebox.askquestion("No Tasks", "Seems like you don't have any tasks. Would you like to add some?")
            if choice.lower() == "yes":
                self.add_task()

    def view_urgent_tasks(self):
        if self.urgent_tasks:
            task_list_text = "\nHere's your urgent tasks:\n"
            for i, task in enumerate(self.urgent_tasks):
                task_list_text += f"{i + 1}: {task}\n"
            messagebox.showinfo("Urgent Tasks", task_list_text)
        else:
            choice = messagebox.askquestion("No Urgent Tasks", "You currently don't have any urgent tasks. Would you like to add some?")
            if choice.lower() == "yes":
                self.add_urgent_task()

    def view_completed_tasks(self):
        if self.completed_tasks:
            task_list_text = "\nHere's your completed tasks:\n"
            for i, task in enumerate(self.completed_tasks):
                task_list_text += f"{i + 1}: {task}\n"
            messagebox.showinfo("Completed Tasks", task_list_text)
        else:
            messagebox.showinfo("No Completed Tasks", "No completed tasks to show at the moment.")

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Please enter the task you'd like to add:")
        if task:
            if task.lower() in [t.lower() for t in self.all_tasks]:
                messagebox.showinfo("Task Already Added", "It seems you've already added this task.")
            else:
                self.all_tasks.append(task)

    def add_urgent_task(self):
        task = simpledialog.askstring("Add Urgent Task", "Please enter the urgent task you'd like to add:")
        if task:
            self.all_tasks.append(task)
            self.urgent_tasks.append(task)

    def remove_task(self):
        if self.all_tasks:
            task_list_text = "\nHere's your current task list:\n"
            for i, task in enumerate(self.all_tasks):
                task_list_text += f"{i + 1}: {task}\n"
            task_number = simpledialog.askinteger("Remove Task", task_list_text + "\nPlease enter the task number you want to remove:")
            if 1 <= task_number <= len(self.all_tasks):
                removed_task = self.all_tasks.pop(task_number - 1)
                messagebox.showinfo("Task Removed", f"Task #{task_number}: {removed_task} has been removed.")
            else:
                messagebox.showinfo("Invalid Task Number", "Please enter a valid task number.")
        else:
            choice = messagebox.askquestion("No Tasks", "It appears you don't have any tasks to remove. Would you like to add some?")
            if choice.lower() == "yes":
                self.add_task()

    def complete_task(self):
        if self.all_tasks:
            task_list_text = "\nHere's your task list:\n"
            for i, task in enumerate(self.all_tasks):
                task_list_text += f"{i + 1}: {task}\n"
            task_number = simpledialog.askinteger("Complete Task", task_list_text + "\nPlease enter the task number you want to mark as completed:")
            if 1 <= task_number <= len(self.all_tasks):
                completed_task = self.all_tasks.pop(task_number - 1)
                self.completed_tasks.append(completed_task)
                messagebox.showinfo("Task Completed", f"Task #{task_number}: {completed_task} has been marked as completed.")
            else:
                messagebox.showinfo("Invalid Task Number", "Please enter a valid task number.")
        else:
            choice = messagebox.askquestion("No Tasks", "It looks like you don't have any tasks to mark as completed. Would you like to add some?")
            if choice.lower() == "yes":
                self.add_task()

def main():
    root = tk.Tk()
    root.title("To-Do List Application")
    app = ToDoListGUI(root)
    root.geometry("600x500")
    root.resizable(width=False, height=False)
    root.mainloop()

if __name__ == "__main__":
    main()
