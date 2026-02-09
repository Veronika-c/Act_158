import tkinter as tk
import pathways
from tkinter import scrolledtext
from student import Student

#Create student
s1 =Student()

#read data
pass_l, pass_a, pass_b, combo, basic_l, basic_a, basic_b = pathways.get_scores()

def on_submit():
    # 1. Get the text from the entry field
    user_input = name_entry.get()

def show_frame(frame):
    home_screen = create_home_screen(main_container)
    info_screen = create_info_screen(main_container)
    path1_screen = create_path1_screen(main_container)
    path2_screen = create_path2_screen(main_container)
    path4_screen = create_path4_screen(main_container)
    path3_screen = create_path3_screen(main_container)
    path5_screen = create_path5_screen(main_container)
    """Brings the specified frame to the front."""
    frame.tkraise()

def add_navigation(parent):
    """Adds a row of navigation buttons to a parent frame."""
    nav_container = tk.Frame(parent, bg="white", height=50)
    nav_container.pack(side="top", fill="x")

    # Navigation Buttons placed next to each other
    home_btn = tk.Button(nav_container, text="Home", 
                         command=lambda: show_frame(home_screen))
    home_btn.pack(side="left", padx=10, pady=5)

    info_btn = tk.Button(nav_container, text="Details", 
                             command=lambda: show_frame(info_screen))
    info_btn.pack(side="left", padx=10, pady=5)
    
    path1_btn = tk.Button(nav_container, text="Pathway 1", 
                            command=lambda: show_frame(path1_screen))
    path1_btn.pack(side="left", padx=10, pady=5)

    path2_btn = tk.Button(nav_container, text="Pathway 2", 
                            command=lambda: show_frame(path2_screen))
    path2_btn.pack(side="left", padx=10, pady=5)

    path3_btn = tk.Button(nav_container, text="Pathway 3", 
                            command=lambda: show_frame(path3_screen))
    path3_btn.pack(side="left", padx=10, pady=5)

    path4_btn = tk.Button(nav_container, text="Pathway 4", 
                            command=lambda: show_frame(path4_screen))
    path4_btn.pack(side="left", padx=10, pady=5)

    path5_btn = tk.Button(nav_container, text="Pathway 5", 
                            command=lambda: show_frame(path5_screen))
    path5_btn.pack(side="left", padx=10, pady=5)

def create_home_screen(container):
    frame = tk.Frame(container, bg="#FADDC0")
    frame.grid(row=0, column=0, sticky="nsew")
    
    # Add the navigation bar
    add_navigation(frame)

    label = tk.Label(frame, text="Act 158 to Graduate", font=("Times New Roman", 18), bg="#FADDC0")
    label.pack(pady=50)
    return frame

def create_info_screen(container):
    def on_submit():
        lit_score = lit_entry.get()
        s1.lit_score = int(lit_score)
        print(s1.lit_score)
        bio_score = bio_entry.get()
        s1.bio_score = int(bio_score)
        print(s1.bio_score)
        al_score = al_entry.get()
        s1.al_score = int(al_score)
        print(s1.al_score)
        s1.grade = 11
        
        s1.result1 = pathways.pathway1_result(s1.lit_score, s1.al_score, s1.bio_score, s1.grade, pass_l, pass_a, pass_b)
        global path1_screen
        path1_screen = create_path1_screen(main_container)
        
    frame = tk.Frame(container, bg="lightgrey")
    frame.grid(row=0, column=0, sticky="nsew")
    
    # Add the navigation bar
    add_navigation(frame)

    info_title = tk.Label(frame, text="Student Information", font=("Times New Roman", 18), bg="lightgrey")
    info_title.pack(anchor='w', padx=10, pady=5)
    #literature entry
    lit_entry = tk.Entry(frame)
    lit_label = tk.Label(frame, text="Literature Keystone Score:", font = ("Times New Roman", 9))
    lit_label.pack(anchor='w', padx=10, pady=5)
    lit_entry.pack(anchor='w', padx=10, pady=5)
    #alegbra entry
    al_entry = tk.Entry(frame)
    al_label = tk.Label(frame, text="Alegbra Keystone Score:" ,  font = ("Times New Roman", 9))

    al_label.pack(anchor='w', padx=10, pady=5)
    al_entry.pack(anchor='w', padx=10, pady=5)
    #Biology entry
    bio_entry = tk.Entry(frame)
    bio_label = tk.Label(frame, text="Biology Keystone Score:",  font = ("Times New Roman", 9))

    bio_label.pack(anchor='w', padx=10, pady=5)
    bio_entry.pack(anchor='w', padx=10, pady=5)
    #CTE entry
    cte_entry = tk.Entry(frame)
    cte_label = tk.Label(frame, text="Are you in a CTE class?",  font = ("Times New Roman", 9))

    cte_label.pack(anchor='w', padx=10, pady=5)
    cte_entry.pack(anchor='w', padx=10, pady=5)
    #Any AP entry
    ap_entry = tk.Entry(frame)
    ap_label = tk.Label(frame, text="Any AP course scores?",  font = ("Times New Roman", 9))

    ap_label.pack(anchor='w', padx=10, pady=5)
    ap_entry.pack(anchor='w', padx=10, pady=5)
    #SAT entry
    sat_entry = tk.Entry(frame)
    sat_label = tk.Label(frame, text="SAT scores?",  font = ("Times New Roman", 9))

    sat_label.pack(anchor='w', padx=10, pady=5)
    sat_entry.pack(anchor='w', padx=10, pady=5)

    submit_btn = tk.Button(frame, text="Submit", command=on_submit,  font = ("Times New Roman", 9))

    submit_btn.pack(pady=10)
    return frame

