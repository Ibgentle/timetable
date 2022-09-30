import tkinter as tk
import tkinter.font as tkFont



teamA = []
teamB = []

def add_TeamA():
    name = teamA_entry.get()
    teamA_listbox.insert(tk.END, name)
    teamA.append(name)
def add_TeamB():
    name = teamB_entry.get()
    teamB_listbox.insert(tk.END, name)
    teamB.append(name)


def delete_TeamA():
    name = teamA_listbox.get(tk.ACTIVE)
    teamA.remove(name)
    teamA_listbox.delete(tk.ACTIVE)
def delete_TeamB():
    name = teamB_listbox.get(tk.ACTIVE)
    teamB.remove(name)
    teamB_listbox.delete(tk.ACTIVE)


def swap_TeamA():
    # name = teamA_listbox.get(tk.ACTIVE)
    # teamB.append(name); teamA.remove(name)
    teamB_listbox.insert(tk.END, teamA_listbox.get(tk.ACTIVE))
    teamA_listbox.delete(tk.ACTIVE)
    

    
def swap_TeamB():
    # name = teamB_listbox.get(tk.ACTIVE)
    # teamB.append(name); teamA.remove(name)
    teamA_listbox.insert(tk.END, teamB_listbox.get(tk.ACTIVE))
    teamB_listbox.delete(tk.ACTIVE)


def generate():
    """Select index and name of each item in the list,
    create a label widget with text set to the name"""

    for i, name in enumerate(teamA):
        lbl_name = tk.Label(master=ttbl_view, text=name, fg="#3498DB", font=font_fam_Gabriola)
        lbl_name.grid(row=3+i, column=1, sticky="w") # Place each item one row below the previous
        # lbl_name.grid(row=4+i, column=2, sticky="w")
        # lbl_name.grid(row=3+i, column=3, sticky="w")
    lbl_separate = tk.Label(master=ttbl_view, text=" ", height=5)
    lbl_separate.grid(row=4+i, column=0, columnspan=6, sticky="ew")
        
    for j, name in enumerate(teamB):
        lbl_name = tk.Label(master=ttbl_view, text=name, fg="green", font=font_fam_Gabriola)
        lbl_name.grid(row=5+i+j, column=1, sticky="w") # Place each item one row below the previous
        # lbl_name.grid(row=3+i, column=2, sticky="w")
        # lbl_name.grid(row=4+i, column=3, sticky="w")
    


window =tk.Tk()
window.title("Timetable Generator")

font_bold = tkFont.Font(weight="bold")
font_fam_Gabriola = tkFont.Font(family="Gabriola", size=15)

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
window.resizable(width=False, height=False)


# Creates a frame that houses the timetable and action buttons
ttbl_view = tk.Frame(master=window, relief=tk.SUNKEN, bd=1)

# creates entry widgets for team member names
teamA_entry = tk.Entry(master=ttbl_view, width=20)
teamB_entry = tk.Entry(master=ttbl_view, width=20)

# Creates labels for the entry boxes of team member names
lbl_teamA_names = tk.Label(master=ttbl_view, text="Enter Team-A names: ")
lbl_teamB_names = tk.Label(master=ttbl_view, text="Enter Team-B names: ")

# Creates a frame that houses the "Generate" and "Save As" buttons
frm_buttons = tk.Frame(master=window, relief=tk.RAISED, bd=2)
btn_generate = tk.Button(master=frm_buttons, text="Generate", bd=5, command=generate)
btn_save = tk.Button(frm_buttons, text="Save As...", bd=5)

# Creates buttons for actions to be performed with team A member names
btn_add_teamA = tk.Button(master=ttbl_view, text="Add name", bd=2, command=add_TeamA)
btn_delete_teamA = tk.Button(master=ttbl_view, text="Delete name", bd=2, command=delete_TeamA)
btn_swap_teamA = tk.Button(master=ttbl_view, text="Swap name", bd=2, command=swap_TeamA)

# Creates buttons for actions to be performed with team B member names
btn_add_teamB = tk.Button(master=ttbl_view, text="Add name", bd=2, command=add_TeamB)
btn_delete_teamB = tk.Button(master=ttbl_view, text="Delete name", bd=2, command=delete_TeamB)
btn_swap_teamB = tk.Button(master=ttbl_view, text="Swap name", bd=2, command=swap_TeamB)


btn_generate.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)


btn_add_teamA.grid(row=0, column=2, sticky="w", padx=10)
btn_delete_teamA.grid(row=0, column=3, sticky="w", padx=10)
btn_swap_teamA.grid(row=0, column=4, sticky="w", padx=10)


btn_add_teamB.grid(row=1, column=2, sticky="w", padx=10)
btn_delete_teamB.grid(row=1, column=3, sticky="w", padx=10)
btn_swap_teamB.grid(row=1, column=4, sticky="w", padx=10)

# Place the widgets in the frames created
frm_buttons.grid(row=0, column=0, sticky="ns")
teamA_entry.grid(row=0, column=0, pady=10, padx=5, sticky="w")
teamB_entry.grid(row=1, column=0, pady=10, padx=5, sticky="w")
lbl_teamA_names.grid(row=0, column=0, pady=10, sticky="nw")
lbl_teamB_names.grid(row=1, column=0, pady=10, sticky="nw")
ttbl_view.grid(row=0, column=1, sticky="nsew")

weekdays = ["Monday", "Tuesday", "Wedneday", "Thurday", "Friday", "Saturday", "Sunday"]

for i in range(7):
    frm_day = tk.Frame(master=ttbl_view, relief = tk.SUNKEN, bd=1)
    frm_day.grid(row=2, column=i+1, sticky="w", padx=10, pady=10)
    day = tk.Label(master=frm_day, text=weekdays[i].upper(), font=font_bold)
    day.grid()


frm_toolbox = tk.Frame(master=ttbl_view, relief=tk.SUNKEN, bd=1)
lbl_toolbox = tk.Label(master=frm_toolbox, text="SHIFT", font=font_bold)
frm_toolbox.grid(row=2, column=0, sticky="w", padx=5, pady=10)
lbl_toolbox.grid()

#Create listboxes to view and select the names that have been entered
teamA_listbox = tk.Listbox(master=ttbl_view, activestyle='none', height=8, width=15)
teamB_listbox = tk.Listbox(master=ttbl_view, activestyle='none', height=8, width=15)


teamA_listbox.grid(row=0, column=5, sticky="w", pady=3)
teamB_listbox.grid(row=1, column=5, sticky="w", pady=5)


window.mainloop()

