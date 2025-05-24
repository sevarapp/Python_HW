from datetime import datetime
import sys

# ------------------- Homework 1: ToDo List Application ------------------- #

class Task:
    def __init__(self, title, description, due_date, status="Incomplete"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"{self.title} | Due: {self.due_date} | Status: {self.status}\n{self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_all_tasks(self):
        return "\n\n".join(str(task) for task in self.tasks)

    def list_incomplete_tasks(self):
        return "\n\n".join(str(task) for task in self.tasks if task.status == "Incomplete")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return True
        return False

# ------------------- Homework 2: Simple Blog System ------------------- #

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = datetime.now()

    def edit(self, new_title, new_content):
        self.title = new_title
        self.content = new_content
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.title} by {self.author} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n{self.content}"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def delete_post(self, title):
        self.posts = [p for p in self.posts if p.title != title]

    def edit_post(self, title, new_title, new_content):
        for post in self.posts:
            if post.title == title:
                post.edit(new_title, new_content)
                return True
        return False

    def list_all_posts(self):
        return "\n\n".join(str(post) for post in self.posts)

    def posts_by_author(self, author):
        return "\n\n".join(str(post) for post in self.posts if post.author == author)

    def latest_posts(self, n=3):
        return "\n\n".join(str(post) for post in sorted(self.posts, key=lambda p: p.timestamp, reverse=True)[:n])

# ------------------- Homework 3: Simple Banking System ------------------- #

class Account:
    def __init__(self, acc_number, acc_holder, balance=0.0):
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def __str__(self):
        return f"Account No: {self.acc_number} | Holder: {self.acc_holder} | Balance: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if account.acc_number in self.accounts:
            raise ValueError("Account already exists.")
        self.accounts[account.acc_number] = account

    def get_account(self, acc_number):
        return self.accounts.get(acc_number)

    def deposit(self, acc_number, amount):
        acc = self.get_account(acc_number)
        if not acc:
            raise ValueError("Account not found.")
        acc.deposit(amount)

    def withdraw(self, acc_number, amount):
        acc = self.get_account(acc_number)
        if not acc:
            raise ValueError("Account not found.")
        acc.withdraw(amount)

    def transfer(self, from_acc, to_acc, amount):
        if from_acc == to_acc:
            raise ValueError("Cannot transfer to the same account.")
        self.withdraw(from_acc, amount)
        self.deposit(to_acc, amount)

    def display_account(self, acc_number):
        acc = self.get_account(acc_number)
        if not acc:
            raise ValueError("Account not found.")
        return str(acc)

# ------------------- Testing the Applications ------------------- #

def main():
    todo = ToDoList()
    blog = Blog()
    bank = Bank()

    # Sample data for testing
    print("\n=== Testing ToDo List ===")
    todo.add_task(Task("Study Python", "Finish class assignments", "2025-05-30"))
    todo.add_task(Task("Exercise", "Run 30 minutes", "2025-05-25"))
    todo.mark_task_complete("Study Python")
    print(todo.list_all_tasks())
    print("\nIncomplete Tasks:\n", todo.list_incomplete_tasks())

    print("\n=== Testing Blog System ===")
    blog.add_post(Post("My First Post", "Hello world!", "Alice"))
    blog.add_post(Post("Python Tips", "Use list comprehensions!", "Alice"))
    blog.add_post(Post("My Trip", "I visited NYC.", "Bob"))
    blog.edit_post("My Trip", "My NYC Trip", "Had fun in Times Square.")
    blog.delete_post("My First Post")
    print(blog.list_all_posts())
    print("\nPosts by Alice:\n", blog.posts_by_author("Alice"))
    print("\nLatest Posts:\n", blog.latest_posts())

    print("\n=== Testing Banking System ===")
    bank.add_account(Account("001", "John", 500))
    bank.add_account(Account("002", "Mary", 1000))
    bank.deposit("001", 200)
    try:
        bank.withdraw("002", 300)
        bank.transfer("001", "002", 100)
    except ValueError as e:
        print("Error:", e)

    print(bank.display_account("001"))
    print(bank.display_account("002"))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Fatal error:", e)
        sys.exit(1)

