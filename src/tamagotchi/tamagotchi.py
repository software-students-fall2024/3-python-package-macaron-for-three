import tkinter as tk

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 50   # Hunger level (0-100)
        self.cleanliness = 50  # Cleanliness level (0-100)
        self.happiness = 50  # Happiness level (0-100)

    def feed(self):
        if self.hunger < 100:
            self.hunger += 10
        return self.hunger

    def clean(self):
        if self.cleanliness < 100:
            self.cleanliness += 10
        return self.cleanliness

    def pat(self):
        if self.happiness < 100:
            self.happiness += 10
        return self.happiness

def start_game():
    pet_name = name_entry.get()  
    #display_text()
    if pet_name:  # Make sure the player entered a name
        root.destroy()  # Close the start window
        game_window(pet_name)

def game_window(name):
    pet = Tamagotchi(name)
    
    def display_text():
        global entry
        string= entry.get()
        label.configure(text=string)

    def update_status():
        # Update the labels with the current status of the pet
        hunger_label.config(text=f"Hunger: {pet.hunger}")
        cleanliness_label.config(text=f"Cleanliness: {pet.cleanliness}")
        happiness_label.config(text=f"Happiness: {pet.happiness}")

    def feed_pet():
        pet.feed()
        status_label.config(text=f"{pet.name} has been fed!")
        update_status()

    def clean_pet():
        pet.clean()
        status_label.config(text=f"{pet.name} has been cleaned!")
        update_status()

    def pat_pet():
        pet.pat()
        status_label.config(text=f"You patted {pet.name}!")
        update_status()

    # Create a new window for the game
    window = tk.Tk()
    window.title(f"{name}'s Tamagotchi")
    label=tk.Label(window, text="", font=("Courier 22 bold"))
    label.pack()

    # Pet status display
    hunger_label = tk.Label(window, text=f"Hunger: {pet.hunger}")
    hunger_label.pack()

    cleanliness_label = tk.Label(window, text=f"Cleanliness: {pet.cleanliness}")
    cleanliness_label.pack()

    happiness_label = tk.Label(window, text=f"Happiness: {pet.happiness}")
    happiness_label.pack()

    # Buttons to interact with the pet
    feed_button = tk.Button(window, text="Feed", command=feed_pet)
    feed_button.pack()

    clean_button = tk.Button(window, text="Clean", command=clean_pet)
    clean_button.pack()

    pat_button = tk.Button(window, text="Pat", command=pat_pet)
    pat_button.pack()

    # Status message
    status_label = tk.Label(window, text=f"Welcome to {name}'s world!")
    status_label.pack()

    # Start game loop
    update_status()
    window.mainloop()

# Main window to enter pet's name
root = tk.Tk()
root.title("Tamagotchi")

# Label and entry field for pet's name
name_label = tk.Label(root, text="Enter your pet's name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

# Start game button
start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

root.mainloop()