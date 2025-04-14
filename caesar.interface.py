import tkinter as tk
from tkinter import scrolledtext

def decrypt_all(text):
    l, u, r = 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', []
    for s in range(1, 26):
        d = ''
        for c in text:
            if c in l:
                d += l[(l.index(c) - s) % 26]
            elif c in u:
                d += u[(u.index(c) - s) % 26]
            else:
                d += c
        r.append(f'Shift {s:2}: {d}')
    return '\n\n'.join(r)

def run():
    t = box.get()
    out.delete('1.0', tk.END)
    out.insert(tk.END, decrypt_all(t))

w = tk.Tk()
w.title("Caesar Decrypt")
w.geometry("600x500")
w.configure(bg="#1e1e2f")

tk.Label(w, text="Encrypted Text:", fg="white", bg="#1e1e2f", font=("Helvetica", 12)).pack(pady=5)
box = tk.Entry(w, width=60, font=("Courier", 12), bg="#2e2e3f", fg="white", insertbackground="white")
box.pack(pady=5)

tk.Button(w, text="Decrypt", command=run, font=("Helvetica", 11), bg="#007acc", fg="white", width=20).pack(pady=10)

out = scrolledtext.ScrolledText(w, width=70, height=20, font=("Courier", 10), bg="#121212", fg="#00ff99", insertbackground="white")
out.pack(pady=10)

w.mainloop()
