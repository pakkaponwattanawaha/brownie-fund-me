from brownie import network, accounts, exceptions
from scripts.utils import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
import pytest


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    # add 100 for an extra money to the funded pool
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)

    # check basic logic
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)

    # we defined that if someone withdraw all account amountFunded is set to 0
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    # try to call withdraw with non-owner actor
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    # raise an exception for the error
    with pytest.raises(exceptions.VirtualMachineError):
        tx = fund_me.withdraw({"from": bad_actor})
        tx.wait(1)
