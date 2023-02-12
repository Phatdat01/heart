from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
    return render_template('./main.html')

@app.route('/klinh',methods=['GET', 'POST'])
def more():
    return render_template('./more.html')

if __name__ == '__main__':
    app.run(debug=True)