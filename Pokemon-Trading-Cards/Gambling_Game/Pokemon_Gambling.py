import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import random

class Card:
    def __init__(self, name, value, image):
        self.name = name
        self.value = value
        self.image = image

class CardPack:
    def __init__(self):
        self.cards = []
        self.populate_pack()

    def populate_pack(self):
        # Add cards to the pack
        self.cards.append(Card("Charizard", 10, "card1.png"))
        self.cards.append(Card("Blastoise", 20, "card2.png"))
        self.cards.append(Card("Infernape", 15, "card3.png"))
        self.cards.append(Card("Fuecoco", 25, "card4.png"))
        self.cards.append(Card("Squirtle", 30, "card5.png"))
        self.cards.append(Card("Mr.Mime", 18, "card6.png"))
        self.cards.append(Card("Ditto", 22, "card7.png"))
        self.cards.append(Card("Gengar", 35, "card8.png"))
        self.cards.append(Card("Pikachu", 40, "card9.png"))
        self.cards.append(Card("Buff Mosquito", 45, "card10.png"))

class Marketplace:
    def __init__(self):
        self.cards = []
        self.populate_marketplace()

    def populate_marketplace(self):
        self.cards.append(Card("Charizard", 10, "card1.png"))
        self.cards.append(Card("Blastoise", 20, "card2.png"))
        self.cards.append(Card("Infernape", 15, "card3.png"))
        self.cards.append(Card("Fuecoco", 25, "card4.png"))
        self.cards.append(Card("Squirtle", 30, "card5.png"))
        self.cards.append(Card("Mr.Mime", 18, "card6.png"))
        self.cards.append(Card("Ditto", 22, "card7.png"))
        self.cards.append(Card("Gengar", 35, "card8.png"))
        self.cards.append(Card("Pikachu", 40, "card9.png"))
        self.cards.append(Card("Buff Mosquito", 45, "card10.png"))

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Card Collection Game")
        self.root.geometry("600x400")  # Set window size
        self.background_image = ImageTk.PhotoImage(Image.open("background.png"))  # Load background image
        self.alleyway_image = ImageTk.PhotoImage(Image.open("alleyway.png"))  # Load alleyway background image
        self.dead_image = ImageTk.PhotoImage(Image.open("dead.png"))  # Load dead background image
        self.card_pack = CardPack()
        self.marketplace = Marketplace()
        self.money = 100  # Initial money
        self.collected_cards = []  # List to keep track of collected cards
        self.create_widgets()
        self.marketplace_window = None
        self.mafia_button = None
        self.borrowed_money = False
        self.borrowed_turns = 0

    def sell_card(self, card, bag_window):
        self.money += card.value
        self.collected_cards.remove(card)  # Remove the sold card from the bag
        self.money_label.config(text=f"Money: ${self.money}")
        messagebox.showinfo("Sold", f"You sold {card.name} for ${card.value}!")
        bag_window.destroy()  # Close the bag window after selling the card
    def create_widgets(self):
        # Background image
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Money label
        self.money_label = tk.Label(self.root, text="Money: $100", font=("Helvetica", 16), bg="white")
        self.money_label.place(relx=0.5, rely=0.1, anchor="center")

        # Open Pack button
        self.open_pack_button = tk.Button(self.root, text="Open Pack", command=self.open_pack, font=("Helvetica", 14), bg="green", fg="white")
        self.open_pack_button.place(relx=0.5, rely=0.3, anchor="center")

        # View Bag button
        self.view_bag_button = tk.Button(self.root, text="View Bag", command=self.view_bag, font=("Helvetica", 14), bg="blue", fg="white")
        self.view_bag_button.place(relx=0.5, rely=0.4, anchor="center")

        # Sell Entire Bag button
        self.sell_bag_button = tk.Button(self.root, text="Sell Entire Bag", command=self.sell_entire_bag,
                                         font=("Helvetica", 14), bg="red", fg="white")
        self.sell_bag_button.place(relx=0.5, rely=0.5, anchor="center")

    def open_pack(self):
        if self.money >= 10:  # Example cost to open a pack
            self.money -= 10
            self.money_label.config(text=f"Money: ${self.money}")

            # Check if the "Need Cash?" button should be shown


            # Randomly select a card based on probabilities
            card_name = self.get_random_card()

            # Get the card object using its name
            card = next((c for c in self.card_pack.cards if c.name == card_name), None)
            
            if card is None:
                messagebox.showerror("Error", f"Failed to find card: {card_name}")
                return

            # Add the collected card to the collection
            self.collected_cards.append(card)

            # Create a new window to display the obtained card
            popup_window = tk.Toplevel(self.root)
            popup_window.title("Obtained Card")

            # Set background color based on card name
            background_color = self.get_background_color(card_name)
            popup_window.configure(bg=background_color)

            # Adjusted geometry for a vertical rectangle shape
            popup_window.geometry("250x350")

            # Resize image to fit the window
            image = Image.open(card.image)
            image_width, image_height = image.size
            aspect_ratio = image_width / image_height
            new_height = 300
            new_width = int(new_height * aspect_ratio)
            image = image.resize((new_width, new_height), Image.ANTIALIAS)

            # Display card image
            card_image = ImageTk.PhotoImage(image)
            card_image_label = tk.Label(popup_window, image=card_image, bg=background_color)
            card_image_label.image = card_image
            card_image_label.pack()

            # Display card name
            card_name_label = tk.Label(popup_window, text=f"Name: {card.name}", font=("Helvetica", 14), bg=background_color)
            card_name_label.pack()

            # Increase borrowed turns counter if applicable
            if self.borrowed_money:
                self.borrowed_turns += 1
                if self.borrowed_turns >= 5:
                    self.show_dead_window()

        else:
            messagebox.showerror("Error", "You don't have enough money to open a pack!")     

    def get_random_card(self):
        # Define card probabilities (adjust as needed)
        card_probabilities = {
            "Charizard": 0.1,  # Probability of 10%
            "Blastoise": 0.1,  # Probability of 10%
            "Infernape": 0.1,  # Probability of 10%
            "Fuecoco": 0.1,  # Probability of 10%
            "Squirtle": 0.1,  # Probability of 10%
            "Mr.Mime": 0.1,  # Probability of 10%
            "Ditto": 0.1,  # Probability of 10%
            "Gengar": 0.1,  # Probability of 10%
            "Pikachu": 0.1,  # Probability of 10%
            "Buff Mosquito": 0.1,  # Probability of 10%
        }

        # Generate a random number between 0 and 1
        random_num = random.random()

        # Select a card based on probabilities
        cumulative_prob = 0
        for card, prob in card_probabilities.items():
            cumulative_prob += prob
            if random_num < cumulative_prob:
                return card
        # Default return, should not reach here
        return None

    def get_background_color(self, card_name):
        # Define background colors for each card
        card_colors = {
            "Charizard": "light salmon",
            "Blastoise": "light blue",
            "Infernape": "light salmon",
            "Fuecoco": "light salmon",
            "Squirtle": "light blue",
            "Mr.Mime": "light purple",
            "Ditto": "light grey",
            "Gengar": "light purple",
            "Pikachu": "light yellow",
            "Buff Mosquito": "light salmon",
        }
        # Return background color based on card name
        return card_colors.get(card_name, "white")  # Default to white if card name not found

    def sell_entire_bag(self):
        for card in self.collected_cards:
            self.money += card.value
        self.collected_cards.clear()  # Clear the bag after selling all cards
        self.money_label.config(text=f"Money: ${self.money}")
        messagebox.showinfo("Sold", "You sold the entire bag!")
    def view_bag(self):
        # Create a new window to display the collected cards for selling
        bag_window = tk.Toplevel(self.root)
        bag_window.title("Bag")

        # Add some padding around the card buttons
        card_frame = tk.Frame(bag_window, bg="white", padx=20, pady=10)
        card_frame.pack()

        # Create buttons for each collected card
        for card in self.collected_cards:
            card_button = tk.Button(card_frame, text=card.name, command=lambda c=card: self.show_card_details(c, bag_window), font=("Helvetica", 12), bg="lightgrey", fg="black", padx=10, pady=5, relief=tk.GROOVE)
            card_button.pack(side=tk.TOP, pady=5)

    def show_card_details(self, card, bag_window):
        # Create a new window to display card details
        details_window = tk.Toplevel(bag_window)
        details_window.title("Card Details")

        # Display card name
        card_name_label = tk.Label(details_window, text=f"Name: {card.name}", font=("Helvetica", 14))
        card_name_label.pack()

        # Display card image
        image = Image.open(card.image)
        image_width, image_height = image.size
        aspect_ratio = image_width / image_height
        new_height = 200
        new_width = int(new_height * aspect_ratio)
        image = image.resize((new_width, new_height), Image.LANCZOS)

        card_image = ImageTk.PhotoImage(image)
        card_image_label = tk.Label(details_window, image=card_image)
        card_image_label.image = card_image
        card_image_label.pack()

        # Display card value
        card_value_label = tk.Label(details_window, text=f"Value: ${card.value}", font=("Helvetica", 14))
        card_value_label.pack()

        # Sell Card button
        sell_button = tk.Button(details_window, text="Sell Card", command=lambda c=card: self.sell_card(c, bag_window), font=("Helvetica", 14), bg="red", fg="white")
        sell_button.pack()



    def run(self):
        self.root.mainloop()

gui = GUI()
gui.run()

