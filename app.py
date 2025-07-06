from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    name = request.form.get('name')
    message = request.form.get('message')
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open('messages.txt', 'a', encoding='utf-8') as f:
        f.write(f"{now} - {name}: {message}\n")
    return render_template('thankyou.html', name=name)

@app.route('/messages')
def messages():
    try:
        with open('messages.txt', 'r', encoding='utf-8') as f:
            all_messages = f.readlines()
    except:
        all_messages = []
    return render_template('view_messages.html', messages=all_messages)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/secret', methods=['GET', 'POST'])
def secret():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == '17041006':
            return render_template('special.html')
        else:
            return "<h3>❌ Parol noto‘g‘ri!</h3><a href='/secret'>Ortga</a>"
    return render_template('secret.html')

@app.route('/marjona')
def marjona():
    return render_template('marjona.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)