def create_path1_screen(container):
    frame = tk.Frame(container, bg="#FADDC0")
    frame.grid(row=0, column=0, sticky="nsew")
    
    # Add the navigation bar
    add_navigation(frame)

    path1_title = tk.Label(frame, text="Pathway 1", font=("Times New Roman", 18), bg="#FADDC0")
    path1_title.pack(pady=50)

    display_area = scrolledtext.ScrolledText(frame, width=50, height=15, wrap=tk.WORD)
    display_area.pack(padx=10, pady=10)
    path1_txt = ""
    for i in range(len(s1.result1)):
        path1_txt += s1.result1[i] +"\n"
        
    long_content = path1_txt
    display_area.insert(tk.INSERT, long_content)
    return frame

def create_path2_screen(container):
    frame = tk.Frame(container, bg="#FADDC0")
    frame.grid(row=0, column=0, sticky="nsew")
    
    # Add the navigation bar
    add_navigation(frame)

    path2_title = tk.Label(frame, text="Pathway 2", font=("Times New Roman", 18), bg="#FADDC0")
    path2_title.pack(pady=50)

    display_area_2 = scrolledtext.ScrolledText(frame, width=50, height=15, wrap=tk.WORD)
    display_area_2.pack(padx=10, pady=10)



    
    return frame

def create_path3_screen(container):
    frame = tk.Frame(container, bg="#FADDC0")
    frame.grid(row=0, column=0, sticky="nsew")
    
    # Add the navigation bar
    add_navigation(frame)

    path3_title = tk.Label(frame, text="Pathway 3", font=("Times New Roman", 18), bg="#FADDC0")
    path3_title.pack(pady=50)
    return frame

def create_path4_screen(container):
    frame = tk.Frame(container, bg="#FADDC0")
    frame.grid(row=0, column=0, sticky="nsew")
    
    # Add the navigation bar
    add_navigation(frame)

    path4_title = tk.Label(frame, text="Pathway 4", font=("Times New Roman", 18), bg="#FADDC0")
    path4_title.pack(pady=50)
    return frame

def create_path5_screen(container):
    frame = tk.Frame(container, bg="#FADDC0")
    frame.grid(row=0, column=0, sticky="nsew")
    
    # Add the navigation bar
    add_navigation(frame)

    path5_title = tk.Label(frame, text="Pathway 5", font=("Times New Roman", 18), bg="#FADDC0")
    path5_title.pack(pady=50)
    return frame
# --- Main Application Setup ---
root = tk.Tk()
root.title("Multi-Screen App with Nav")
root.geometry("800x800")

main_container = tk.Frame(root)
main_container.pack(fill="both", expand=True)

main_container.grid_rowconfigure(0, weight=1)
main_container.grid_columnconfigure(0, weight=1)

# Initialize all screens
home_screen = create_home_screen(main_container)
info_screen = create_info_screen(main_container)
path1_screen = create_path1_screen(main_container)
path2_screen = create_path2_screen(main_container)
path3_screen = create_path3_screen(main_container)
path4_screen = create_path4_screen(main_container)
path5_screen = create_path5_screen(main_container)
# Show initial frame
show_frame(home_screen)

root.mainloop()
