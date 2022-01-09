from flask import Flask, render_template, request
import joblib

model=joblib.load('House_price.pkl') 

#instance of an app
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('prediction.html')

@app.route('/data', methods=['POST'] )
def data():
    area= request.form.get('area')
    rooms= request.form.get('rooms')
    bathroom= request.form.get('bathroom')
    floors= request.form.get('floors')
    driveway= request.form.get('driveway')
    game_room= request.form.get('game_room')
    cellar= request.form.get('cellar')
    gas= request.form.get('gas')
    air= request.form.get('air')
    garage= request.form.get('garage')
    situation= request.form.get('situation')




    result= model.predict([[area,rooms,bathroom,floors,driveway,game_room,cellar,gas,air,garage,situation]])
    

    
    return render_template('result.html', predict=result[0])

if __name__ == '__main__':
    app.run(debug=True)