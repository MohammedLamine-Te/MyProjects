import tkinter as tk
from tkinter import PhotoImage
#___________________Window information
root = tk.Tk()
root.title('MMC - Mahdi_Mohammed_Compiler')
root.geometry('1200x700')
root.resizable(False, True)  

#___________________Style Variables (Light Mode)
MainBgColor = "#F5F3EE"          # Main background (soft cream)
MenuColor   = "#E2D7C5"          # Menu + sidebar background (beige)
NurmalButtonBgColor = "#D7C3A3"  # Button normal background
ActivButtonBgColor  = "#3B2F2F"  # Button active background
CodeAreaText = "#2B2B2B"         # Code text color
FontFamily = "Consolas"

# Terminal Colors (modern dark style)
TerminalBg = "#2B2B2B"           # Dark background
TerminalFg = "#E8E8E8"           # Soft white text
TerminalBorder = "#C1BBAA"       # Subtle top border line

root.config(bg=MainBgColor)

#___________________Menu Bar
NavMenu = tk.Menu(root, bg=MenuColor, fg=CodeAreaText, activebackground=NurmalButtonBgColor, activeforeground="black")
root.config(menu=NavMenu)

FileMenu = tk.Menu(NavMenu, tearoff=False, bg=MenuColor, fg=CodeAreaText, activebackground=NurmalButtonBgColor)
NavMenu.add_cascade(label='File', menu=FileMenu, font=FontFamily)
FileMenu.add_command(label='New File', font=FontFamily)
FileMenu.add_command(label='Open File', font=FontFamily)
FileMenu.add_command(label='Open Folder', font=FontFamily)
FileMenu.add_separator()
FileMenu.add_command(label='Save', font=FontFamily)
FileMenu.add_command(label='Save as', font=FontFamily)
FileMenu.add_separator()
FileMenu.add_command(label='AutoSave', font=FontFamily)
FileMenu.add_separator()
FileMenu.add_command(label='Exit', font=FontFamily)

EditMenu = tk.Menu(NavMenu, tearoff=False, bg=MenuColor, fg=CodeAreaText, activebackground=NurmalButtonBgColor)
NavMenu.add_cascade(label='Edit', menu=EditMenu, font=FontFamily)
EditMenu.add_command(label='Undo', font=FontFamily)
EditMenu.add_command(label='Redo', font=FontFamily)
EditMenu.add_separator()
EditMenu.add_command(label='Copy', font=FontFamily)
EditMenu.add_command(label='Cut', font=FontFamily)
EditMenu.add_command(label='Paste', font=FontFamily)

HelpMenu = tk.Menu(NavMenu, tearoff=False, bg=MenuColor, fg=CodeAreaText, activebackground=NurmalButtonBgColor)
NavMenu.add_cascade(label='Help', menu=HelpMenu, font=FontFamily)
HelpMenu.add_command(label='Settings', font=FontFamily)
HelpMenu.add_command(label='Issues report', font=FontFamily)
HelpMenu.add_separator()
HelpMenu.add_command(label='About', font=FontFamily)

#___________________Top Toolbar 
toolbar = tk.Frame(root, bg=MenuColor, padx=5, pady=5, relief="flat", highlightthickness=0)
toolbar.pack(side='top', fill=tk.X)

RunImage = tk.PhotoImage(file='./Image/run.png')
RunButton = tk.Button(
    toolbar, 
    text='Run', 
    font=(FontFamily, 11, "bold"),
    image=RunImage, 
    compound='left', 
    fg="#3B2F2F",
    bg=NurmalButtonBgColor,
    activebackground=ActivButtonBgColor,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    bd=0,
    padx=10,
    pady=4
)
RunButton.pack(side=tk.RIGHT, padx=8, pady=4)

#___________________Main Zone (Body)
BodyFrame = tk.Frame(root, bg=MainBgColor)
BodyFrame.pack(fill="both", expand=True)

# Sidebar (reduced width)

SideMenuFrame = tk.Frame(BodyFrame, width=50, bg=MenuColor)
SideMenuFrame.pack(side='left', fill='y')
SideMenuFrame.pack_propagate(False)


############
open_menu = False

def posesionMenu():
    global open_menu
    if open_menu:
        SideMenuFrame.config(width=50)
        SideButton1.config(text="")
        SideButton2.config(text="")
        open_menu = False
    else:
        SideMenuFrame.config(width=220)
        SideButton1.config(text="  Mohammed Lamine", anchor="w", compound="left")
        SideButton2.config(text="  Ahmed Mahdi", anchor="w", compound="left")
        open_menu = True
    SideMenuFrame.update() 
