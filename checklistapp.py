import customtkinter as ctk
import os

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("System")

tasks = []
text_file = "Tasks from Check-List.txt"

def load_tasks():
    if os.path.exists(text_file):
        with open(text_file, "r") as f:
            for line in f:
                check_text = line.strip()
                if check_text:
                    add_task_to_ui(check_text)

def add_task_to_ui(check_text):
    task_frame = ctk.CTkFrame(master=disp_frame, fg_color="transparent")
    task_frame.pack(anchor="center")
    tasks.append(task_frame)

    chbx1 = ctk.CTkCheckBox(master=task_frame, text=f" {check_text}", font=("Helvetica", 20))
    chbx1.pack(side="left", padx=10, pady=10)
    
    del_button = ctk.CTkButton(master=task_frame, text="Delete", command=lambda: del_tasks(task_frame), height=20, width=50)
    del_button.pack(side="right", padx=10, pady=10)

def add_clicked():   
    check_text = user_input.get()

    if not check_text:
        user_input.configure(placeholder_text="Must fill this field.")
        return

    add_task_to_ui(check_text)
    total_task.configure(text=f"Total Tasks: {len(tasks)}")
    user_input.delete(0, "end")

    with open(text_file, "a") as f:
        f.write(f"{check_text}\n")

def del_tasks(task_frame):
    task_frame.destroy()
    tasks.remove(task_frame)
    total_task.configure(text=f"Total Tasks: {len(tasks)}")

def reset():
    for widget in disp_frame.winfo_children():
        widget.destroy()

    tasks.clear()
    total_task.configure(text=f"Total Tasks: {len(tasks)}")
    with open(text_file,"w") as f:
        pass

def clear():
    user_input.delete(0,"end")

root = ctk.CTk()
root.title("Check-List")
root.geometry("400x600")

upper_frame = ctk.CTkFrame(master=root,width=100,height=50,border_width=1,fg_color="transparent")
upper_frame.pack(padx=20,pady=20,fill="both", expand=True)

user_input = ctk.CTkEntry(master=upper_frame,placeholder_text="Add Tasks Here",width=300,height=50,font=("Arial", 20))
user_input.pack(pady=30)

button_frame = ctk.CTkFrame(master=upper_frame, fg_color="transparent")
button_frame.pack(pady=10, anchor="center")

add_button = ctk.CTkButton(master=button_frame,text="Add",command=add_clicked,height=30,width=70)
add_button.pack(side="left", padx=10)

reset_button = ctk.CTkButton(master=button_frame,text="Reset",command=reset,height=30,width=70)
reset_button.pack(side="left",padx=10)

clear_button = ctk.CTkButton(master=button_frame,text="Clear",command=clear,height=30,width=70)
clear_button.pack(side="left",padx=10)

total_task = ctk.CTkLabel(master=root,text=f"Total Tasks: 0",font=("Arial",20,"bold"))
total_task.pack(anchor="center")

disp_frame = ctk.CTkScrollableFrame(master=root, width=300, height=300, border_width=2, fg_color="#2a2c2e", orientation="vertical")
disp_frame.pack(padx=20,pady=20, fill="both", expand=True)

load_tasks()

root.mainloop()
