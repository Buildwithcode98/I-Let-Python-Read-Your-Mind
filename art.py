import tkinter as tk

TEXT = "CODE IS NOT JUST LOGIC IT IS POETRY IN MOTION"
TYPE_SPEED = 80  # ms

root = tk.Tk()
root.title("Python Word Art")
root.geometry("900x400")
root.configure(bg="black")

# Allow ESC to close
root.bind("<Escape>", lambda e: root.destroy())

text_widget = tk.Text(
    root,
    font=("Helvetica", 48, "bold"),
    bg="black",
    fg="white",
    bd=0,
    wrap="word"
)
text_widget.pack(expand=True, padx=40, pady=40)

text_widget.tag_config("highlight", foreground="#00ffcc")

index = 0

def type_text():
    global index
    if index < len(TEXT):
        text_widget.insert("end", TEXT[index])

        # Remove old highlight
        text_widget.tag_remove("highlight", "1.0", "end")

        content = text_widget.get("1.0", "end-1c")
        last_space = content.rfind(" ")

        if last_space != -1:
            start = f"1.{last_space + 1}"
            end = "end-1c"
            text_widget.tag_add("highlight", start, end)

        index += 1
        root.after(TYPE_SPEED, type_text)

type_text()
root.mainloop()




 