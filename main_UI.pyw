import customtkinter as ctk
from customtkinter import filedialog
import tkinter
import functions

#set basic appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#window
window = ctk.CTk()
window.title("Linked In Learning Notes Extraction Tool")
window.geometry("500x350")
window.eval('tk::PlaceWindow . center')

#variables
optionmenu_var = ctk.StringVar(value=".txt")
input_path = ""
output_path = ""

#######GUI widgets
#initialize custom font variable
custom_font = ctk.CTkFont(family="consolas", size=14)

#label for input path
input_label = ctk.CTkLabel(window, text="LIL Exported Notes:", font=custom_font)
input_label.place(x=80, y=60)

#input path selection button
input_button = ctk.CTkButton(window, text="select file", font=custom_font, command=functions.set_input)
input_button.place(x=270, y=60)

#label for output path
label_output = ctk.CTkLabel(window, text="Note Output Path:", font=custom_font)
label_output.place(x=80, y=100)

#output path selection button
output_button = ctk.CTkButton(window, text="select path", font=custom_font, command=functions.set_output)
output_button.place(x=270, y=100)

#option button label
label_format_prompt = ctk.CTkLabel(window, text="Output Extension:", font=custom_font)
label_format_prompt.place(x=80, y=155)

#combo box
combobox = ctk.CTkOptionMenu(window, values=[".txt",".md", ".docx"], font=ctk.CTkFont(family="consolas", size=12), variable=optionmenu_var, 
                             dropdown_font=ctk.CTkFont(family="consolas", size=12), anchor="center")
combobox.place(x=270, y=155)

# #radio button txt selection
# txt_selection = ctk.CTkRadioButton(window, text=".txt", font=ctk.CTkFont(family="consolas", size=12), variable=radio_var, value=1)
# txt_selection.place(x=230, y=160)

# #radio button md selection
# md_selection = ctk.CTkRadioButton(window, text=".md", font=ctk.CTkFont(family="consolas", size=12), variable=radio_var, value=2)
# md_selection.place(x=300, y=160)

# #radio button docx selection
# docx_selection = ctk.CTkRadioButton(window, text=".docx", font=ctk.CTkFont(family="consolas", size=12), variable=radio_var, value=3)
# docx_selection.place(x=370, y=160)

#extract button
extract_button = ctk.CTkButton(window, text="extract notes", font=custom_font, command = functions.extract_event)
extract_button.pack(pady=(220,50))

#run
window.mainloop()

