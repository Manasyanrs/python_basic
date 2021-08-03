data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

for keys, values in data.items():
    print(keys, ":", values)

data["ETH"]["total_diff"] = 100
print("\nЗначение total_diff в ETH после замены = {}".format(data["ETH"]["total_diff"]))

new_data = {}
for element in data["tokens"]:
    new_data.update(element)

data["tokens"] = new_data

data["tokens"]["fst_token_info"]["name"] = "doge"
print("\nЗначение name в tokens после замены = {}".format(data["tokens"]["fst_token_info"]["name"]))

data["ETH"]["total_out"] = data["tokens"].pop("total_out")
print("\nЗначение total_out в ETH после замены = {}".format(data["ETH"]["total_out"]))

data["tokens"]["fst_token_info"]["total_price"] = data["tokens"]["fst_token_info"].pop("price")
print("\nПосле замены лкюча total_price в tokens = {}".format(data["tokens"]["fst_token_info"]["total_price"]))
