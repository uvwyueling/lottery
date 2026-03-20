import random
import tkinter as tk
from tkinter import messagebox

# ── 颜色变量（Claude 浅色风格） ────────────
BG        = "#faf9f7"   # 背景：暖米白
FG        = "#1a1a1a"   # 主文字：深炭
ACCENT    = "#d97706"   # 强调色：橙
BTN_DIS   = "#e8e5e0"   # 禁用按钮背景
FG_DIS    = "#aaaaaa"   # 禁用按钮文字
FG_SUB    = "#888888"   # 次要文字：灰

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

# ── UI 事件函数 ────────────────────────
def on_confirm():
    global total, remaining, drawn
    try:
        n = int(entry_total.get())
        if n < 1 or n > 100:
            messagebox.showerror("错误", "请输入 1 到 100 之间的整数")
            return
        total     = n
        remaining = list(range(1, total + 1))
        drawn     = []

        # 输入区变身：隐藏输入框和确认按钮，显示总题数文字
        entry_total.pack_forget()
        btn_confirm.pack_forget()
        label_total.config(text=f"总题数为 {total}")

        label_result.config(text="—")
        label_drawn.config(text="已抽到：（无）")

        # 激活抽取按钮
        btn_draw.config(state=tk.NORMAL, bg=ACCENT, fg="#faf9f7")

    except ValueError:
        messagebox.showerror("错误", "请输入有效的整数")

def on_draw():
    if not remaining:
        messagebox.showinfo("提示", "所有题目已抽完！")
        return
    draw()
    label_result.config(text=str(drawn[-1]))
    label_drawn.config(text="已抽到：" + "、".join(str(n) for n in drawn))

def on_reset():
    reset()

    # 恢复输入区
    entry_total.delete(0, tk.END)
    entry_total.pack(side=tk.LEFT, padx=10)
    btn_confirm.pack(side=tk.LEFT)
    label_total.config(text="请输入总题数：")

    label_result.config(text="—")
    label_drawn.config(text="已抽到：（无）")

    # 禁用抽取按钮
    btn_draw.config(state=tk.DISABLED, bg=BTN_DIS, fg=FG_DIS)

# ── 搭建舞台 ───────────────────────────
root = tk.Tk()
root.title("随机抽签")
root.geometry("500x440")
root.resizable(False, False)
root.configure(bg=BG)

# 输入区域
frame_input = tk.Frame(root, bg=BG, pady=24)
frame_input.pack()

label_total = tk.Label(
    frame_input, text="请输入总题数：",
    font=("Arial", 14), bg=BG, fg=FG
)
label_total.pack(side=tk.LEFT)

entry_total = tk.Entry(
    frame_input,
    font=("Arial", 14), width=6,
    bg="#ffffff", fg=FG, insertbackground=FG,
    relief=tk.FLAT, bd=4
)
entry_total.pack(side=tk.LEFT, padx=10)

btn_confirm = tk.Label(
    frame_input, text="确认",
    font=("Arial", 13), bg=ACCENT, fg="#faf9f7",
    padx=12, pady=5, cursor="hand2"
)
btn_confirm.pack(side=tk.LEFT)
btn_confirm.bind("<Button-1>", lambda e: on_confirm())

# 大数字显示（视觉中心）
label_result = tk.Label(
    root, text="—",
    font=("Arial", 100, "bold"),
    bg=BG, fg=FG
)
label_result.pack(pady=0)

# 随机抽取按钮
btn_draw = tk.Label(
    root, text="随机抽取",
    font=("Arial", 18, "bold"),
    width=12,
    bg=BTN_DIS, fg=FG_DIS,
    pady=16, cursor="hand2"
)
btn_draw.pack(pady=12)
btn_draw.bind("<Button-1>", lambda e: on_draw() if btn_draw["state"] != "disabled" else None)

# 已抽到记录
label_drawn = tk.Label(
    root, text="已抽到：（无）",
    font=("Arial", 13),
    bg=BG, fg=FG_SUB,
    wraplength=460
)
label_drawn.pack(pady=6)

# 清空记录按钮（藏在右下角）
btn_reset = tk.Button(
    root, text="清空记录",
    font=("Arial", 8),
    bg=BG, fg="#444444",
    relief=tk.FLAT,
    command=on_reset
)
btn_reset.place(relx=1.0, rely=1.0, x=-8, y=-8, anchor=tk.SE)

root.mainloop()



