import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced To-Do List App")
        self.root.geometry("600x500")
        self.root.config(bg="#f0f8ff")
        self.tasks = []
        self.load_tasks()

        # Title and Description
        title_label = tk.Label(self.root, text="Welcome to Your To-Do List", font=("Arial", 16, "bold"), bg="#f0f8ff")
        title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        description_label = tk.Label(self.root, text="Add, Complete, and Manage Your Tasks Efficiently", font=("Arial", 10), bg="#f0f8ff")
        description_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        # Task Input Section
        self.task_entry = tk.Entry(self.root, width=40, font=("Arial", 12))
        self.task_entry.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        self.task_entry.insert(0, "Enter your task here...")

        self.add_button = tk.Button(self.root, text="Add Task", bg="#4caf50", fg="white", font=("Arial", 10), command=self.add_task)
        self.add_button.grid(row=2, column=2, padx=10, pady=10)

        # Task List Section
        self.task_listbox = tk.Listbox(self.root, width=60, height=15, font=("Arial", 10), bg="#ffffff", selectbackground="#cce7ff")
        self.task_listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        # Add Scrollbar to Listbox
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.task_listbox.yview)
        scrollbar.grid(row=3, column=3, sticky="ns", padx=5)
        self.task_listbox.config(yscrollcommand=scrollbar.set)

        # Task Actions Section
        self.complete_button = tk.Button(self.root, text="Mark Completed", bg="#2196f3", fg="white", font=("Arial", 10), command=self.mark_completed)
        self.complete_button.grid(row=4, column=0, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", bg="#f44336", fg="white", font=("Arial", 10), command=self.delete_task)
        self.delete_button.grid(row=4, column=1, pady=10)

        self.save_button = tk.Button(self.root, text="Save Tasks", bg="#ff9800", fg="white", font=("Arial", 10), command=self.save_tasks)
        self.save_button.grid(row=4, column=2, pady=10)

        self.display_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task and task != "Enter your task here...":
            self.tasks.append({"task": task, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.display_tasks()
        else:
            messagebox.showwarning("Input Error", "Task description cannot be empty.")

    def mark_completed(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = True
            self.display_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            if messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this task?"):
                index = selected[0]
                del self.tasks[index]
                self.display_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[Completed]" if task["completed"] else "[Pending]"
            color = "green" if task["completed"] else "black"
            self.task_listbox.insert(tk.END, f"{task['task']} {status}")
            self.task_listbox.itemconfig(tk.END, fg=color)

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
        messagebox.showinfo("Success", "Tasks saved successfully.")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
