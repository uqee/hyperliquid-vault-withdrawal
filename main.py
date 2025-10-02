from eth_account import Account
from hyperliquid.exchange import Exchange
from hyperliquid.info import Info

VAULT = "0xdfc24b077bc1425ad1dea75bcb6f8158e10df303" # this one is HLP, replace with your vault address
WALLET = "" # put your private key

account = Account.from_key(WALLET)
exchange = Exchange(account)
info = Info(skip_ws=True)

input("Press Enter to get balances...")

spot_user_state = info.spot_user_state(account.address)
print(spot_user_state)

user_state = info.user_state(account.address)
print(user_state)

user_vault_equities = info.user_vault_equities(account.address)
print(user_vault_equities)

input("Press Enter to withdraw from the vault...")

equity = 10000 * int(100 * float(user_vault_equities[0]['equity'])) # to micro USDC int
print(equity)

result = exchange.vault_usd_transfer(VAULT, False, equity)
print(result)

input("Press Enter to get updated balances...")

spot_user_state = info.spot_user_state(account.address)
print(spot_user_state)

user_state = info.user_state(account.address)
print(user_state)

user_vault_equities = info.user_vault_equities(account.address)
print(user_vault_equities)
