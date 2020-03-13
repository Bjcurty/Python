# Flask is a class with good website making capeabilities
from flask import Flask

# creating app variable
app=Flask(__name__)

# 
@app.route('/')
def home():
    return "Website content goes here!"

if __name__=="__main__":
    app.run(debug=True)
