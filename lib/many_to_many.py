class Author:

    all = []

    def __init__(self, name, date = None, royalties = None):
        self.name = name
        self.date = date
        self.royalties = royalties
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]


    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        contracts = [contract for contract in Contract.all if contract.author == self]
        contract_royalties = [contract.royalties for contract in contracts]
        total = sum(contract_royalties)
        return total

         


class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if author in Author.all:
            self.author = author
        else:
            raise Exception
        if book in Book.all:
            self.book = book
        else:
            raise Exception
        if type(date) == str:
            self.date = date
        else:
            raise Exception
        if type(royalties) == int:
            self.royalties = royalties
        else:
            raise Exception
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls):
        sorted_contracts = sorted(Contract.all, key = lambda contract: contract.date)
        return sorted_contracts
