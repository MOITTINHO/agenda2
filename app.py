from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import pywhatkit as kit

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessário para usar flash messages

events = []

def send_whatsapp_message(phone, message):
    now = datetime.now()
    kit.sendwhatmsg(phone, message, now.hour, now.minute + 1)
    

@app.route('/')
def index():
    current_month = request.args.get('month', datetime.now().month, type=int)
    current_year = request.args.get('year', datetime.now().year, type=int)
    return render_template('index.html', events=events, month=current_month, year=current_year)

@app.route('/events')
def events_page():
    return render_template('events.html', events=events)

@app.route('/add_event', methods=['POST'])
def add_event():
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    phone = request.form['phone']
    
    # Verifica se já existe um evento na mesma data
    for event in events:
        if event['date'] == date:
            flash("Já existe um evento agendado para essa data!", "error")
            return redirect(url_for('index'))

    events.append({'name': name, 'date': date, 'time': time, 'phone': phone})

   
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


