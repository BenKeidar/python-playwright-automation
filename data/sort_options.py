from enum import Enum


class SortOption(str, Enum):
    PRICE_LOW_TO_HIGH = "lohi"
    PRICE_HIGH_TO_LOW = "hilo"
    NAME_A_TO_Z = "az"
    NAME_Z_TO_A = "za"
