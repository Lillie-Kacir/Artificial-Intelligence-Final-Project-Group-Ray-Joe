#project

import tkinter as tk
from tkinter import ttk, messagebox

<<<<<<< Updated upstream
# ── Placeholder course list (swap these out later) ───────────────────────────
ALL_COURSES = [
    "Temp 1",
    "Temp 2",
    "Temp 3",
    "Temp 4",
    "Temp 5",
=======
#test

# ── Theme Colors ──────────────────────────────────────────────────────────────
BG       = "#f0f4f8"
DARK     = "#1a2332"
WHITE    = "#ffffff"
CARD_BG  = "#ffffff"
MID_DARK = "#2d3f55"
ACCENT   = "#3b82f6"
GREEN    = "#10b981"
PURPLE   = "#7c3aed"
AMBER    = "#f59e0b"
RED      = "#ef4444"
MUTED    = "#6b7280"
LIGHT_BG = "#f8fafc"

# ── Engineering Courses with Tags ─────────────────────────────────────────────
ENGINEERING_COURSES = [
    {
        "code": "ENGR 1001",
        "name": "Engineering Orientation",
        "tags": ["engineering", "design"],
    },
    {
        "code": "ENGR 1041",
        "name": "Foundations of Design 1",
        "tags": ["engineering", "design"],
    },
    {
        "code": "ENGR 1051",
        "name": "Foundations of Design 2",
        "tags": ["engineering", "design"],
    },
    {
        "code": "ECCS 1611",
        "name": "Programming 1",
        "tags": ["programming", "software"],
    },
    {
        "code": "ECCS 1621",
        "name": "Programming 2",
        "tags": ["programming", "software"],
    },
    {
        "code": "ECCS 1721",
        "name": "Digital Logic",
        "tags": ["electrical", "hardware"],
    },
    {
        "code": "ECCS 2311",
        "name": "Electric Circuits",
        "tags": ["electrical"],
    },
    {
        "code": "ECCS 2331",
        "name": "Digital Signal Processing",
        "tags": ["electrical", "signal_processing"],
    },
    {
        "code": "ECCS 2341",
        "name": "Electronics",
        "tags": ["electrical", "hardware"],
    },
    {
        "code": "ECCS 2381",
        "name": "Maker Engineering",
        "tags": ["robotics", "design", "embedded"],
    },
    {
        "code": "ECCS 2671",
        "name": "Data Structures & Algorithms 1",
        "tags": ["programming", "software"],
    },
    {
        "code": "ECCS 3241",
        "name": "Embedded Hardware-Software",
        "tags": ["embedded", "hardware", "programming"],
    },
    {
        "code": "ECCS 3351",
        "name": "Embedded Real-Time App",
        "tags": ["embedded", "programming", "robotics"],
    },
    {
        "code": "ECCS 3411",
        "name": "Computer Security",
        "tags": ["security", "programming", "networking"],
    },
    {
        "code": "ECCS 3611",
        "name": "Computer Architecture",
        "tags": ["hardware", "electrical"],
    },
    {
        "code": "ECCS 3631",
        "name": "Networks & Data Communications",
        "tags": ["networking", "software"],
    },
    {
        "code": "ECCS 3661",
        "name": "Operating Systems",
        "tags": ["software", "programming"],
    },
     #spring courses
 {
        "code": "ECCS 1011",
        "name": "Python and Problem Solving",
        "tags": ["programming", "software"],
    },
    {
        "code": "ECCS 1101",
        "name": "Computer Science Orientation",
        "tags": ["software"],
    },
    {
        "code": "ECCS 1421",
        "name": "Net-Centric Computing",
        "tags": ["networking", "software"],
    },
    {
        "code": "ECCS 2011",
        "name": "Introduction to Data Science",
        "tags": ["data", "programming"],
    },
    {
        "code": "ECCS 2021",
        "name": "Machine Learning",
        "tags": ["ai", "data"],
    },
    {
        "code": "ECCS 2321",
        "name": "Signals and Systems",
        "tags": ["signal_processing", "electrical"],
    },
    {
        "code": "ECCS 2411",
        "name": "Software Design Patterns",
        "tags": ["software", "programming"],
    },
    {
        "code": "ECCS 2421",
        "name": "Software Engineering",
        "tags": ["software"],
    },
    {
        "code": "ECCS 2431",
        "name": "Mobile App Development",
        "tags": ["software", "programming"],
    },
    {
        "code": "ECCS 2441",
        "name": "Web Development",
        "tags": ["software", "programming"],
    },
    {
        "code": "ECCS 2451",
        "name": "Landscapes of Computer Science",
        "tags": ["software"],
    },
    {
        "code": "ECCS 2681",
        "name": "Data Structures & Algorithms 2",
        "tags": ["programming", "software"],
    },
    {
        "code": "ECCS 3101",
        "name": "Basic Electromagnetics",
        "tags": ["electrical"],
    },
    {
        "code": "ECCS 3111",
        "name": "Applied Electromagnetics",
        "tags": ["electrical"],
    },
    {
        "code": "ECCS 3121",
        "name": "Machines & Power Electronics",
        "tags": ["electrical", "power"],
    },
    {
        "code": "ECCS 3131",
        "name": "Signals & Systems",
        "tags": ["signal_processing", "electrical"],
    },
    {
        "code": "ECCS 3141",
        "name": "Control & Automation",
        "tags": ["controls", "electrical"],
    },
    {
        "code": "ECCS 3191",
        "name": "Communication Systems",
        "tags": ["signal_processing", "networking"],
    },
    {
        "code": "ECCS 3311",
        "name": "Digital Signal Processing",
        "tags": ["signal_processing"],
    },
    {
        "code": "ECCS 3331",
        "name": "Electronics",
        "tags": ["electrical", "hardware"],
    },
    {
        "code": "ECCS 3401",
        "name": "Machine Learning",
        "tags": ["ai", "data"],
    },
    {
        "code": "ECCS 3421",
        "name": "Software Development",
        "tags": ["software"],
    },
    {
        "code": "ECCS 3431",
        "name": "Theory of Computation",
        "tags": ["theory"],
    },
    {
        "code": "ECCS 3451",
        "name": "UI/UX Design",
        "tags": ["design", "software"],
    },
    {
        "code": "ECCS 3481",
        "name": "Databases",
        "tags": ["data", "software"],
    },
    {
        "code": "ECCS 3781",
        "name": "Project Development",
        "tags": ["project", "design"],
    },
    {
        "code": "ECCS 4111",
        "name": "Power Systems",
        "tags": ["power", "electrical"],
    },
    {
        "code": "ECCS 4121",
        "name": "Advanced Power",
        "tags": ["power"],
    },
    {
        "code": "ECCS 4141",
        "name": "Information Science",
        "tags": ["data"],
    },
    {
        "code": "ECCS 4161",
        "name": "Advanced Controls",
        "tags": ["controls"],
    },
    {
        "code": "ECCS 4191",
        "name": "System Design",
        "tags": ["design"],
    },
    {
        "code": "ECCS 4211",
        "name": "VLSI System Design",
        "tags": ["hardware"],
    },
    {
        "code": "ECCS 4221",
        "name": "Hardware Security",
        "tags": ["security", "hardware"],
    },
    {
        "code": "ECCS 4321",
        "name": "Advanced Network Security",
        "tags": ["security", "networking"],
    },
    {
        "code": "ECCS 4331",
        "name": "Photovoltaic System Design",
        "tags": ["power"],
    },
    {
        "code": "ECCS 4351",
        "name": "Smart Grid",
        "tags": ["power"],
    },
    {
        "code": "ECCS 4361",
        "name": "Digital Image Processing",
        "tags": ["signal_processing", "ai"],
    },
    {
        "code": "ECCS 4391",
        "name": "Engineering Economy",
        "tags": ["engineering"],
    },
    {
        "code": "ECCS 4411",
        "name": "Programming Languages",
        "tags": ["programming"],
    },
    {
        "code": "ECCS 4431",
        "name": "Theory of Computation",
        "tags": ["theory"],
    },
    {
        "code": "ECCS 4441",
        "name": "Ethical Hacking & Pen Testing",
        "tags": ["security"],
    },
    {
        "code": "ECCS 4451",
        "name": "Cryptocurrency & Blockchain",
        "tags": ["security", "data"],
    },
    {
        "code": "ECCS 4461",
        "name": "Artificial Intelligence",
        "tags": ["ai"],
    },
    {
        "code": "ECCS 4621",
        "name": "Deep Learning",
        "tags": ["ai", "data"],
    },
    {
        "code": "ECCS 4731",
        "name": "Capstone Seminar",
        "tags": ["project"],
    },
    {
        "code": "ECCS 4741",
        "name": "Wireless Sensor Networks",
        "tags": ["networking", "embedded"],
    },
>>>>>>> Stashed changes
]


class StudentTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Course Tracker")
        self.root.geometry("700x620")
        self.root.configure(bg="#f0f2f5")
        self.root.resizable(True, True)

        # Each entry: {"frame": Frame, "var": StringVar, "combo": Combobox, "btn": Button}
        self.course_rows = []

        self._build_ui()

    # ── UI Construction ───────────────────────────────────────────────────────

    def _build_ui(self):
        canvas = tk.Canvas(self.root, bg="#f0f2f5", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        self.inner = tk.Frame(canvas, bg="#f0f2f5")
        self.inner_id = canvas.create_window((0, 0), window=self.inner, anchor="nw")

        self.inner.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")),
        )
        canvas.bind(
            "<Configure>",
            lambda e: canvas.itemconfig(self.inner_id, width=e.width),
        )
        canvas.bind_all(
            "<MouseWheel>",
            lambda e: canvas.yview_scroll(-1 * (e.delta // 120), "units"),
        )

        self._build_header()
        self._build_name_card()
        self._build_courses_card()
        self._build_save_bar()

    def _card(self, title):
        wrapper = tk.Frame(self.inner, bg="#f0f2f5", pady=10, padx=20)
        wrapper.pack(fill="x")

        card = tk.Frame(
            wrapper, bg="white", bd=0, relief="flat",
            highlightbackground="#d1d5db", highlightthickness=1,
        )
        card.pack(fill="x")

        title_bar = tk.Frame(card, bg="#2c3e50", pady=10, padx=16)
        title_bar.pack(fill="x")
        tk.Label(
            title_bar, text=title, font=("Helvetica", 13, "bold"),
            fg="white", bg="#2c3e50",
        ).pack(anchor="w")

        body = tk.Frame(card, bg="white", padx=16, pady=14)
        body.pack(fill="x")
        return body

    def _build_header(self):
        header = tk.Frame(self.inner, bg="#2c3e50", pady=18)
        header.pack(fill="x")
        tk.Label(
            header,
            text="Student Course Tracker",
            font=("Helvetica", 20, "bold"),
            fg="white",
            bg="#2c3e50",
        ).pack()

    # ── Name Card ─────────────────────────────────────────────────────────────

    def _build_name_card(self):
        body = self._card("Student Name")

        tk.Label(
            body, text="Full Name:", font=("Helvetica", 11),
            bg="white", fg="#374151",
        ).grid(row=0, column=0, sticky="w", pady=(0, 6))

        self.name_var = tk.StringVar()
        ttk.Entry(
            body, textvariable=self.name_var, font=("Helvetica", 11), width=40,
        ).grid(row=1, column=0, sticky="ew")

        body.columnconfigure(0, weight=1)

    # ── Courses Card ──────────────────────────────────────────────────────────

    def _build_courses_card(self):
        body = self._card("Classes Already Taken")
        self.courses_body = body

        tk.Label(
            body,
            text="Select each course you have already completed:",
            font=("Helvetica", 11), bg="white", fg="#374151",
        ).pack(anchor="w", pady=(0, 10))

        self.courses_container = tk.Frame(body, bg="white")
        self.courses_container.pack(fill="x")

        ttk.Separator(body, orient="horizontal").pack(fill="x", pady=12)

        tk.Button(
            body,
            text="＋  Add Class",
            command=self._add_course_row,
            bg="#10b981", fg="white",
            font=("Helvetica", 10, "bold"),
            relief="flat", padx=14, pady=7, cursor="hand2",
            activebackground="#059669", activeforeground="white",
        ).pack(anchor="w")

        # Start with two rows
        self._add_course_row()
        self._add_course_row()

    # ── Save Bar ──────────────────────────────────────────────────────────────

    def _build_save_bar(self):
        bar = tk.Frame(self.inner, bg="#f0f2f5", pady=14, padx=20)
        bar.pack(fill="x")

        tk.Button(
            bar,
            text="💾  Save All",
            command=self._save_all,
            bg="#3498db", fg="white",
            font=("Helvetica", 12, "bold"),
            relief="flat", padx=24, pady=10, cursor="hand2",
            activebackground="#2980b9", activeforeground="white",
        ).pack(side="left")

        self.save_status = tk.Label(
            bar, text="", font=("Helvetica", 10, "italic"),
            bg="#f0f2f5", fg="#16a34a",
        )
        self.save_status.pack(side="left", padx=14)

    # ── Course Row Logic ──────────────────────────────────────────────────────

    def _add_course_row(self):
        row_index = len(self.course_rows) + 1

        row_frame = tk.Frame(self.courses_container, bg="white", pady=4)
        row_frame.pack(fill="x")

        tk.Label(
            row_frame,
            text=f"Course {row_index}:",
            font=("Helvetica", 10), bg="white", fg="#6b7280",
            width=10, anchor="w",
        ).pack(side="left")

        var = tk.StringVar(value="")
        combo = ttk.Combobox(
            row_frame, textvariable=var,
            state="readonly", font=("Helvetica", 10), width=28,
        )
        combo.pack(side="left", padx=(0, 10))

        rm_btn = tk.Button(
            row_frame, text="✕",
            bg="#ef4444", fg="white",
            font=("Helvetica", 9, "bold"),
            relief="flat", padx=6, pady=2, cursor="hand2",
            activebackground="#dc2626", activeforeground="white",
        )
        rm_btn.pack(side="left")

        row = {"frame": row_frame, "var": var, "combo": combo, "btn": rm_btn}
        self.course_rows.append(row)

        var.trace_add("write", lambda *_: self._on_selection_changed())
        rm_btn.config(command=lambda r=row: self._remove_row(r))

        self._refresh_all_combos()
        self._update_remove_buttons()

    def _remove_row(self, row):
        if len(self.course_rows) <= 1:
            return
        self.course_rows.remove(row)
        row["frame"].destroy()
        self._renumber_rows()
        self._refresh_all_combos()
        self._update_remove_buttons()

    def _renumber_rows(self):
        for i, row in enumerate(self.course_rows):
            label = row["frame"].winfo_children()[0]
            label.config(text=f"Course {i + 1}:")

    def _on_selection_changed(self):
        self._refresh_all_combos()

    def _refresh_all_combos(self):
        """
        Rebuild each combobox's option list so it only shows courses
        that haven't been chosen by a *different* row.
        """
        chosen = {row["var"].get() for row in self.course_rows if row["var"].get()}

        for row in self.course_rows:
            current = row["var"].get()
            taken_by_others = chosen - ({current} if current else set())
            available = [c for c in ALL_COURSES if c not in taken_by_others]

            row["combo"].config(values=available)

            if current and current not in available:
                row["var"].set("")

    def _update_remove_buttons(self):
        """Disable the remove button when only one row remains."""
        only_one = len(self.course_rows) == 1
        for row in self.course_rows:
            if only_one:
                row["btn"].config(state="disabled", bg="#9ca3af", cursor="arrow")
            else:
                row["btn"].config(state="normal", bg="#ef4444", cursor="hand2")

    # ── Save ──────────────────────────────────────────────────────────────────

    def _save_all(self):
        name = self.name_var.get().strip()
        if not name:
            messagebox.showwarning("Missing Name", "Please enter a student name before saving.")
            return

        selected_courses = [row["var"].get() for row in self.course_rows if row["var"].get()]
        if not selected_courses:
            messagebox.showwarning("No Courses", "Please select at least one course before saving.")
            return

        summary = (
            f"Saved successfully!\n\n"
            f"Student: {name}\n"
            f"Courses ({len(selected_courses)}): {', '.join(selected_courses)}"
        )
        messagebox.showinfo("Saved", summary)
        self.save_status.config(
            text=f"✔  Saved {name} · {len(selected_courses)} course(s)"
        )


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    root = tk.Tk()

    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("TCombobox", padding=4)
    style.configure("TEntry", padding=4)

    app = StudentTrackerApp(root)
    root.mainloop()
