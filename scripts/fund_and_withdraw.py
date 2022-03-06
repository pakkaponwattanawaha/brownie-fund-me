from brownie import FundMe
from scripts.utils import get_account


def fund():
    # Smart contract in python kinda act like its own class that can calculat and persist data on the chain!!!!
    fund_me = FundMe[-1]
    print("FundMe Obj", FundMe)
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current enrty fee in {entrance_fee}")
    print("Funding")
    fund_me.fund(
        {"from": account, "value": entrance_fee}
    )  # balance will be deducted from the address bc it that way in SC


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw(
        {"from": account}
    )  # balance will be added to the account bc its that way in SC


def main():
    fund()
    withdraw()
