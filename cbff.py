import requests

# Etherscan API endpoint
API_KEY = '53XMCC9VFG8JQ8YF6Q8DRT8PFYGZMBR9C5'
API_ENDPOINT = f'https://api.etherscan.io/api?module=account&action=balance&apikey={API_KEY}&address='

# addx= open ("ethbal.txt", "a")
def get_eth_balance(address):
    # Make a request to the Etherscan API to get balance
    response = requests.get(API_ENDPOINT + address)
    balance_wei = int(response.json()['result'])
    
    # Convert balance from wei to ether
    balance_eth = balance_wei / 10**18
    
    return balance_eth

def main():
    # Read Ethereum addresses from a file (assuming one address per line)
    with open('ethereum_addresses.txt', 'r') as file:
        addresses = file.readlines()
    
    # Remove whitespace characters like `\n` at the end of each line
    addresses = [address.strip() for address in addresses]
    
    # Get and print the balance for each address
    for address in addresses:
        balance = get_eth_balance(address)
        print(f"Address: {address}, Balance: {balance} ETH")
        with open('address_balances.txt', 'a') as addx:
        # Iterate through addresses, get balance, and write to file
            addx.write(f"Address: {address}, Balance: {balance} ETH\n")

if __name__ == "__main__":
    main()
