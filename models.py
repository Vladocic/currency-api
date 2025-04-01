from pydantic import BaseModel
from typing import Optional, List


class Currency(BaseModel):
    num_code: int
    char_code: str
    unit: int
    name: str
    rate: float

class CurrencyUpdate(BaseModel):
    num_code: int
    char_code: Optional[str] = None
    unit: Optional[int] = None
    name: Optional[str] = None
    rate: Optional[float] = None

class CurrencyDelete(BaseModel):
    num_code: Optional[List[int]] = None
    char_code: Optional[List[str]] = None
    unit: Optional[List[int]] = None
    name: Optional[List[str]] = None
    rate: Optional[List[float]] = None