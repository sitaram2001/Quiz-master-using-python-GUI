import tkinter as tk
from tkinter import messagebox
import json
import random

user = []

def play():    
    print("\n==========QUIZ START==========")
    score = 0
    
    with open(r"D:\python\Quiz_app\questions.json", 'r') as f:
        questions = json.load(f)

    for i in range(10):
        no_of_questions = len(questions)
        ch = random.randint(0, no_of_questions-1)
        current_question = questions[ch]

        question = f'\nQ{i+1} {current_question["question"]}\n'
        options = current_question["options"]
        answer = current_question["answer"].upper()  # Convert to uppercase for case-insensitive comparison

        user_answer = ask_question(question, options).upper()  # Convert to uppercase for case-insensitive comparison

        if user_answer == answer:
            print("\nYou are correct")
            score += 1
        else:
            print(f"\nYou are incorrect. Correct answer: {answer}")

        del questions[ch]

    print(f'\nFINAL SCORE: {score}')
    messagebox.showinfo("Quiz Result", f"FINAL SCORE: {score}")

def ask_question(question, options):
    answer = ""

    def set_answer(option):
        nonlocal answer
        answer = option.strip()  # Remove leading and trailing whitespaces
        submit_button.config(state=tk.NORMAL)  # Enable the submit button

    def submit_answer():
        window.destroy()

    window = tk.Toplevel()
    window.title("Quiz Question")
    window.attributes("-fullscreen", True)
    window.configure(bg="skyblue")

    # Create a custom title bar
    title_bar = tk.Frame(window, bg="gray")
    title_bar.pack(expand=1, fill="x")

    title_label = tk.Label(title_bar, text="Quiz Question", font=("Helvetica", 16), bg="gray", fg="white")
    title_label.pack(side=tk.LEFT, padx=10)

    # Window controls
    minimize_button = tk.Button(title_bar, text="_", command=window.iconify, relief=tk.FLAT, bg="gray", fg="white")
    minimize_button.pack(side=tk.RIGHT)

    maximize_button = tk.Button(title_bar, text="⭱", command=lambda: toggle_fullscreen(window), relief=tk.FLAT, bg="gray", fg="white")
    maximize_button.pack(side=tk.RIGHT)

    close_button = tk.Button(title_bar, text="✕", command=window.destroy, relief=tk.FLAT, bg="gray", fg="white")
    close_button.pack(side=tk.RIGHT)

    question_label = tk.Label(window, text=question, font=("Helvetica", 16), bg="skyblue", fg="white")
    question_label.pack(pady=10)

    for option in options:
        button = tk.Button(window, text=option, command=lambda opt=option: set_answer(opt), font=("Helvetica", 14), bg="lightgreen", fg="black")
        button.pack(pady=5)

    submit_button = tk.Button(window, text="Submit", command=submit_answer, state=tk.DISABLED, font=("Helvetica", 14), bg="orange", fg="white")
    submit_button.pack(pady=10)

    window.grab_set()
    window.wait_window()

    return answer

def toggle_fullscreen(window):
    state = not window.attributes("-fullscreen")
    window.attributes("-fullscreen", state)

