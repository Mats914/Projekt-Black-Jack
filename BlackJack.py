import tkinter as tk
import random

# Card suits and ranks
suits = ['♥', '♠', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Create and shuffle a deck of cards
def skapa_kortlek():
    kortlek = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(kortlek)
    return kortlek

# Calculate total score of a hand
def beräkna_poäng(hand):
    poäng = 0
    ess = 0
    for kort in hand:
        poäng += values[kort[0]]
        if kort[0] == 'A':
            ess += 1
    # Adjust for Aces if score is over 21
    while poäng > 21 and ess:
        poäng -= 10
        ess -= 1
    return poäng

# Format hand for display
def format_hand(hand):
    return '  '.join([f"{r}{s}" for r, s in hand])

class Blackjack:
    def __init__(self, master):
        self.master = master
        master.title("Blackjack")

        # Layout frames
        self.info_frame = tk.Frame(master)
        self.info_frame.pack(pady=10)

        self.knapp_frame = tk.Frame(master)
        self.knapp_frame.pack(pady=10)

        self.restart_frame = tk.Frame(master)
        self.restart_frame.pack(pady=10)

        # Labels for game info
        self.spelar_label = tk.Label(self.info_frame, text="Dina kort: ")
        self.spelar_label.pack()

        self.dator_label = tk.Label(self.info_frame, text="Datorns kort: ")
        self.dator_label.pack()

        self.resultat_label = tk.Label(self.info_frame, text="", font=('Helvetica', 14, 'bold'))
        self.resultat_label.pack(pady=5)

        # Buttons
        self.hit_knapp = tk.Button(self.knapp_frame, text="Kort (Hit)", width=12, command=self.spelare_tar_kort)
        self.hit_knapp.pack(side=tk.LEFT, padx=5)

        self.stand_knapp = tk.Button(self.knapp_frame, text="Stanna (Stand)", width=12, command=self.spelare_stannar)
        self.stand_knapp.pack(side=tk.RIGHT, padx=5)

        self.spela_igen_knapp = tk.Button(self.restart_frame, text="Spela igen", command=self.starta_om_spelet)
        self.spela_igen_knapp.pack()

        self.starta_spel()

    # Start a new game
    def starta_spel(self):
        self.kortlek = skapa_kortlek()
        self.spelare_hand = [self.kortlek.pop(), self.kortlek.pop()]
        self.dator_hand = [self.kortlek.pop(), self.kortlek.pop()]
        self.uppdatera_visning(initial=True)

    # Update cards shown on screen
    def uppdatera_visning(self, initial=False):
        spelar_poäng = beräkna_poäng(self.spelare_hand)
        self.spelar_label.config(text=f"Dina kort: {format_hand(self.spelare_hand)} (Poäng: {spelar_poäng})")

        if initial:
            # Show only one card for dealer initially
            d_kort = f"{self.dator_hand[0][0]}{self.dator_hand[0][1]}"
            self.dator_label.config(text=f"Datorns kort: {d_kort}  ??")
        else:
            dator_poäng = beräkna_poäng(self.dator_hand)
            self.dator_label.config(text=f"Datorns kort: {format_hand(self.dator_hand)} (Poäng: {dator_poäng})")

    # When player chooses to "Hit"
    def spelare_tar_kort(self):
        self.spelare_hand.append(self.kortlek.pop())
        self.uppdatera_visning(initial=True)
        if beräkna_poäng(self.spelare_hand) > 21:
            self.resultat_label.config(text="Du förlorade! Du gick över 21.")
            self.inaktivera_knappar()

    # When player chooses to "Stand"
    def spelare_stannar(self):
        while beräkna_poäng(self.dator_hand) < 17:
            self.dator_hand.append(self.kortlek.pop())
        self.uppdatera_visning(initial=False)
        self.kolla_vinnare()
        self.inaktivera_knappar()

    # Decide the winner
    def kolla_vinnare(self):
        spelar_poäng = beräkna_poäng(self.spelare_hand)
        dator_poäng = beräkna_poäng(self.dator_hand)

        if dator_poäng > 21:
            self.resultat_label.config(text="Datorn gick över 21! Du vann!")
        elif spelar_poäng > dator_poäng:
            self.resultat_label.config(text="Du vann!")
        elif spelar_poäng < dator_poäng:
            self.resultat_label.config(text="Datorn vann!")
        else:
            self.resultat_label.config(text="Oavgjort!")

    # Disable buttons after game ends
    def inaktivera_knappar(self):
        self.hit_knapp.config(state=tk.DISABLED)
        self.stand_knapp.config(state=tk.DISABLED)

    # Restart the game
    def starta_om_spelet(self):
        self.hit_knapp.config(state=tk.NORMAL)
        self.stand_knapp.config(state=tk.NORMAL)
        self.resultat_label.config(text="")
        self.starta_spel()

# Launch the game
root = tk.Tk()
spel = Blackjack(root)
root.mainloop()
