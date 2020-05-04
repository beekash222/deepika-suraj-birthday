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
    if select == "Deepu":
        x ="Happy birthday Rabbit, hope you liked it I know ur love for coding,hence thought of doing thissome people are meant to be in ur life and u r the one for me thnq for being there..love you laods,,,enjoy ur day  keeping smiling , loving ,enjoying and always be happy may god fulfils ur all dreams and accept your prayer nd grant ur all wishes looking forward for a bright and happy future together thnq for not ruining my surprise this time ..loads of love for that P.S. I love you" 
    elif select == "Neha":
        x = "Happy Birthday Suraj,May God bless you!!""\n""Jaldi se tere aur Deepu ki shaddi ho i want to see fusion marriage(odia+haryanvi)""\n""Bhagwan tjhe bahut sare bache de ..aur unki parwarish k lia bahut sare paise bhi de"
    elif select == "Mahak":
       x = "Happy Birthday Suraj,May God bless you!!""\n""Jaldi se tere aur Deepu ki shaddi ho i want to see fusion marriage(odia+haryanvi)""\n""Bhagwan tjhe bahut sare bache de ..aur unki parwarish k lia bahut sare paise bhi de"
    elif select == "Swati":
       x = "Happy Birthday Suraj,May God bless you!!""\n""Jaldi se tere aur Deepu ki shaddi ho i want to see fusion marriage(odia+haryanvi)""\n""Bhagwan tjhe bahut sare bache de ..aur unki parwarish k lia bahut sare paise bhi de"        
    elif select == "Vinisha":
       x = "Happy Birthday Suraj,May God bless you!!""\n""Jaldi se tere aur Deepu ki shaddi ho i want to see fusion marriage(odia+haryanvi)""\n""Bhagwan tjhe bahut sare bache de ..aur unki parwarish k lia bahut sare paise bhi de"        
    elif select == "Shivam":
       x = "Happy Birthday Suraj,May God bless you!!""\n""Jaldi se tere aur Deepu ki shaddi ho i want to see fusion marriage(odia+haryanvi)""\n""Bhagwan tjhe bahut sare bache de ..aur unki parwarish k lia bahut sare paise bhi de"        
    elif select == "Rohan":
       x = "Happy Birthday Suraj,May God bless you!!""\n""Jaldi se tere aur Deepu ki shaddi ho i want to see fusion marriage(odia+haryanvi)""\n""Bhagwan tjhe bahut sare bache de ..aur unki parwarish k lia bahut sare paise bhi de"        
    elif select == "Anwesha":
       x = "Happy Birthday Suraj,May God bless you!!""\n""Jaldi se tere aur Deepu ki shaddi ho i want to see fusion marriage(odia+haryanvi)""\n""Bhagwan tjhe bahut sare bache de ..aur unki parwarish k lia bahut sare paise bhi de"        
    elif select == "Manjeet":
       x = "Happy Birthday Suraj,May God bless you!!""\n""Jaldi se tere aur Deepu ki shaddi ho i want to see fusion marriage(odia+haryanvi)""\n""Bhagwan tjhe bahut sare bache de ..aur unki parwarish k lia bahut sare paise bhi de"        
    elif select == "Priyabart":
       x = "Happy Birthday Suraj,May God bless you!!""\n""Jaldi se tere aur Deepu ki shaddi ho i want to see fusion marriage(odia+haryanvi)""\n""Bhagwan tjhe bahut sare bache de ..aur unki parwarish k lia bahut sare paise bhi de"        
    elif select == "Debu":    
       x = "Happy Birthday Suraj,May God bless you!!""\n""Jaldi se tere aur Deepu ki shaddi ho i want to see fusion marriage(odia+haryanvi)""\n""Bhagwan tjhe bahut sare bache de ..aur unki parwarish k lia bahut sare paise bhi de"        
    return x

@app.route('/predict2',methods=['GET','POST'])
def predict2():
        return render_template('main.html')


@app.route('/predict3',methods=['GET','POST'])
def predict3():
    if 'Scratch_Me1' in request.form:
        x = "You won lots of kissess & hugs and free shopping..."
        return x
    if 'Scratch_Me2' in request.form:
        x = "You won dinner date..."
        return x
    if 'Scratch_Me3' in request.form:
        x = "You won a trip with me"
        return x
    
    #return render_template('main.html', prediction_text1= x)
   
if __name__=="__main__":
 #   port=int(os.environ.get('PORT',5000))
     app.run()