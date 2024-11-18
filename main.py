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

def main():
    # Create a new tournament
    tourney = tr.Tourney()
    file_path = 'participants.txt'  # Replace with the path to your text file
    tourney.addPlayers(read_players(file_path))
    tourney.populateTables()
    tourney.table_result_by_dict({0:"Krau", 1:"Vitor", 2:"Claudio"})
    tourney.display_leaderboard()
    

if __name__ == "__main__":
    main() 