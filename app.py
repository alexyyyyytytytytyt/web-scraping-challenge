from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrapy


app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():
    
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars, dfe="Mission on Mars")


@app.route("/scrape")
def scrape():
    
    
    # Run the scrape function
    
    
    mars = mongo.db.mars
    mars_data = scrapy.scrape_info()
    mars_data = scrapy.scrape_marsFacts()
    mars_data = scrapy.mars_hemispheres()
    
    
    mars.update_one({}, {"$set": mars_data}, upsert=True)
    return redirect("/", code=302)




if __name__ == "__main__":
    app.run(debug=True)