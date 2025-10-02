# hyperliquid-vault-withdrawal

1. Get vault address from the vault's web page and put it into the `VAULT` variable in `main.py`

2. Get wallet private key from your wallet (e.g. MetaMask) and put it into the `WALLET` variable in `main.py`

3. Run these commands in terminal one by one

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install eth-account hyperliquid-python-sdk
    python3 main.py
    deactivate
    ```

    If `python3` and `pip3` are not found, try `python` and `pip` instead.

    If the result is `{'status': 'err', 'response': 'Insufficient vault equity for withdrawal'}`, maybe your vault equity fluctuated more than 1 cent down between the steps, so just try again.

    If the result is `{'status': 'ok', 'response': {'type': 'default'}}`, then you have successfully withdrawn your vault equity to your margin balance, congrats!

4. Optionally you can withdraw your margin balance into your Arbitrum wallet via [DeBridge](https://app.debridge.finance/?address=&inputChain=999999&outputChain=42161&inputCurrency=0xaf88d065e77c8cc2239327c5edb3a432268e5831&outputCurrency=0xaf88d065e77c8cc2239327c5edb3a432268e5831&dlnMode=simple).
