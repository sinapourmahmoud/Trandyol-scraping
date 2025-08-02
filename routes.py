from flask import render_template, request

from database import Database


def all_routes(app,db):
    @app.route('/',methods=['GET','POST'])
    def index():
        if request.method=='POST':
            print(request.args)
            sql = 'SELECT * FROM products WHERE 1=1'
            params = []
            title = request.form.get('query', '').strip()
            categories = request.form.getlist('category')
            min_price = request.form.get('min_price', type=float)
            max_price = request.form.get('max_price', type=float)
            min_rate = request.form.get('min_rate', type=float)
            max_rate = request.form.get('max_rate', type=float)
            if title:
                sql += ' AND name LIKE ?'
                params.append(f"%{title}%")
            if categories:
                sql += f" AND category IN ({','.join(['?'] * len(categories))})"
                params.extend(categories)
            if min_price and max_price:
                sql += ' AND price >=? AND price <=?'
                params.append(min_price)
                params.append(max_price)
            if min_rate and max_rate:
                sql += ' AND rate >=? AND rate <=? '
                params.append(min_rate)
                params.append(max_rate)
            sql+=' ORDER BY price ASC, rate ASC'
            db.execute(sql, params)
            results = db.fetchall()
            return render_template('index.html',products=results,title=title,min_price=min_price,max_price=max_price,min_rate=min_rate,max_rate=max_rate)

        return render_template('index.html',products=[],title='',min_price='',max_price='',min_rate='',max_rate='')