# ------------------- Libraries -----------------------
from Erstellung_CVF import AllData, read_all_data
from Diagram import FilePlot
from tkinter import ttk, BOTH
import tkinter as tk
from datetime import datetime


class ExpenseManagerGUI:
    """
    The class 'ExpenseManagerGUI' creates the graphical user interface (GUI)
    for managing expenses and income. It has two main tabs:
    - Tab 1: Data entry for income and expenses
    - Tab 2: Display various charts
    """

    def __init__(self):
        """
        Initializes the main window, notebook (tabs) and calls the forms.
        """
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.geometry("500x450")
        self.root.title("🧮 Ausgaben 🧮")
        self.notebook = ttk.Notebook(self.root)
        self.create_notebook_frames()
        self.create_form1()
        self.create_form2()
        self.root.mainloop()

    def create_notebook_frames(self):
        """
        Creates two tabs inside the notebook:
        - Tab 1: New entries
        - Tab 2: Show charts
        """
        self.frame1 = ttk.Frame(self.notebook)
        self.frame1.grid()
        self.frame2 = ttk.Frame(self.notebook)
        self.frame2.grid()

        self.notebook.add(self.frame1, text="Neuer Eintrag")
        self.notebook.add(self.frame2, text="Diagram anzeigen")
        self.notebook.pack(expand=True, fill=BOTH)

    def create_form1(self):
        """
        Creates the form to input expenses or income:
        - Amount
        - Type (Income / Expense)
        - Category
        - Date
        - Details
        + Save and Cancel buttons
        """

        def only_numeric(char):
            """
            Validates the amount input: only numeric entries with max two decimals allowed.
            Colors the field red if invalid.
            """
            if char == "":
                input_amount.configure(bg="white")
                return True
            try:
                float(char)
                if "." in char and len(char.split(".")[1]) > 2:
                    return False
                input_amount.configure(bg="white")
                return True
            except ValueError:
                input_amount.configure(bg="red")
                return False

        self.frame1.grid_columnconfigure(0, weight=1)
        input_frame = tk.Frame(self.frame1, borderwidth=5, relief="ridge", bg="lightgray")
        input_frame.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
        input_frame.grid_columnconfigure(1, weight=1)

        # Amount
        tk.Label(input_frame, text="Betrag(€): (0.00)", font=('Times New Roman', 12, 'bold'), bg="lightgray").grid(
            row=0, column=0, padx=2, pady=5, ipadx=5, ipady=5, sticky="w")
        input_amount = tk.Entry(input_frame, validate="key",
                                validatecommand=(input_frame.register(only_numeric), "%P"),
                                font=('Times New Roman', 12, 'bold'), bg="white")
        input_amount.grid(row=0, column=1, columnspan=3, padx=5, pady=5, ipadx=3, ipady=3, sticky="nsew")
        input_amount.insert(0, "")

        # Type
        tk.Label(input_frame, text="Type:", font=('Times New Roman', 12, 'bold'), bg="lightgray").grid(
            row=1, column=0, padx=2, pady=5, ipadx=5, ipady=5, sticky="w")
        selection_type = ttk.Combobox(input_frame, values=["Einnahme", "Ausgabe"],
                                      font=('Times New Roman', 12, 'bold'), state="readonly")
        selection_type.current(1)
        selection_type.grid(row=1, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

        # Category
        tk.Label(input_frame, text="Kategorie:", font=('Times New Roman', 12, 'bold'), bg="lightgray").grid(
            row=2, column=0, padx=5, pady=5, sticky="w")
        try:
            _, category_list = read_all_data()
        except Exception as e:
            category_list = []
            print("Fehler beim Laden der Kategorien:", e)

        selection_category = ttk.Combobox(input_frame, values=category_list,
                                          font=('Times New Roman', 12, 'bold'), state="readonly")
        if category_list:
            selection_category.current(0)
        else:
            selection_category.set("Keine Kategorien")
        selection_category.grid(row=2, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

        # Date
        tk.Label(input_frame, text="Datum (YYYY-MM-DD):", font=('Times New Roman', 12, 'bold'), bg="lightgray").grid(
            row=3, column=0, padx=2, pady=5, ipadx=5, ipady=5, sticky="w")
        input_date = tk.Entry(input_frame, font=('Times New Roman', 10, 'bold'), bg="white")
        input_date.grid(row=3, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")
        input_date.insert(0, datetime.today().strftime('%Y-%m-%d'))

        # Details
        tk.Label(input_frame, text="Details:", font=('Times New Roman', 12, 'bold'), bg="lightgray").grid(
            row=4, column=0, padx=10, pady=10, sticky="w")
        input_details = tk.Text(input_frame, width=20, height=5, font=('Times New Roman', 12, 'bold'))
        input_details.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5, sticky="ew")

        # Data handler instance
        data_handler = AllData(input_amount, selection_type, input_details, selection_category, input_date)

        # Buttons
        tk.Button(input_frame, text="Speichern", command=data_handler.speichern_data,
                  font=('Times New Roman', 12, 'bold')).grid(row=5, column=0, padx=5, pady=5,
                                                             ipadx=5, ipady=5, sticky="ew", columnspan=3)
        tk.Button(input_frame, text="Abbrechen", command=data_handler.leer_daten,
                  font=('Times New Roman', 12, 'bold')).grid(row=6, column=0, padx=5, pady=5,
                                                             ipadx=5, ipady=5, sticky="ew", columnspan=3)

    def create_form2(self):
        """
        Creates the form to select and display charts:
        - Chart type
        - Year
        - Button to plot
        """
        self.frame2.grid_rowconfigure(0, weight=1)
        self.frame2.grid_columnconfigure(0, weight=1)
        plot_frame = tk.Frame(self.frame2, borderwidth=5, relief="ridge", bg="lightgray")
        plot_frame.grid(row=0, column=0, sticky="nsew", pady=2, padx=2)
        plot_frame.grid_columnconfigure(0, weight=1)

        # Plot selection
        tk.Label(plot_frame, text="Plot auswählen:", font=('Times New Roman', 12, 'bold'), bg="lightgray").grid(
            row=0, column=0, columnspan=3, padx=2, pady=2, ipadx=5, ipady=5, sticky="ew")
        plot_selection = ttk.Combobox(plot_frame, values=[
            "Einnahmen und Ausgaben pro Monat (Balkendiagramm 📊)",
            "Verteilung der Einnahmen und Ausgaben (Liniendiagramm 📈)",
            "Einnahmen und Ausgaben pro Monat (Kreisdiagramm ◔)",
            "Kategorie der Ausgaben pro Monat (Balkendiagramm 📊)"],
            state="readonly", font=('Times New Roman', 11, 'bold'))
        plot_selection.current(0)
        plot_selection.grid(row=1, column=0, padx=2, ipadx=10, ipady=10, pady=2, sticky="ew", columnspan=3)

        # Year selection
        tk.Label(plot_frame, text="Jahr auswählen:", font=('Times New Roman', 12, 'bold'), bg="lightgray").grid(
            row=2, column=0, columnspan=3, padx=2, pady=2, ipadx=5, ipady=5, sticky="ew")
        try:
            all_data, _ = read_all_data()
        except Exception as e:
            all_data = []
            print("Fehler beim Laden der Daten:", e)

        year_list = sorted({entry[2][:4] for entry in all_data})
        year_selection = ttk.Combobox(plot_frame, values=year_list, state="readonly",
                                      font=('Times New Roman', 12, 'bold'))
        if year_list:
            year_selection.current(0)
        else:
            year_selection.set("Kein Jahr")
        year_selection.grid(row=3, column=0, padx=2, pady=5, ipady=5, ipadx=5, sticky="ew", columnspan=3)

        # Plot button
        plot_handler = FilePlot(plot_selection, year_selection)
        tk.Button(plot_frame, text="Plot anzeigen", command=plot_handler.show_plot,
                  font=('Times New Roman', 12, 'bold')).grid(row=4, column=0, columnspan=6,
                                                             padx=2, pady=50, ipadx=5, ipady=5, sticky="ew")


# Entry point of the program
if __name__ == "__main__":
    ExpenseManagerGUI()
