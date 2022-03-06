from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3


DECIMALS = 8
STARTING_PRICE = 200_000_000_000

FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENT
    ):
        print("My account!!!", accounts[0])
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

    # when work with local environment there is no chainlink aggregator provided so we import and deploy our own


def deploy_mock():

    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
