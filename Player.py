
from dataclasses import dataclass, field


@dataclass  
class Player:

    _name: str
    _score: int = field(default=0)
    _rounds_won: float = field(default=0)
    _opponent_match2: float = field(default=0)
    _opponent_match3: float = field(default=0)
    _is_drop: bool = field(default=False)
    _is_bye: bool = field(default=False)
    _is_was_bye: bool = field(default=False)

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value) -> None:
        self._name = value

    @property
    def score(self) -> int:
        return self._score
    
    @score.setter
    def score(self, value) -> None:
        self._score = value
    
    @property
    def roundsWon(self) -> float:
        return self._rounds_won
    
    @roundsWon.setter
    def roundsWon(self, value) -> None:
        self._rounds_won = value

    @property
    def opponentMatch2(self) -> float:
        return self._opponent_match2
    
    @opponentMatch2.setter
    def opponentMatch2(self, value) -> None:
        self._opponent_match2 = value

    @property
    def opponentMatch3(self) -> float:
        return self._opponent_match3
    
    @opponentMatch3.setter
    def opponentMatch3(self, value) -> None:
        self._opponent_match3 = value

    @property
    def isDrop(self) -> bool:
        return self._is_drop
    
    @isDrop.setter
    def isDrop(self, value) -> None:
        self._is_drop = value

    @property
    def isBye(self) -> bool:
        return self._is_bye
    
    @isBye.setter
    def isBye(self, value) -> None:
        self._is_bye = value

    @property
    def isWasBye(self) -> bool:
        return self._is_was_bye
    
    @isWasBye.setter
    def isWasBye(self, value) -> None:
        self._is_was_bye = value