def quiz_questions():
    if len(user) == 0:
        messagebox.showinfo("Error", "You must first log in before adding questions.")
    elif len(user) == 2:
        if user[1] == "ADMIN":
            add_question_window = tk.Toplevel()
            add_question_window.title("Add Questions")
            add_question_window.attributes("-fullscreen", True)
            add_question_window.configure(bg="lightcoral")

            # Create a custom title bar
            title_bar = tk.Frame(add_question_window, bg="gray")
            title_bar.pack(expand=1, fill="x")

            title_label = tk.Label(title_bar, text="Add Questions", font=("Helvetica", 16), bg="gray", fg="white")
            title_label.pack(side=tk.LEFT, padx=10)

            # Window controls
            minimize_button = tk.Button(title_bar, text="_", command=add_question_window.iconify, relief=tk.FLAT, bg="gray", fg="white")
            minimize_button.pack(side=tk.RIGHT)

            maximize_button = tk.Button(title_bar, text="⭱", command=lambda: toggle_fullscreen(add_question_window), relief=tk.FLAT, bg="gray", fg="white")
            maximize_button.pack(side=tk.RIGHT)

            close_button = tk.Button(title_bar, text="✕", command=add_question_window.destroy, relief=tk.FLAT, bg="gray", fg="white")
            close_button.pack(side=tk.RIGHT)

            label = tk.Label(add_question_window, text="Enter the question that you want to add:", font=("Helvetica", 16), bg="lightcoral", fg="white")
            label.pack(pady=10)

            ques_entry = tk.Entry(add_question_window, font=("Helvetica", 14))
            ques_entry.pack(pady=10)

            options_label = tk.Label(add_question_window, text="Enter the 4 options with character initials (A, B, C, D)", font=("Helvetica", 16), bg="lightcoral", fg="white")
            options_label.pack(pady=10)

            options_entries = []
            for i in range(4):
                entry = tk.Entry(add_question_window, font=("Helvetica", 14))
                entry.pack(pady=5)
                options_entries.append(entry)

            ans_label = tk.Label(add_question_window, text="Enter the answer:", font=("Helvetica", 16), bg="lightcoral", fg="white")
            ans_label.pack(pady=10)

            ans_entry = tk.Entry(add_question_window, font=("Helvetica", 14))
            ans_entry.pack(pady=10)

            def add_question():
                question = ques_entry.get()
                options = [entry.get() for entry in options_entries]
                answer = ans_entry.get().upper()

                if not question or not all(options) or not answer:
                    messagebox.showinfo("Error", "Please fill in all fields.")
                    return

                with open(r"D:\python\Quiz_app\questions.json", 'r+') as f:
                    questions = json.load(f)
                    dic = {"question": question, "options": options, "answer": answer}
                    questions.append(dic)
                    f.seek(0)
                    json.dump(questions, f)
                    f.truncate()
                    messagebox.showinfo("Success", "Question successfully added.")
                    add_question_window.destroy()

            add_button = tk.Button(add_question_window, text="Add Question", command=add_question, font=("Helvetica", 14), bg="orange", fg="white")
            add_button.pack(pady=10)

        else:
            messagebox.showinfo("Error", "You don't have access to adding questions. Only admins are allowed to add questions.")
def create_account():
    create_account_window = tk.Toplevel()
    create_account_window.title("Create Account")
    create_account_window.attributes("-fullscreen", True)
    create_account_window.configure(bg="lightblue")

    label = tk.Label(create_account_window, text="Enter your USERNAME:", font=("Helvetica", 16), bg="lightblue", fg="white")
    label.pack(pady=10)

    username_entry = tk.Entry(create_account_window, font=("Helvetica", 14))
    username_entry.pack(pady=10)

    label = tk.Label(create_account_window, text="Enter your PASSWORD:", font=("Helvetica", 16), bg="lightblue", fg="white")
    label.pack(pady=10)

    password_entry = tk.Entry(create_account_window, show="*", font=("Helvetica", 14))
    password_entry.pack(pady=10)

    def create_account_action():
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showinfo("Error", "Please enter both username and password.")
            return

        with open(r"D:\python\Quiz_app\user_accounts.json", 'r+') as user_accounts:
            users = json.load(user_accounts)
            if username in users.keys():
                messagebox.showinfo("Error", "An account with this username already exists.\nPlease enter the login panel.")
            else:
                users[username] = [password, "PLAYER"]
                user_accounts.seek(0)
                json.dump(users, user_accounts)
                user_accounts.truncate()
                messagebox.showinfo("Success", "Account created successfully!")
                create_account_window.destroy()

    create_button = tk.Button(create_account_window, text="Create Account", command=create_account_action, font=("Helvetica", 14), bg="orange", fg="white")
    create_button.pack(pady=10)

