from dataclasses import dataclass , field
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
        shuffled_players = [player for player in self.players if not player.isDrop()]
        random.shuffle(shuffled_players)
        self._tables = [shuffled_players[i:i + 4] for i in range(0, len(shuffled_players), 4)]


    def _scramble_rounds(self) -> None:
        _bye_players = [player for player in self._players if player.isBye() or player.isWasBye()]
        sorted_players = [player for player in sorted_players if not player.isBye() or player.isWasBye() or player.isDrop()]
        for player in _bye_players:
            sorted_players[-1].isBye = True
            sorted_players.pop()
            player.isWasBye = True
            player.isBye = False
        sorted_players.extend(_bye_players)
        sorted_players = sorted(self._players, key=lambda player: (player.score, player.opponentMatch1, player.opponentMatch2, player.opponentMatch3))
        self._tables = [sorted_players[i:i + 4] for i in range(0, len(sorted_players), 4)]

    def _treat_byes(self) -> None:
        last_table = self._tables[-1] if self._tables else []
        if len(last_table) < 4:
            for player in last_table:
                player.isBye = True
                player.score += 3
            self._tables.pop()

    def _scramble_tables(self) -> bool:

        if self._round == 0:
            self._scramble_round_0()

        if self._round > 0:
            self._scramble_rounds()
            

        if self._bye_rule:
            self._treat_byes()
        return True
    
    
    def table_result(self, result_dict:dict[int, Player]) -> bool:
        for table, winner in result_dict.items():
            self._table_result(table, winner)

    def _table_result(self, table:int, winner:Player = None) -> bool:
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
        sorted_players = sorted(self._players, key=lambda player: (player.score, player.opponentMatch1, player.opponentMatch2, player.opponentMatch3), reverse=True)
        for player in sorted_players:
            print(f"{player.name:<20} - {player.score:<2} - {player.roundsWon:<1} - {player.opponentMatch1:<3} - {player.opponentMatch2:<3} - {player.opponentMatch3:<3}")

    def start_tourney(self) -> bool:
        self.scramble_tables()
        self._round += 1
        return True
    
name = "Comedor de Casada123123"
score = 3
roundsWon = 1
opponentMatch1 = 12
opponentMatch2 = 32
opponentMatch3 = 612

print(f"{name:>15} Points: {score:<2} Rounds Won: {roundsWon:<1} CDD1: {opponentMatch2:<3} CDD2: {opponentMatch3:<3}")