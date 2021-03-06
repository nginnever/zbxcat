import xcat.zcash
import xcat.bitcoin
from xcat import *

htlcTrade = Trade()
print("Starting test of xcat...")

def get_initiator_addresses():
    return {'bitcoin': 'myfFr5twPYNwgeXyjCmGcrzXtCmfmWXKYp', 'zcash': 'tmFRXyju7ANM7A9mg75ZjyhFW1UJEhUPwfQ'}

def get_fulfiller_addresses():
    return {'bitcoin': 'mrQzUGU1dwsWRx5gsKKSDPNtrsP65vCA3Z', 'zcash': 'tmTjZSg4pX2Us6V5HttiwFZwj464fD2ZgpY'}

def initiate(trade):
    # Get amounts
    amounts = {"sell": {"currency": "bitcoin", "amount": "0.5"}, "buy": {"currency": "zcash", "amount": "1.12"}}
    sell = amounts['sell']
    buy = amounts['buy']
    sell_currency = sell['currency']
    buy_currency = buy['currency']
    # Get addresses
    init_addrs = get_initiator_addresses()
    sell['initiator'] = init_addrs[sell_currency]
    buy['initiator'] = init_addrs[buy_currency]
    fulfill_addrs = get_fulfiller_addresses()
    sell['fulfiller'] = fulfill_addrs[sell_currency]
    buy['fulfiller'] = fulfill_addrs[buy_currency]
    # initializing contract classes with addresses, currencies, and amounts
    trade.sell = Contract(sell)
    trade.buy = Contract(buy)
    print(trade.sell.__dict__)
    print(trade.buy.__dict__)

    secret = generate_password()
    print("Generating secret to lock funds:", secret)
    save_secret(secret)
    # TODO: Implement locktimes and mock block passage of time
    sell_locktime = 2
    buy_locktime = 4 # Must be more than first tx

    create_sell_p2sh(trade, secret, sell_locktime)
    txid = fund_sell_contract(trade)
    print("Sent")
    create_buy_p2sh(trade, secret, buy_locktime)

def fulfill(trade):
    buy = trade.buy
    sell = trade.sell
    buy_p2sh_balance = check_p2sh(buy.currency, buy.p2sh)
    sell_p2sh_balance = check_p2sh(sell.currency, sell.p2sh)

    if buy_p2sh_balance == 0:
        print("Buy amt:", buy.amount)
        txid = fund_buy_contract(trade)
        print("Fund tx txid:", txid)
    else:
        raise ValueError("Sell p2sh not funded, buyer cannot redeem")

def redeem_one(trade):
    buy = trade.buy
    if trade.sell.get_status() == 'redeemed':
        raise RuntimeError("Sell contract status was already redeemed before seller could redeem buyer's tx")
    else:
        secret = get_secret()
        print("GETTING SECRET IN TEST:", secret)
        tx_type, txid = redeem_p2sh(trade.buy, secret)
        print("\nTX Type", tx_type)
        setattr(trade.buy, tx_type, txid)
        save(trade)
        print("You have redeemed {0} {1}!".format(buy.amount, buy.currency))

def redeem_two(trade):
    if trade.sell.get_status() == 'redeemed':
        raise RuntimeError("Sell contract was redeemed before buyer could retrieve funds")
    elif trade.buy.get_status() == 'refunded':
        print("buy was refunded to buyer")
    else:
        # Buy contract is where seller disclosed secret in redeeming
        if trade.buy.currency == 'bitcoin':
            secret = bXcat.parse_secret(trade.buy.redeem_tx)
        else:
            secret = zXcat.parse_secret(trade.buy.redeem_tx)
        print("Found secret in seller's redeem tx", secret)
        redeem_tx = redeem_p2sh(trade.sell, secret)
        setattr(trade.sell, 'redeem_tx', redeem_tx)
        save(trade)

def generate_blocks(num):
    bXcat.generate(num)
    zXcat.generate(num)

initiate(htlcTrade)
fulfill(htlcTrade)

generate_blocks(6)

redeem_one(htlcTrade)
redeem_two(htlcTrade)

# addr = CBitcoinAddress('tmFRXyju7ANM7A9mg75ZjyhFW1UJEhUPwfQ')
# print(addr)
# # print(b2x('tmFRXyju7ANM7A9mg75ZjyhFW1UJEhUPwfQ'))
# print(b2x(addr))
