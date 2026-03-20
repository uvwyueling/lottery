import random
import tkinter as tk
from tkinter import messagebox

# ── 全局状态 ──────────────────────────
total = None
remaining = []        # 还没被抽到的数字
drawn = []            # 已经被抽到的数字

# ── 核心逻辑 ─────────────────────────-
def draw():
    pick_up = random.choice(remaining)
    drawn.append(pick_up)
    remaining.remove(pick_up)

def reset():
    global total, remaining, drawn
    total = None
    remaining = []
    drawn = []

# ── UI 事件函数（连接按钮和逻辑） ──────
def on_confirm():
    global total, remaining, drawn
    try:
        n = int(entry_total.get())
        if n < 1 or n > 100:
            messagebox.showerror("错误", "请输入 1 到 100 之间的整数")
            return
        total = n
        remaining = list(range(1, total + 1))
        drawn = []
        label_result.config(text="—")
        label_drawn.config(text="已抽到：（无）")
        btn_draw.config(state=tk.NORMAL)
    except ValueError:
        messagebox.showerror("错误", "请输入有效的整数")

def on_draw():
    if not remaining:
        messagebox.showinfo("提示", "所有题号已抽完。")
        return
    draw()
    label_result.config(text=str(drawn[-1]))
    label_drawn.config(text="已抽到：" + "、".join(str(n) for n in drawn))

def on_reset():
    reset()
    entry_total.delete(0, tk.END)
    label_result.config(text="—")
    label_drawn.config(text="已抽到：（无）")
    btn_draw.config(state=tk.DISABLED)


# ── 搭建舞台 ───────────────────────────
root = tk.Tk()
root.title("随机抽签")
root.geometry("500x420")
root.resizable(False, False)

# 输入区域
frame_input = tk.Frame(root, pady=20)
frame_input.pack()
tk.Label(frame_input, text="请输入总题数：", font=("Arial", 14)).pack(side=tk.LEFT)
entry_total = tk.Entry(frame_input, font=("Arial", 14), width=6)
entry_total.pack(side=tk.LEFT, padx=10)
tk.Button(frame_input, text="确认", font=("Arial", 14), command=on_confirm).pack(side=tk.LEFT)

# 大数字显示（视觉中心）
label_result = tk.Label(root, text="—", font=("Arial", 90, "bold"), fg="#333333")
label_result.pack(pady=5)

# 随机抽取按钮（大而显眼）
btn_draw = tk.Button(
    root, text="随机抽取", font=("Arial", 18, "bold"),
    width=12, height=2, bg="#4CAF50", fg="white",
    command=on_draw, state=tk.DISABLED
)
btn_draw.pack(pady=10)

# 已抽到记录
label_drawn = tk.Label(
    root, text="已抽到：（无）",
    font=("Arial", 11), fg="#888888", wraplength=460
)
label_drawn.pack(pady=5)

# 清空记录按钮（小、不显眼、藏在右下角）
btn_reset = tk.Button(
    root, text="清空记录", font=("Arial", 12),
    fg="#bbbbbb", relief=tk.FLAT, command=on_reset
)
btn_reset.place(relx=1.0, rely=1.0, x=-8, y=-8, anchor=tk.SE)

root.mainloop()