toggle_btn = tk.Button(SideMenuFrame, text="☰", command=posesionMenu)
toggle_btn.pack(pady=16)

SideImage1 = tk.PhotoImage(file='./Image/file.png')
SideButton1 = tk.Button(SideMenuFrame, image=SideImage1,width=30, height=30, bg=MenuColor, relief="flat", cursor="hand2", activebackground=NurmalButtonBgColor,compound="left")
SideButton1.pack(pady=15)

SideImage2 = tk.PhotoImage(file='./Image/extention.png')
SideButton2 = tk.Button(SideMenuFrame, image=SideImage2,width=30, height=30, bg=MenuColor, relief="flat", cursor="hand2", activebackground=NurmalButtonBgColor,compound="left")
SideButton2.pack(pady=5)

# Code Area
CodeAreaFrame = tk.Frame(BodyFrame, bg=MainBgColor)
CodeAreaFrame.pack(fill="both", expand=True)

CodeAreya = tk.Text(
    CodeAreaFrame,
    height=15, width=140,
    font=(FontFamily, 12),
    bg="white",
    fg=CodeAreaText,
    insertbackground="black",
    relief="flat",
    undo=True
)
CodeAreya.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

#_________________Terminal Area
TerminalFrame = tk.Frame(root, bg=TerminalBg, highlightbackground=TerminalBorder, highlightthickness=1)
TerminalFrame.pack(side='bottom', fill='x')

# Top Bar with Control Buttons
ControlBar = tk.Frame(TerminalFrame, bg=TerminalBg)
ControlBar.pack(side='top', fill='x', pady=4, padx=8)

CloseMinimiseFrame = tk.Frame(TerminalFrame , height=20 ,width=1150 , bg= TerminalBg)
CloseMinimiseFrame.pack(side="top" ,fill='y')
CloseMinimiseFrame.pack_propagate(False)

CloseImage = PhotoImage(file='./Image/close.png')
CloseButton = tk.Button(CloseMinimiseFrame, image=CloseImage,bd=0 ,highlightthickness=0, bg=TerminalBg, activebackground=NurmalButtonBgColor, relief="flat", cursor="hand2")
CloseButton.pack(side='right', padx=10 , pady=0 )
CloseButton.pack_propagate(False)

MinimiseImage = PhotoImage(file='./Image/minimiser.png')
MinimiseButton = tk.Button(CloseMinimiseFrame, image=MinimiseImage , bd= 0 ,highlightthickness=0, bg=TerminalBg, activebackground=NurmalButtonBgColor, relief="flat", cursor="hand2")
MinimiseButton.pack(side='right', padx=0 , pady=0 )
MinimiseButton.pack_propagate(False)


# Terminal Text Box
TerminalBox = tk.Text(
    TerminalFrame,
    height=10,
    bg=TerminalBg,
    fg=TerminalFg,
    insertbackground=TerminalFg,
    relief="flat",
    font=(FontFamily, 11),
)
TerminalBox.pack(fill='x', expand=True, padx=10, pady=5)

# Remove spaces and lines

def Remove_lines_spaces():
    text1 = CodeAreya.get("1.0",tk.END)
    line = text1.split("\n")
    lines=[] 
    for i in line:
        if i.strip() != "":
            text2 = "".join(i.split())
            lines.append(text2)

    text3 = "\n".join(lines)
    CodeAreya.delete("1.0",tk.END)
    CodeAreya.insert(tk.END,text3)

RunButton.config(command=Remove_lines_spaces)


Button_Menu = tk.Menubutton(
    toolbar,
    text="▼",
    font=(FontFamily, 11, "bold"),
    bg=NurmalButtonBgColor,
    activebackground=ActivButtonBgColor,
    fg="#3B2F2F",
    relief="flat",
    cursor="hand2",
    bd=0
)

RunMenu = tk.Menu(
    Button_Menu,
    tearoff=False,
    bg=MenuColor,
    fg=CodeAreaText,
    activebackground=NurmalButtonBgColor,
    activeforeground="black",
    font=FontFamily
)

RunMenu.add_command(label="Run Normally", command=Remove_lines_spaces)
RunMenu.add_separator()
RunMenu.add_command(label="Run and Save", command=Remove_lines_spaces)

Button_Menu.config(menu=RunMenu)
Button_Menu.pack(side=tk.RIGHT, padx=8, pady=4)

root.mainloop()
