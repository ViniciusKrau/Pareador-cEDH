from dataclasses import dataclass , field
from tabulate import tabulate
from termcolor import colored
from Player import Player
import logging
import traceback
import random


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
@dataclass
class Tourney:

    _players: list = field(default_factory=list)
    _round: int = field(default=0)
    _tables: list = field(default_factory=list)
    _dropped_players: list = field(default_factory=list)
    _bye_rule: bool = field(default=False)
    
    @property
    def players(self) -> list:
        return self._players
    
    @players.setter
    def players(self, value:list) -> None:
        self._players = value

    @property
    def round(self) -> int:
        return self._round
    
    @round.setter
    def round(self, value:int) -> None:
        self._round = value

    @property
    def tables(self) -> list:
        return self._tables
    
    @tables.setter
    def tables(self, value:list) -> None:
        self._tables = value
    
    @property
    def byeRule(self) -> bool:
        return self._bye_rule
    
    @byeRule.setter
    def byeRule(self, value:bool) -> None:
        self._bye_rule = value

    @property
    def droppedPlayers(self) -> list:
        return self._dropped_players
    
    @droppedPlayers.setter
    def droppedPlayers(self, value:list) -> None:
        self._dropped_players = value

    def getPlayerByName (self, name:str) -> Player:
        for player in self._players:
            if player.name == name:
                return player

    def addPlayers(self, players:str) -> None:
        new_players = players.split('\n')
        for player in new_players:
            player = Player(player)
            self._players.append(player)
        logger.info(f"Players added: {new_players}")

    def removePlayer(self, name:str) -> bool:
        for player in self._players:
            if player.name == name:
                self._player.remove(player)
                del player
                logger.info(f"Player removed: {name}")
                return True
        logger.info(f"Player removal failed: {name}")
        return False
    
    def dropPlayerByName(self, name:str) -> bool:
        self.dropPlayer(self.getPlayerByName(name))
    
    def dropPlayer(self, player:Player) -> bool:
        try:
            player.isDrop = True
            self._dropped_players.append(player)
        except Exception:
            traceback.print_exc()
            return False
        logger.info(f"Player dropped: {Player.name}")
        return True
    
    def populateTables(self) -> bool:
        if len(self._players) > 4:
            self._tables = [self._players[i:i + 4] for i in range(0, len(self._players), 4)]
            return True
        else:
            self._tables.appent(self._players)
        return False
    
    
    def _scramble_round_0(self) -> None:
        shuffled_players = [player for player in self._players if not player.isDrop()]
        random.shuffle(shuffled_players)
        self._tables = [shuffled_players[i:i + 4] for i in range(0, len(shuffled_players), 4)]


    def _scramble_rounds(self) -> None:
        noDropPlayers = [player for player in sorted_players if not player.isDrop()]
        sorted_players = sorted(noDropPlayers, key=lambda player: (player.score, player.roundswon, player.opponentMatch2, player.opponentMatch3))
        self._tables = [sorted_players[i:i + 4] for i in range(0, len(sorted_players), 4)]

    def _treat_byes(self) -> None:
        last_table = self._tables[-1] if self._tables else []
        players_not_in_last_table = [player for table in self._tables for player in table if player not in last_table]

        if len(last_table) >= 4:
            return
        
        # Swap already byed players with not byed players or give a bye to a player
        for player in last_table:

            if not player.isWasBye:
                player.isBye = True
                player.isWasBye = True
                player.score += 3
                continue

            for player2 in reversed(players_not_in_last_table):
                if player2.isWasBye:
                    continue
                player2.isBye = True
                player2.isWasBye = True
                player2.score += 3
                self.swap_players(player, player2)
                break

                

    def _scramble_tables(self) -> bool:

        if self._round == 0:
            self._scramble_round_0()

        if self._round > 0:
            self._scramble_rounds()
            

        if self._bye_rule:
            self._treat_byes()
        return True
    
    
    def set_player_as_bye_by_name(self, name:str) -> bool:
        player = self.getPlayerByName(name)
        return self.set_player_as_bye(player)
    
    
    def set_player_as_bye(self, player:Player) -> bool:
        player.isBye = True
        player.isWasBye = True
        for table in self._tables:
            if player in table:
                table.remove(player)
                break
        return True
    
    
    def swap_players(self, player1:Player, player2:Player) -> None:
        if (player1.isDrop
                or player2.isDrop
                or player1 == player2
                or len(self._tables) <= 0 
                or player1 not in self._players 
                or player2 not in self._players):
            return
        
        for table in self._tables:
            if player1 in table:
                index = table.index(player1)
                table[index] = player2
            if player2 in table:
                index = table.index(player2)
                table[index] = player1
        
    
    def table_result_by_dict(self, result_dict:dict[int, Player]) -> bool:
        for table, winner in result_dict.items():
            self.table_result(table, winner)


    def table_result(self, table:int, winner:Player = None) -> bool:
        players = self._tables[table]
        opponent_match2_list :list = [player.score for player in players]
        opponent_match3_list :list = [player.opponentMatch2 for player in players]

        for idx,player in enumerate(players):
            player.opponentMatch2 += sum(opponent_match2_list[:idx] + opponent_match2_list[idx+1:])
            player.opponentMatch3 += sum(opponent_match3_list[:idx] + opponent_match3_list[idx+1:])

            if winner is not None:
                if player == winner:
                    player.score += 3
                    player.roundsWon += 1
            elif winner is None:
                player.score += 1
        return True
    
    
    def display_leaderboard(self) -> None:
        sorted_players = sorted(self._players, key=lambda player: (player.score, player.roundsWon, player.opponentMatch2, player.opponentMatch3), reverse=True)
    
        # Prepare data for tabulate
        table_data = []
        for player in sorted_players:
            table_data.append([
            player.name[:15],  # Truncate name to 15 characters
            player.score,
            player.roundsWon,
            player.opponentMatch2,
            player.opponentMatch3
            ])
        
        # Define table headers
        headers = ["Name", "Score", "Rounds Won", "Opponent Match 2", "Opponent Match 3"]
        
        # Print the leaderboard using tabulate
        print(tabulate(table_data, headers=headers, tablefmt="grid"))


    def start_tourney(self) -> bool:
        self.scramble_tables()
        self._round += 1
        return True
