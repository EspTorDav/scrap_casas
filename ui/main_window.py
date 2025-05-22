import tkinter as tk
from tkinter import ttk
from scraper.models import PropertyListing

# Puedes definir aquí o importar tu función para crear la ventana
def create_main_window(properties_list):
    root = tk.Tk()
    root.title("Scraping de casas")

    frame = ttk.Frame(root)
    frame.pack(fill='both', expand=True)

    columns = ("description", "location", "price", "features", "link")
    tree = ttk.Treeview(frame, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=150)

    for prop in properties_list:
        tree.insert("", "end", values=(prop.description, prop.location, prop.price, prop.features, prop.link))

    tree.pack(fill='both', expand=True)

    root.mainloop()

if __name__ == "__main__":
    # Datos de ejemplo o importados de scraping
    properties = [
        PropertyListing("Nice flat downtown", "Madrid", "€1500", "2 bedrooms, 1 bath", "http://link1.com"),
        PropertyListing("Cozy house", "Barcelona", "€2000", "3 bedrooms, 2 baths", "http://link2.com"),
        PropertyListing("Modern apartment", "Valencia", "€1200", "1 bedroom, 1 bath", "http://link3.com"),
    ]

    create_main_window(properties)
