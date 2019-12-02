# Karol Talaga 302929
# Zbigniew Żeglecki 302947
from typing import Optional, List, Dict
from abc import ABC, abstractmethod


class Product:
    def __init__(self, product_name: str, price: float):
        self.product_name = product_name
        self.price = price


class TooManyProductsFoundError(Exception):
    pass


# FIXME: Każda z poniższych klas serwerów powinna posiadać: (1) metodę inicjalizacyjną przyjmującą listę obiektów typu
#  `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze, (2) możliwość
#  odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę
#  wyników wyszukiwania, (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów
#  spełniających kryterium wyszukiwania

class Server(ABC):
    def __init__(self, list_of_products: List[Product], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.list_of_products = list_of_products

    n_max_returned_entries = 3

    def make_dict(self) -> Dict[str, Product]:
        dict_of_products = {}
        for product in self.list_of_products:
            dict_of_products[product.product_name] = product
        return dict_of_products

    @abstractmethod
    def get_entries(self, n: int = 1):
        raise NotImplementedError


class ListServer:
    pass


class MapServer:
    pass


class Client:
    pass


    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()