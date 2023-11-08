from typing import List, Dict
from pydantic import BaseModel


class SingleDataPoint(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float
