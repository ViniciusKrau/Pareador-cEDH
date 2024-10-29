
from dataclasses import dataclass, field


@dataclass  
class Player:

    _name: str
    _score: int = field(default=0)
    _opponentMatch1: float = field(default=0)
    _opponentMatch2: float = field(default=0)
    _opponentMatch3: float = field(default=0)
    _isDrop: bool = field(default=False)
    _isBye: bool = field(default=False)

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
    def opponentMatch1(self) -> float:
        return self._opponentMatch1
    
    @opponentMatch1.setter
    def opponentMatch1(self, value) -> None:
        self._opponentMatch1 = value

    @property
    def opponentMatch2(self) -> float:
        return self._opponentMatch2
    
    @opponentMatch2.setter
    def opponentMatch2(self, value) -> None:
        self._opponentMatch2 = value

    @property
    def opponentMatch3(self) -> float:
        return self._opponentMatch3
    
    @opponentMatch3.setter
    def opponentMatch3(self, value) -> None:
        self._opponentMatch3 = value

    @property
    def isDrop(self) -> bool:
        return self._isDrop
    
    @isDrop.setter
    def isDrop(self, value) -> None:
        self._isDrop = value

    @property
    def isBye(self) -> bool:
        return self._isBye
    
    @isBye.setter
    def isBye(self, value) -> None:
        self._isBye = value