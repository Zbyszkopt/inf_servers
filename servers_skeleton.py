# Karol Talaga 302929
# Zbigniew Żeglecki 302947

import re
from typing import Optional, List, Dict
from abc import ABC, abstractmethod


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __hash__(self):
        return hash((self.name, self.price))

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


class TooManyProductsFoundError(Exception):
    pass


class Server(ABC):
    def __init__(self, list_of_products: List[Product]) -> None:
        self.list_of_products = list_of_products

    n_max_returned_entries = 3

    def make_dict(self) -> Dict[str, Product]:
        dict_of_products = {product.name: product for product in self.list_of_products}
        return dict_of_products

    @abstractmethod
    def get_entries(self, n_letters: int = 1):
        raise NotImplementedError


class ListServer:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_entries(self, n_letters: int = 1) -> List[Product]:
        wishlist = []
        for prod in self.list_of_products:
            let_ = re.split('(\d+)', prod.name)[0]
            num_ = re.split('(\d+)', prod.name)[1]
            if len(num_) == 2 or len(num_) == 3:
                if len(let_):
                    wishlist.append(product)
        if len(wishlist) > self.n_max_returned_entries:
            raise TooManyProductsFoundError()
        sorted_wishlist = sorted(wishlist, key=lambda product: product.price)
        return sorted_wishlist


class MapServer(Server):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
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










