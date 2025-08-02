from database import Database
from bot import Bot
from trandyol import Trandyol
from flask import Flask, render_template


def main():
    app=Flask(__name__,template_folder='templates')
#     shop=Trandyol()
#     shop.get_items('shoes','https://www.trendyol.com/kadin-ayakkabi-x-g1-c114')
#     shop.get_items('bag','https://www.trendyol.com/kadin-canta-x-g1-c117')
#     shop.get_items('bag','https://www.trendyol.com/erkek-canta-x-g2-c117')
#     shop.get_items('shoes','https://www.trendyol.com/erkek-ayakkabi-x-g2-c114')
#     print(Trandyol.items)
    db=Database()
#     db.execute("""
#         CREATE TABLE IF NOT EXISTS products (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             company TEXT,
#             link TEXT ,
#             rate REAL,
#             product TEXT,
#             category TEXT,
#             price REAL
#         )
#     """)
#     db.executemany("""
#     INSERT INTO products (name,company,link,rate,product,category,price) VALUES(?,?,?,?,?,?,?)
# """,Trandyol.items)
    from routes import all_routes
    all_routes(app,db)
    return app

