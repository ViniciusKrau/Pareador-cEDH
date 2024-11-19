import tkinter as tk
from tkinter import filedialog, messagebox
import Player as pl
import Tourney as tr

def read_players(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def start_tournament(file_path):
    tourney = tr.Tourney()
    tourney.addPlayers(read_players(file_path))
    tourney.next_round()
    tourney.display_leaderboard()
    tourney.display_tables()

def main():
    global tourney
    start_tournament("participants.txt")
    root = tk.Tk()
    root.title("Tournament Manager")

    rows = len(tourney.players)

    open_button = tk.Button(root, text="Open Participants File", command=open_file)
    open_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()