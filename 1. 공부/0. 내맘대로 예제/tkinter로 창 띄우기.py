import tkinter as tk

def say_hello():
    label.config(text="안녕하세요!")

root = tk.Tk()
root.title("테스트 창")
root.geometry("300x150")  # 창 크기: 너비 x 높이

label = tk.Label(root, text="버튼을 눌러보세요")
label.pack(pady=10)

button = tk.Button(root, text="누르기", command=say_hello)
button.pack(pady=5)

root.mainloop()
