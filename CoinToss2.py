import CoinClass as c

def show_coin_status(obj):
    print(f"This side is up: {obj.get_sideup()}")

def flip(obj):
    obj.toss()

mycoin = c.Coin()
show_coin_status(mycoin)
flip(mycoin)
show_coin_status