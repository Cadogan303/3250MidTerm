#Pokemon Game
import tkinter as tk

# Pokemon Class
class Pokemon:
    def __init__(self, name:str, type:str, hit:int, health:int):
        self.name = name
        self.type = type
        self.hit = hit
        self.health = health

    # To set color to type... to do later
    #def typeColor():
    #    if Pokemon.type == 'fire':
    #        text-color == 'red'

    def attack(self, Pokemon):
        print(f"{self.name} ATTACKS!")
        attackChance = chance()
        print(attackChance)

        if attackChance in [3, 4, 5]:
            print(attackChance)
            print("Attack Successful! -" + str(self.hit))
            Pokemon.health = Pokemon.health - self.hit
        elif attackChance in [1, 2]:
            print(attackChance)
            print(f"{self.name} unleashes SUPER ATTACK!")
            print(f"{self.name}'s attack does DOUBLE DAMAGE!")
            Pokemon.health = Pokemon.health - 2*self.hit
        else: #attackChance == 0
            print(f"{self.name}'s attack failed!")

        print(f"{self.name}'s health: "f"{self.health}")
        print(f"{Pokemon.name}'s health: "f"{Pokemon.health} \n")

    def defend(self):
        defensePerk = chance()
        print(defensePerk)
        if defensePerk == 0:
            print(f"{self.name} fails to Defend!")
        elif defensePerk == 1 or 2:
            print(f"{self.name} Enters Hibernation Mode! Health increases a little!: +100")
            self.health = self.health + 100
        else: #defensePerk == 3 or 4 or 5:
            print(f"{self.name} Enters Meditative Mode! Health increases a significant amount!: +500")
            self.health = self.health + 500

        print(f"{self.name}'s health: "f"{self.health} \n")
    
    def retaliate(self, Pokemon):
        ret = chance()
        print(ret)
        if ret == 0 or 1 or 2:
            print(f"{Pokemon.name} was left open! \n")
            print(f"{self.name} retaliates!")
            self.attack(Pokemon)
        else:
            print(f"{self.name} fails to retaliate")
# END of Pokemon Class
            
# BATTLE CLASS            
def Battle(self, Pokemon):

    while self.health > 0 and Pokemon.health > 0:
        action = str.lower(input("Would you like to attack or defend?: "))
        if action == "attack":
            self.attack(Pokemon)
    
        elif action == "defend":
            self.defend()
            Pokemon.retaliate(self)
        else:
            print("Unknown action! Pokemon confused!")
            self.attack(Pokemon)
            print("However, " + self.name + " was distracted by your actions.")
            Pokemon.retaliate(self)
        if Pokemon.health <= 0 or self.health <= 0:
            break
# OPPONENT ACTIONS
        print("OPPONENTS TURN: \n")
        opponentActions = chance()
        print(opponentActions)
        if opponentActions == 0 or 1 or 2:
            Pokemon.attack(self)
        else:
            Pokemon.defend()
            self.retaliate(Pokemon)
        if self.health <= 0 or Pokemon.health <= 0:
            break
# END of BATTLE CLASS
        
def Initiate():
    Battle(Charmander,Pikachu)
            
# Standard Pokemons
Charmander = Pokemon('Charmander','fire',150,1000)
Bulbasaur = Pokemon('Bulbasaur','earth',150,1000)
Squirtle = Pokemon('Squirtle','water',150,1000)
Pikachu = Pokemon('Pikachu','electric',150,1000)
Custom = Pokemon('Create New!','need',100,1000)

StdPokemonsList = ('Charmander', 'Bulbasaur', 'Squirtle', 'Pikachu')

# Main window
root = tk.Tk()
root.title("Welcome to The Pokemon Game")
root.geometry()

# Frame containing Character Selection Options
CharSelectionFrame = tk.Frame(master = root, height = 300)

# Main title displaying in Character Selection Frame
WelcomeMsg = tk.Label(
    master=CharSelectionFrame, 
    text="Pick your Pokemon!",
    font='Helvetica 20 bold',
    fg="red", 
    bg="yellow", 
    )
WelcomeMsg.pack()

# Where Pokemon traits will be displayed
result_label = tk.Label(CharSelectionFrame, text="")
StartBtn = tk.Button(text="hidden", height=3, width=20, bg="black",fg="white",command=Initiate)

def ShowBattleBtn():
    StartBtn.config(text = "Begin Battle!?")
    StartBtn.pack()

def display_stats(Pokemon:Pokemon):
    if Pokemon.name in StdPokemonsList:
        result_label.config(text=f"You've chosen {Pokemon.name} a {Pokemon.type} type Pokemon with Health: {Pokemon.health}, and Power: {Pokemon.hit}")
    else:
        create_custom_pokemon()
    
    ShowBattleBtn()

# Frame where battle sequence should commence
BattleFrame = tk.Frame(master = root, height = 300)

CharSelectionFrame.pack()

result_label.pack()

# Create your own Pokemon window (Called when "Create New!" btn is selected)
def create_custom_pokemon():
    custom_window = tk.Toplevel(root)
    custom_window.title("Pokemon Creation")
    custom_window.geometry()
    
    WindowDescription = tk.Label(custom_window, text = "Choose attributes for your Pokemon!")
    WindowDescription.grid(row=0,column=0,columnspan = 2, sticky = tk.W+tk.E)

    # Create input fields for custom Pokemon attributes
    name_label = tk.Label(custom_window, text="Name:")
    name_label.grid(row=1,column=0)
    name_entry = tk.Entry(custom_window)
    name_entry.grid(row=1,column=1)


    type_label = tk.Label(custom_window, text="Type:")
    type_label.grid(row=2, column=0)
    type_entry = tk.Entry(custom_window)
    type_entry.grid(row=2, column=1)

    power_label = tk.Label(custom_window, text="Power:")
    power_label.grid(row=3, column=0)
    power_entry = tk.Entry(custom_window)
    power_entry.grid(row=3, column=1)

    # Function to close window once Custom Pokemon is Created
    def CloseWindow():
        custom_window.destroy()

    # Function to retrieve details from usr then displayed when create btn selected
    def create_pokemon():
        name = name_entry.get()
        type = type_entry.get()
        hit = power_entry.get()
        result_label.config(text=f"You've created {name}, a {type} type Pokemon with power level {hit}!")
        CloseWindow()
        return Pokemon(name,type,hit,1000)
        
    create_button = tk.Button(custom_window, text="Create",width=10,height=2,bg="darkcyan",fg="black", command=create_pokemon)
    create_button.grid(row=4, column= 0, columnspan=2)

def create_button(Pokemon:Pokemon, element):

    CharSelectionBtn = tk.Button(
        master=CharSelectionFrame, 
        text = Pokemon.name,
        width=20,
        height=2,
        bg=element,
        fg="black",
        command = lambda: display_stats(Pokemon))
    CharSelectionBtn.pack(side=tk.LEFT)

# Only the "Create your own Pokemon" button has functionality
create_button(Charmander, "red")
create_button(Bulbasaur,"blue")
create_button(Squirtle, "green")
create_button(Pikachu, "yellow")
create_button(Custom, "grey")

root.mainloop()