def login_account():
    login_account_window = tk.Toplevel()
    login_account_window.title("Login Panel")
    login_account_window.attributes("-fullscreen", True)
    login_account_window.configure(bg="lightgreen")

    label = tk.Label(login_account_window, text="USERNAME:", font=("Helvetica", 16), bg="lightgreen", fg="white")
    label.pack(pady=10)

    username_entry = tk.Entry(login_account_window, font=("Helvetica", 14))
    username_entry.pack(pady=10)

    label = tk.Label(login_account_window, text="PASSWORD:", font=("Helvetica", 16), bg="lightgreen", fg="white")
    label.pack(pady=10)

    password_entry = tk.Entry(login_account_window, show="*", font=("Helvetica", 14))
    password_entry.pack(pady=10)

    def login_action():
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showinfo("Error", "Please enter both username and password.")
            return

        with open(r"D:\python\Quiz_app\user_accounts.json", 'r') as user_accounts:
            users = json.load(user_accounts)

        if username not in users.keys():
            messagebox.showinfo("Error", "An account with that name doesn't exist.\nPlease create an account first.")
        elif username in users.keys():
            if users[username][0] != password:
                messagebox.showinfo("Error", "Your password is incorrect.\nPlease enter the correct password and try again.")
            elif users[username][0] == password:
                messagebox.showinfo("Success", "You have successfully logged in.")
                user.append(username)
                user.append(users[username][1])
                login_account_window.destroy()

    login_button = tk.Button(login_account_window, text="Login", command=login_action, font=("Helvetica", 14), bg="orange", fg="white")
    login_button.pack(pady=10)

def logout():
    global user
    if len(user) == 0:
        messagebox.showinfo("Error", "You are already logged out.")
    else:
        user = []
        messagebox.showinfo("Success", "You have been logged out successfully.")

def rules():
    messagebox.showinfo("Rules", '''
    ==========RULES==========
    1. Each round consists of 10 random questions. To answer, you must press A/B/C/D (case-insensitive).
    Your final score will be given at the end.
    2. Each question consists of 1 point. There's no negative point for wrong answers.
    3. You can create an account from ACCOUNT CREATION panel.
    4. You can login using the LOGIN PANEL. Currently, the program can only login and not do anything more.
    ''')

def about():
    messagebox.showinfo("About Us", '''
    ==========ABOUT US==========
    This project has been created by 
    Suma Sri
    Surendra Appala
    Sita Ram
    Varshini
    Priyanka
    As a mini project on Python  for our 5th Semester.
    ''')

if __name__ == "__main__":
    main_window = tk.Tk()
    main_window.title("Quiz Master")
    main_window.attributes("-fullscreen", True)
    main_window.configure(bg="purple")

    label = tk.Label(main_window, text="Welcome to Quiz Master!", bg="lightgray", font=("Helvetica", 20), fg="navy")
    label.pack(pady=10)

    play_button = tk.Button(main_window, text="Play Quiz", command=play, font=("Helvetica", 14), bg="green", fg="white")
    play_button.pack(pady=10)

    quiz_questions_button = tk.Button(main_window, text="Add Quiz Questions", command=quiz_questions, font=("Helvetica", 14), bg="green", fg="white")
    quiz_questions_button.pack(pady=10)

    create_account_button = tk.Button(main_window, text="Create an Account", command=create_account, font=("Helvetica", 14), bg="green", fg="white")
    create_account_button.pack(pady=10)

    login_button = tk.Button(main_window, text="Login Panel", command=login_account, font=("Helvetica", 14), bg="green", fg="white")
    login_button.pack(pady=10)

    logout_button = tk.Button(main_window, text="Logout Panel", command=logout, font=("Helvetica", 14), bg="green", fg="white")
    logout_button.pack(pady=10)

    rules_button = tk.Button(main_window, text="See Instructions", command=rules, font=("Helvetica", 14), bg="green", fg="white")
    rules_button.pack(pady=10)

    about_button = tk.Button(main_window, text="About Us", command=about, font=("Helvetica", 14), bg="green", fg="white")
    about_button.pack(pady=10)

    exit_button = tk.Button(main_window, text="Exit", command=main_window.destroy, font=("Helvetica", 14), bg="red", fg="white")
    exit_button.pack(pady=10)

    main_window.mainloop()
