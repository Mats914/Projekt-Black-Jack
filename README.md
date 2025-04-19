# 🃏 Blackjack med Tkinter

Detta projekt är en enkel implementation av Blackjack-spelet med en grafisk användargränssnitt (GUI) byggd i Python med hjälp av Tkinter.

## 🎮 Spelets regler

- Spelet spelas mot datorn med en vanlig kortlek (52 kort) som blandas varje runda.
- Både spelaren och datorn får två kort i början. Datorn visar endast ett av sina kort först.
- Spelaren kan välja att:
  - **Kort (Hit)** – ta ett till kort.
  - **Stanna (Stand)** – sluta ta fler kort.
- Om spelaren går över 21 poäng förlorar hen direkt.
- När spelaren stannar:
  - Datorn drar kort tills den når minst 17 poäng.
  - Om datorn går över 21 poäng vinner spelaren.
  - Annars vinner den med högst poäng (max 21).

## ▶️ Så kör du spelet

### ✅ Förutsättningar
Du behöver ha **Python 3** installerat.

### 🧪 Installation & Körning
1. Klona eller ladda ner projektet till din dator.
2. Öppna terminalen i projektmappen.
3. Kör kommandot:

```bash
python blackjack.py
