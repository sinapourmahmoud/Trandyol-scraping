from database import Database
from bot import Bot
from trandyol import Trandyol


def main():
    shop=Trandyol()
    shop.get_items('shoes','https://www.trendyol.com/kadin-ayakkabi-x-g1-c114')
    shop.get_items('bag','https://www.trendyol.com/kadin-canta-x-g1-c117')
    shop.get_items('bag','https://www.trendyol.com/erkek-canta-x-g2-c117')
    shop.get_items('shoes','https://www.trendyol.com/erkek-ayakkabi-x-g2-c114')
    print(Trandyol.items)
if __name__=="__main__":
    main()

