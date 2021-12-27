import os
from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = 'f1223cfw2344e595e55d58fae30954sfgf02079dbfa9281' 

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', page='home')



# Run the app
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)