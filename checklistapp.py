import customtkinter as ctk

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("System")


cycle = 0
def add_clicked():   
    global cycle
    cycle += 1
    check_text = user_input.get() 
    chbx1 = ctk.CTkCheckBox(master=frame, text=f"{cycle}. " + check_text, font=("Bahnschrift SemiBold",20)).pack(pady=10)
    user_input.delete(0,"end") 

def reset():
    global cycle
    cycle = 0
    for widget in frame.winfo_children():
        widget.destroy()

def clear():
    user_input.delete(0,"end")

root = ctk.CTk()
root.title("Check-List")
root.geometry("400x500")

upper_frame = ctk.CTkFrame(master=root,width=100,height=50,border_width=2,fg_color="transparent")
upper_frame.pack(padx=20,pady=20,fill="both", expand=True)

user_input = ctk.CTkEntry(master=upper_frame,placeholder_text="Enter here",width=300,height=50,font=("Arial", 20))
user_input.pack(pady=30)

button_frame = ctk.CTkFrame(master=upper_frame, fg_color="transparent")
button_frame.pack(pady=10, anchor="center")

add_button = ctk.CTkButton(master=button_frame,text="Add",command=add_clicked,height=30,width=70)
add_button.pack(side="left", padx=10)

reset_button = ctk.CTkButton(master=button_frame,text="Reset",command=reset,height=30,width=70)
reset_button.pack(side="left",padx=10)

clear_button = ctk.CTkButton(master=button_frame,text="Clear",command=clear,height=30,width=70)
clear_button.pack(side="left",padx=10)

frame = ctk.CTkScrollableFrame(master=root, width=300, height=300, border_width=2, fg_color="#2a2c2e", orientation="vertical")
frame.pack(padx=20,pady=20, fill="both", expand=True)

root.mainloop()
