#Pokemon Game
import tkinter as tk

pokemon_stats = {
    "Charmander": {"health": 100, "power": 80},
    "Bulbasaur": {"health": 100, "power": 75},
    "Squirtle": {"health": 100, "power": 70},
    "Pikachu": {"health": 100, "power": 90}
}

def display_stats(pokemon):
    if pokemon in pokemon_stats:
        health = pokemon_stats[pokemon]["health"]
        power = pokemon_stats[pokemon]["power"]
        result_label.config(text=f"{pokemon}: Health: {health}, Power: {power}")

def create_custom_pokemon():
    custom_window = tk.Toplevel(root)
    custom_window.title("Create Your Own Pokemon")

    # Create input fields for custom Pokemon attributes
    name_label = tk.Label(custom_window, text="Name:")
    name_label.grid(row=0, column=0)
    name_entry = tk.Entry(custom_window)
    name_entry.grid(row=0, column=1)

    type_label = tk.Label(custom_window, text="Type:")
    type_label.grid(row=1, column=0)
    type_entry = tk.Entry(custom_window)
    type_entry.grid(row=1, column=1)

    power_label = tk.Label(custom_window, text="Power:")
    power_label.grid(row=2, column=0)
    power_entry = tk.Entry(custom_window)
    power_entry.grid(row=2, column=1)

    # Function to create the custom Pokemon
    def create_pokemon():
        name = name_entry.get()
        pokemon_type = type_entry.get()
        power = power_entry.get()
        result_label.config(text=f"Created {name}, a {pokemon_type} type Pokemon with power level {power}!")
        display_stats(name)

    create_button = tk.Button(custom_window, text="Create", command=create_pokemon)
    create_button.grid(row=3, columnspan=2)

root = tk.Tk()
root.title("Welcome to The Pokemon Game")
root.geometry('500x350+200+200')

label = tk.Label(root, text="Pick your Pokemon!", fg="red", bg="yellow", width=100, height=10)
label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

def create_button(root, pokemon):
    if pokemon == "Create your own Pokemon":
        button = tk.Button(root, text=pokemon, command=create_custom_pokemon)
    else:
        button = tk.Button(root, text=pokemon, command=lambda p=pokemon: display_stats(p))
    button.pack()

# Only the "Create your own Pokemon" button has functionality
create_button(root, "Charmander")
create_button(root, "Bulbasaur")
create_button(root, "Squirtle")
create_button(root, "Pikachu")
create_button(root, "Create your own Pokemon")

root.mainloop()
