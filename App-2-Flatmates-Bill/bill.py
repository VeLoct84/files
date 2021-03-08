class Bill:
    """
    Object that contains data about bill, such as total amount and period
    of the bill.
    """

    def __init__(self, amount, time):
        self.amount = amount    # refer to total amount of the period
        self.time = time    # period E.g. "Jan, Feb, etc"


class Flatmate:
    """
    Object that contains data about name of people, period staying, and
    return the bill to pay
    """

    def __init__(self, name, day_in_house):
        self.name = name    # name of mate who's stay in house
        self.day_in_house = day_in_house

    def pays(self, bill, flatmate2):
        weight = self.day_in_house/(self.day_in_house + flatmate2.day_in_house)
        to_pay = bill.amount * weight
        return to_pay
