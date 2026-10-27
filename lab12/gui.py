# gui.py — Дополнительный графический интерфейс для поиска и просмотра книг

from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox
from logic import find_records, statistics
from storage import load_records


class BookAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Список книг для чтения (Вариант 2)")
        self.root.geometry("750x500")

        self.data_path = Path(__file__).resolve().parent / "data.json"
        try:
            self.records = load_records(self.data_path)
        except Exception as e:
            self.records = []
            messagebox.showwarning("Внимание", f"Не удалось загрузить data.json: {e}\nНачат пустой список.")

        # Верхняя панель: поиск
        top_frame = ttk.LabelFrame(root, text="Поиск по названию книги")
        top_frame.pack(fill=tk.X, padx=12, pady=8)

        self.search_var = tk.StringVar()
        ttk.Label(top_frame, text="Подстрока:").pack(side=tk.LEFT, padx=6, pady=6)
        self.search_entry = ttk.Entry(top_frame, textvariable=self.search_var, width=30)
        self.search_entry.pack(side=tk.LEFT, padx=6, pady=6)

        ttk.Button(top_frame, text="Найти", command=self.on_search).pack(side=tk.LEFT, padx=6, pady=6)
        ttk.Button(top_frame, text="Показать все", command=self.on_show_all).pack(side=tk.LEFT, padx=6, pady=6)

        # Центральная панель: таблица Treeview
        table_frame = ttk.Frame(root)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=6)

        columns = ("id", "title", "category", "amount", "status")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("title", text="Название книги")
        self.tree.heading("category", text="Жанр / Категория")
        self.tree.heading("amount", text="Страниц")
        self.tree.heading("status", text="Статус")

        self.tree.column("id", width=50, anchor=tk.CENTER)
        self.tree.column("title", width=300)
        self.tree.column("category", width=150)
        self.tree.column("amount", width=80, anchor=tk.CENTER)
        self.tree.column("status", width=120, anchor=tk.CENTER)

        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Нижняя панель: статус и статистика
        self.status_var = tk.StringVar()
        self.status_label = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(fill=tk.X, side=tk.BOTTOM, padx=12, pady=6)

        self.update_table(self.records)

    def update_table(self, items):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for r in sorted(items, key=lambda x: x["id"]):
            st = "Прочитана" if r["completed"] else "Не прочитана"
            self.tree.insert("", tk.END, values=(r["id"], r["title"], r["category"], f"{r['amount']} стр.", st))

        stats = statistics(self.records)
        self.status_var.set(
            f"Отображено: {len(items)} из {stats['total_count']} книг | "
            f"Прочитано: {stats['completed_count']} | Всего страниц: {stats['total_amount']}"
        )

    def on_search(self):
        query = self.search_var.get().strip()
        if not query:
            messagebox.showinfo("Поиск", "Поисковый запрос не должен быть пустым.")
            return

        found = find_records(self.records, query)
        self.update_table(found)
        if not found:
            messagebox.showinfo("Результат", f"По запросу '{query}' книги не найдены.")

    def on_show_all(self):
        self.search_var.set("")
        self.update_table(self.records)


def main():
    root = tk.Tk()
    app = BookAppGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
