from brownie import FundMe, MockV3Aggregator, network, config
from scripts.utils import get_account, deploy_mock, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def deploy_fund_me():
    account = get_account()
    # if we're on rinkeby network, use development address wallet , otherwise, deploy mock locally
    # mock == out own price feed data

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]

    else:
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address
        print("Mock Deployed!!")

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get(
            "verify"
        ),  # go to active network then verify publicity
    )  # deploying contract will change state on the chain so we need the address to collect gas and for ownership
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
