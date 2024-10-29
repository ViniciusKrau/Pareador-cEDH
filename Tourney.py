from dataclasses import dataclass , field
from Player import Player
import random

@dataclass
class Tourney:

    _players: list = field(default_factory=list)
    _round: int = field(default=0)
    _tables: list = field(default_factory=list)
    _byeRule: bool = field(default=False)

    def upRound(self) -> None:
        self._round += 1
    
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
        return self._byeRule
    
    @byeRule.setter
    def byeRule(self, value:bool) -> None:
        self._byeRule = value

    def addPlayers(self, players:str) -> None:
        new_players = players.split('\n')
        for player in new_players:
            player = Player(player)
            self._players.append(player)

    def removePlayer(self, name:str) -> bool:
        for player in self._players:
            if player.name == name:
                self._player.remove(player) # Remove player from the list of players
                del player
                return True
        return False
    
    def populateTables(self) -> bool:
        if len(self._players) > 4:
            self._tables = [self._players[i:i + 4] for i in range(0, len(self._players), 4)]
            return True
        else:
            self._tables.appent(self._players)
        return False


    def scrambleTables(self) -> bool:
        self.checkForDrops()
        round = self.round
        byePlayers = [player for player in self._players if player.isBye]
        
        if round == 0:
            shuffled_players = self._players
            random.shuffle(shuffled_players)
            self._tables = [shuffled_players[i:i + 4] for i in range(0, len(shuffled_players), 4)]

        elif round > 0:
            sorted_players = [player for player in sorted_players if not player.isBye]
            for _ in byePlayers:
                sorted_players.pop()
            sorted_players.extend(byePlayers)
            sorted_players = sorted(self._players, key=lambda player: (player.score, player.opponentMatch1, player.opponentMatch2, player.opponentMatch3))
            self._tables = [sorted_players[i:i + 4] for i in range(0, len(sorted_players), 4)]

        else:
            return False
        
        if self.byeRule:
            last_table = self._tables[-1] if self._tables else []
            if len(last_table) < 4:
                for player in last_table:
                    player.isBye = True
        return True