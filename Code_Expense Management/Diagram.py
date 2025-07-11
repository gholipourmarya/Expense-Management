import matplotlib.pyplot as plt
from Erstellung_CVF import read_all_data

class FilePlot:
    """
    A class to create and display various financial plots
    based on income and expense data read from a CSV file.
    """

    def __init__(self, selected_plot_var, selected_year_var):
        """
        Initialize the FilePlot object.

        Parameters:
        selected_plot_var (tkinter variable): Tkinter variable storing the selected plot type.
        selected_year_var (tkinter variable): Tkinter variable storing the selected year.
        """
        self.all_ausgabe, self.kategorien = read_all_data()
        self.selected_plot_var = selected_plot_var
        self.selected_year_var = selected_year_var

    def show_plot(self):
        """
        Select and display the plot based on the selected plot type.
        """
        plot_type = self.selected_plot_var.get()
        if "Einnahmen und Ausgaben pro Monat (Balkendiagramm 📊)" in plot_type:
            self.show_balkendiagramm()
        elif "Verteilung der Einnahmen und Ausgaben (Liniendiagramm 📈)" in plot_type:
            self.show_liniendiagramm()
        elif "Einnahmen und Ausgaben pro Monat (Kreisdiagramm ◔)" in plot_type:
            self.show_kreisdiagramm()
        elif "Kategorie vom Ausgaben pro Monat (Balkendiagramm 📊)" in plot_type:
            self.show_liniendiagramm2()

    def show_balkendiagramm(self):
        """
        Displays a stacked bar chart of monthly income and expenses for the selected year.
        """
        allausgabe = self.all_ausgabe
        jahr = self.selected_year_var.get()
        einnahmen_monat = {}
        ausgaben_monat = {}

        for value in allausgabe:
            monat = value[2][:7]
            if value[2][:4] == jahr:
                if value[1] == "Einnahme":
                    einnahmen_monat[monat] = einnahmen_monat.get(monat, 0) + float(value[0])
                else:
                    ausgaben_monat[monat] = ausgaben_monat.get(monat, 0) + float(value[0])

        monate = sorted(set(einnahmen_monat.keys()).union(ausgaben_monat.keys()))
        einnahmen = [einnahmen_monat.get(monat, 0) for monat in monate]
        ausgaben = [ausgaben_monat.get(monat, 0) for monat in monate]

        plt.figure(figsize=(10, 6))
        plt.bar(monate, einnahmen, label='Einnahmen', color='green')
        plt.bar(monate, ausgaben, label='Ausgaben', color='red', bottom=einnahmen)
        plt.xlabel('Monat')
        plt.ylabel('Betrag (€)')
        plt.title(f'Einnahmen und Ausgaben pro Monat ({jahr})')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def show_kreisdiagramm(self):
        """
        Displays a pie chart showing the distribution of total income and expenses for the selected year.
        """
        allausgabe = self.all_ausgabe
        jahr = self.selected_year_var.get()
        sum_einnahmen = 0
        sum_ausgaben = 0

        for value in allausgabe:
            if value[2][:4] == jahr:
                if value[1] == "Einnahme":
                    sum_einnahmen += float(value[0])
                elif value[1] == "Ausgabe":
                    sum_ausgaben += float(value[0])

        daten = [sum_einnahmen, sum_ausgaben]
        kategorien = ['Einnahmen', 'Ausgaben']
        farben = ['green', 'red']

        plt.figure(figsize=(8, 6))
        plt.pie(daten, labels=kategorien, colors=farben, autopct='%1.1f%%', startangle=140)
        plt.title(f'Verteilung der Einnahmen und Ausgaben ({jahr})')
        plt.axis('equal')
        plt.show()

    def show_liniendiagramm(self):
        """
        Displays a line chart of monthly income and expenses for the selected year.
        """
        allausgabe = self.all_ausgabe
        jahr = self.selected_year_var.get()
        einnahmen_monat = {}
        ausgaben_monat = {}

        for value in allausgabe:
            monat = value[2][:7]
            if value[2][:4] == jahr:
                if value[1] == "Einnahme":
                    einnahmen_monat[monat] = einnahmen_monat.get(monat, 0) + float(value[0])
                else:
                    ausgaben_monat[monat] = ausgaben_monat.get(monat, 0) + float(value[0])

        monate = sorted(set(einnahmen_monat.keys()).union(ausgaben_monat.keys()))
        einnahmen = [einnahmen_monat.get(monat, 0) for monat in monate]
        ausgaben = [ausgaben_monat.get(monat, 0) for monat in monate]

        plt.figure(figsize=(10, 6))
        plt.plot(monate, einnahmen, label="Einnahmen (€)", color="green", marker="o")
        plt.plot(monate, ausgaben, label="Ausgaben (€)", color="red", marker="o")
        plt.title(f"Einnahmen und Ausgaben pro Jahr ({jahr})", fontsize=16)
        plt.xlabel("Monate", fontsize=12)
        plt.ylabel("Betrag (€)", fontsize=12)
        plt.legend()
        plt.grid(True)
        plt.show()

    def show_liniendiagramm2(self):
        """
        Displays a bar chart of expenses per category for the selected year.
        """
        allausgabe = self.all_ausgabe
        jahr = self.selected_year_var.get()

        kategorie_ausgaben = {}

        for value in allausgabe:
            if value[2][:4] == jahr and value[1] == "Ausgabe":
                kategorie = value[3]
                kategorie_ausgaben[kategorie] = kategorie_ausgaben.get(kategorie, 0) + float(value[0])

        kategorien = sorted(kategorie_ausgaben.keys())
        ausgaben = [kategorie_ausgaben[k] for k in kategorien]

        plt.figure(figsize=(10, 6))
        plt.bar(kategorien, ausgaben, label=f'Ausgaben ({jahr})', color='green')
        plt.xlabel('Kategorie')
        plt.ylabel('Betrag (€)')
        plt.title(f'Ausgaben pro Kategorie ({jahr})')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()
