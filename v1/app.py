import tkinter as tk
from tkinter import scrolledtext

# 确保已经导入了上面定义的 get_project_intro 函数
from v1.get_intro import get_project_intro  # 替换 your_script_name 为包含 get_project_intro 函数的脚本名

def fetch_intro():
    project = entry.get()
    intro = get_project_intro(project)
    text_area.configure(state='normal')
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, intro)
    text_area.configure(state='disabled')

# 创建主窗口
root = tk.Tk()
root.title("GitHub 项目介绍器")

# 创建输入框
entry_label = tk.Label(root, text="输入GitHub项目URL或名称:")
entry_label.pack()
entry = tk.Entry(root, width=50)
entry.pack()

# 创建按钮
fetch_button = tk.Button(root, text="获取项目介绍", command=fetch_intro)
fetch_button.pack()

# 创建滚动文本区域
text_area_label = tk.Label(root, text="项目介绍:")
text_area_label.pack()
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15, state='disabled')
text_area.pack()

# 运行主循环
root.mainloop()
