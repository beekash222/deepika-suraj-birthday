from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, flash, request, redirect, url_for
from flask import Flask, url_for, send_from_directory, request,render_template
import gunicorn

     
app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/predict',methods=['GET','POST'])
def predict():

    return render_template('main.html', prediction_text= "HAPPY Birthday!")

@app.route('/predict1',methods=['GET','POST'])
def predict1():
    select = request.form.get("cars","None")
    if select == "Beekash":
        x ='''Hello Lopy, Its been 5 days with you and i know there is no such thing as a concidence! people met for a reason but whatever it is , i am so happy and glad that i have you in my life and whatever happenes in future, i will always with you becuase i know i will never have another friend like you.
Thanks for tolerating me and my crazy habits i know its not easy but trust me i never do anything intentionally to hurt you.

Your love for your friends is an exquisite and amazing. sometimes i feel jealous that i never had any friendship like this with anyone.

Your presence makes me feel alive, you are funny and witty and i feel more connected and comfortable with you.

You always make me smile by your crazy jokes and incidents this make my sadness disappear.

Someone well said "An empty stomach need food, an empty brain needs knowledge, an empty house needs a family, and an empty heart needs love. But then, an empty life needs a friend, Thanks for filing in"


Thanks for being wih me !'''        
    return x

@app.route('/predict2',methods=['GET','POST'])
def predict2():
        return render_template('main.html')


@app.route('/predict3',methods=['GET','POST'])
def predict3():
    if 'Scratch_Me1' in request.form:
        x = "You won free shopping with me"
        return x
    if 'Scratch_Me2' in request.form:
        x = "You won a dinner date with me"
        return x
    if 'Scratch_Me3' in request.form:
        x = "You won a trip with me"
        return x
    
    #return render_template('main.html', prediction_text1= x)
   
if __name__=="__main__":
 #   port=int(os.environ.get('PORT',5000))
     app.run()
