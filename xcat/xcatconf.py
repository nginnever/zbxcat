# Replace these with your own addresses and trade amts to pass info in through config flag
ADDRS = {
    'regtest': {
        "initiator": {
            "bitcoin": "mvc56qCEVj6p57xZ5URNC3v7qbatudHQ9b",
            "zcash": "tmTF7LMLjvEsGdcepWPUsh4vgJNrKMWwEyc"
        },
        "fulfiller": {
            "bitcoin": "moRt56gJQGDNK46Y6fYy2HbooKnQXrTGDN",
            "zcash": "tmK3rGzHDqa78MCwEicx9VcY9ZWX9gCF2nd"
        },
        "amounts": {'buy': {'currency': 'zcash', 'amount': 0.02}, 'sell': {'currency': 'bitcoin', 'amount': 0.01}}
    },
    'testnet': {
        "initiator": {
            "bitcoin": "mvc56qCEVj6p57xZ5URNC3v7qbatudHQ9b",
            "zcash": "tmTF7LMLjvEsGdcepWPUsh4vgJNrKMWwEyc"
        },
        "fulfiller": {
            "bitcoin": "mn2boR7rYq9DaAWWrVN5MazHKFyf7UhdyU",
            "zcash": "tmErB22A1G74aq32aAh5AoqgQSJsAAAdT2p"
        },
        "amounts": {'buy': {'currency': 'zcash', 'amount': 0.02}, 'sell': {'currency': 'bitcoin', 'amount': 0.01}}
    }
}

NETWORK = 'testnet'

# Pass regtest trade data in on command line
# '[{"initiator": {"bitcoin": "mvc56qCEVj6p57xZ5URNC3v7qbatudHQ9b", "zcash": "tmTF7LMLjvEsGdcepWPUsh4vgJNrKMWwEyc"}, "fulfiller": {"bitcoin": "moRt56gJQGDNK46Y6fYy2HbooKnQXrTGDN", "zcash": "tmK3rGzHDqa78MCwEicx9VcY9ZWX9gCF2nd"}, "amounts": {"buy": {"currency": "zcash", "amount": 0.02}, "sell": {"currency": "bitcoin", "amount": 0.01}}}]'
