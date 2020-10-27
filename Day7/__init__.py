import json
import flask
app = flask.Flask("shop")
#from .models import products

products=[
    {
        "id":1,
        "name":"Macbook",
        "price":1000.99,
        "stock_quantity":3,
        "category":"technology"
    },
    {
        "id":2,
        "name":"HeadPhone",
        "price":99.99,
        "stock_quantity":5,
        "category":"technology"
    },
    {
        "id":3,
        "name":"meet",
        "price":25.5,
        "stock_quantity":2,
        "category":"food"
    },
    {
        "id":4,
        "name":"Coca Cola",
        "price":3.99,
        "stock_quantity":4,
        "category":"food"
    },
]


#for home page
@app.route("/")
def home():
    return flask.render_template("shop.html",products=products)
#for all products
@app.route('/products')
def indexproducts():
    return flask.render_template("products.html", products=products)
#for a spasific product
@app.route('/product/<int:number>')
def index(number):
    return flask.render_template("product.html", products=products,number=number)
#for a spasific product
@app.route('/search/by-category/<string:category>')
def indexcategory(category):
    return flask.render_template("category.html",products=products,category=category)
app.run(debug=True)# yes for debug
