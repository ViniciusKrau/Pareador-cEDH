import Player as pl
import Tourney as tr

def read_players(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
            return contents
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = 'path/to/your/file.txt'  # Replace with the path to your text file
    read_players(file_path)

def main():
    # Create a new tournament
    tourney = tr.Tourney()

    # Add players to the tournament
    

if __name__ == "__main__":
    main() 