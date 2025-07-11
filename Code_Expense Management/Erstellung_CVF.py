#-----------Importieren der Bibliotheken-------------------------------------------------------------------
import os.path  # Importiert das Modul zum Arbeiten mit Dateipfaden (z. B. Überprüfen, ob eine Datei existiert)
import csv  # Importiere das Modul csv, um mit CSV-Dateien zu arbeiten
import tkinter as tk  # Importiere das tkinter-Modul für die GUI-Erstellung
from tkinter import messagebox  # Importiere das messagebox-Modul für Fehlermeldungen
from datetime import datetime  # Importiere das Modul datetime für die Arbeit mit Datumswerten
data = "Ausgaben_File.csv"  # Der Dateiname der CSV-Datei mit den Ausgaben/Einnahmen

class AllData:
    """
    A class to handle user inputs, validate them, and store financial data
    (income/expenses) into a CSV file.
    """

    def __init__(self, input_betrag, auswahl_typ, input_details, auswahl_kategory, input_datum):
        """
        Initialize the AllData instance with GUI entry widgets.

        Parameters:
        input_betrag (tk.Entry): Entry widget for amount.
        auswahl_typ (tk.Combobox): Dropdown for selecting income or expense.
        input_details (tk.Text): Text widget for additional details.
        auswahl_kategory (tk.Combobox): Dropdown for selecting a category.
        input_datum (tk.Entry): Entry widget for the date.
        """
        self.all_ausgabe = []
        self.input_betrag = input_betrag
        self.auswahl_typ = auswahl_typ
        self.input_details = input_details
        self.auswahl_kategory = auswahl_kategory
        self.input_datum = input_datum

    def leer_daten(self):
        """
        Clears all input fields in the form and resets them to default values.
        """
        self.input_betrag.config(validate="none")
        self.input_betrag.delete(0, "end")
        self.auswahl_typ.current(1)
        self.input_details.delete('1.0', tk.END)
        self.auswahl_kategory.current(0)
        self.input_datum.delete(0, tk.END)
        self.input_datum.insert(0, datetime.today().strftime('%Y-%m-%d'))
        self.input_betrag.config(validate="key")

    def screiben_daten_csv(self):
        """
        Writes user-entered financial data to a CSV file.
        Creates the file with headers if it does not exist or is empty.
        """
        print_betrag = self.input_betrag.get()
        print_typ = self.auswahl_typ.get()
        print_datum = self.input_datum.get()
        print_kategory = self.auswahl_kategory.get()
        string_details = self.input_details.get("1.0", "end-1c").replace("\n", " ")
        if string_details == "":
            string_details = "None"

        if not os.path.exists(data) or os.path.getsize(data) == 0:
            with open(data, "a", newline='', encoding='utf-8') as f:
                writer_data = csv.writer(f)
                writer_data.writerow(["ohne Kategorie", "Gehalt", "Haushalt", "Lebensmittel", "Kleidung", "Mitte", "Gesundheit", "Sport"])
                writer_data.writerow(["Betrag", "Type", "Datum", "Kategory", "Details"])
                writer_data.writerow([print_betrag, print_typ, print_datum, print_kategory, string_details])
        else:
            with open(data, mode='a', newline='', encoding='utf-8') as f:
                writer_data = csv.writer(f)
                writer_data.writerow([print_betrag, print_typ, print_datum, print_kategory, string_details])

    def check_eingeben(self):
        """
        Validates user input fields, especially amount and date.
        Highlights fields and shows error dialogs if validation fails.

        Returns:
        bool: True if all inputs are valid, otherwise None.
        """
        betrag = self.input_betrag.get()
        datum = self.input_datum.get()
        try:
            if datum == "" and betrag == "":
                raise ValueError("Bitte Betrag und Datum eingeben!")
            elif betrag == "":
                raise ValueError("Bitte Betrag eingeben!")
            elif datum == "":
                raise ValueError("Bitte Datum eingeben!")

            datetime.strptime(datum, "%Y-%m-%d")
            self.input_betrag.config(bg="white")
            self.input_datum.config(bg="white")
            return True
        except ValueError as e:
            if "Betrag und Datum" in str(e):
                self.input_betrag.config(bg="red")
                self.input_datum.config(bg="red")
                messagebox.showerror("Fehler", str(e))
                self.input_betrag.focus_set()
            elif "Betrag" in str(e):
                self.input_betrag.config(bg="red")
                messagebox.showerror("Fehler", str(e))
                self.input_betrag.focus_set()
            elif "Datum" in str(e):
                self.input_datum.config(bg="red")
                messagebox.showerror("Fehler", str(e))
                self.input_datum.focus_set()
            else:
                self.input_datum.config(bg="red")
                messagebox.showerror("Fehler", "Ungültiges Datumsformat!\nDas richtige Format ist: YYYY-MM-DD")
                self.input_datum.focus_set()

    def speichern_data(self):
        """
        Saves the validated user input data to the CSV file.
        If the amount is zero, it clears the input fields without saving.
        """
        betrag_f = self.input_betrag.get()
        if betrag_f == "0" or betrag_f == "0.0":
            self.leer_daten()
        elif self.check_eingeben():
            self.screiben_daten_csv()
            self.leer_daten()


def read_all_data():
    """
    Reads all financial entries from the CSV file and returns them.

    Returns:
    tuple: A list of data rows and a list of category headers.
    """
    all_ausgabe = []
    with open(data, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        kategory = next(reader)
        next(reader)
        for i in reader:
            all_ausgabe.append(i)
    return all_ausgabe, kategory
