from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
    return render_template('./main.html')

@app.route('/klinh',methods=['GET', 'POST'])
def more():
    return render_template('./more.html')

@app.route('/toi-yeu-em',methods=['GET', 'POST'])
def hope():
    return render_template('./hope.html')

if __name__ == '__main__':
    app.run(debug=True)