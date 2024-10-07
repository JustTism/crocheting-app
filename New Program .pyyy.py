import tkinter as tk
from tkinter import messagebox, simpledialog
 
class CrochetApp:
     def __init__(self):
         self.label = None
         self.patterns = []
         self.frame = tk.Frame(self.root)

     def init(self, root: object):
         self.root = root
         self.root.title("Crochet Pattern Manager")

         self.frame.pack(pady=10)
 
         self.label = tk.Label(self.frame, text="Crochet Patterns")
         self.label.pack()
 
         self.pattern_listbox = tk.Listbox(self.frame, width=50)
         self.pattern_listbox.pack(pady=10)
 
         self.add_pattern_button = tk.Button(self.frame, text="Add Pattern", command=self.add_pattern)
         self.add_pattern_button.pack(side=tk.LEFT, padx=5)
 
         self.delete_pattern_button = tk.Button(self.frame, text="Delete Pattern", command=self.delete_pattern)
         self.delete_pattern_button.pack(side=tk.LEFT, padx=5)
 
         self.view_pattern_button = tk.Button(self.frame, text="View Pattern", command=self.view_pattern)
         self.view_pattern_button.pack(side=tk.LEFT, padx=5)
 
     def add_pattern(self):
         pattern_name = simpledialog.askstring("Input", "Enter pattern name:")
         if pattern_name:
             self.patterns.append(pattern_name)
             self.update_listbox()
 
     def delete_pattern(self):
         selected_pattern_index = self.pattern_listbox.curselection()
         if selected_pattern_index:
             del self.patterns[selected_pattern_index[0]]
             self.update_listbox()
         else:
             messagebox.showwarning("Warning", "Select a pattern to delete.")
 
     def view_pattern(self):
         selected_pattern_index = self.pattern_listbox.curselection()
         if selected_pattern_index:
             pattern_name = self.patterns[selected_pattern_index[0]]
             messagebox.showinfo("Pattern Details", f"Pattern Name: {pattern_name}")
         else:
             messagebox.showwarning("Warning", "Select a pattern to view.")
 
     def update_listbox(self):
         self.pattern_listbox.delete(0, tk.END)
         for pattern in self.patterns:
             self.pattern_listbox.insert(tk.END, pattern)
 
if __name__ == "main":
     root = tk.Tk()
     app = CrochetApp()
     root.mainloop()
