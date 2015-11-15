class Bill:

    def __init__(self, amount):
        self. amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.amount)

    def __eq__(self, other):
        return self.amount == other.amount

    def __int__(self):
        return self.amount


class BillBatch:

    def __init__(self, Bills):
        self. Bills = Bills

    def __len__(self):
        return len(self.Bills)

    def total(self):
        return sum(self.Bills)

    def __getitem__(self, index):
        self.index = index
        return self.Bills[self.index]


class CashDesk:

    def __init__(self):
        self.dict = {}
        self.amount = 0

    def check_bill(self, money):
        if isinstance(money, BillBatch):
            for bill in money:
                if bill not in self.dict:
                    self.dict[bill] = 1
                else:
                    self.dict[bill] += 1
        elif isinstance(money, Bill):
            if money not in self.dict:
                self.dict[money] = 1
            else:
                self.dict[money] += 1

    def take_money(self, money):
        self.check_bill(money)
        if isinstance(money, BillBatch):
            self.amount += money.total()
        elif isinstance(money, Bill):
            self.amount += int(money)

    def total(self):
        return self.amount

    def inspect(self):
        return self.dict


a = Bill(10)
b = Bill(5)
c = Bill(10)

int(a) == 10
str(a) == "A 10$ bill"
print(a)

a == b
a == c
money_holder = {}

money_holder[a] = 1

if c in money_holder:
    money_holder[c] += 1

print(c)  # { "A 10$ bill": 2 }
print("BLA")
values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

for bill in batch:
    print(bill)

print("BLA")

values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BillBatch(bills)

desk = CashDesk()

print(desk.take_money(batch))
print(desk.take_money(Bill(10)))
