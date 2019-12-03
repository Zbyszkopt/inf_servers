# Karol Talaga 302929
# Zbigniew Żeglecki 302947

import re
from typing import Optional, List, Dict
from abc import ABC, abstractmethod


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
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


class MapServer(Server):

    def __init__(self, list_of_products: List[Product], n_max_returned_entries: int, *args, **kwargs) -> None:
        super().__init__(list_of_products, n_max_returned_entries, *args, **kwargs)
        self.dict_of_products = self.make_dict()

    def get_entries(self, n_letters: int = 1) -> List[Product]:

        wishlist = []
        for id, value in self.dict_of_products.items():
            let_ = re.split('(\d+)', id)[0]
            num_ = re.split('(\d+)', id)[1]
            if len(num_) == 2 or len(num_) == 3:
                if len(let_) == n_letters:
                    wishlist.append(value)

        if len(wishlist) > self.n_max_returned_entries:
            raise TooManyProductsFoundError

        sorted_wishlist = sorted(list_, key=lambda product: product.price)

        return sorted_wishlist


class Client:

    def __init__(self, server: Server) -> None:
        self.server = server

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:

        sum_of_prices = 0

        try:
            work_lst = self.server.get_entries(n_letters)
            for prod in work_lst:
                sum_of_prices += prod.price
        except TooManyProductsFoundError:
            print('Error in getting prices for number: {num}\n Reason: Too many products have been found'.format(num=n_letters))
            return None

        if sum_of_prices == 0:
            return None
        else:
            return sum_of_prices










