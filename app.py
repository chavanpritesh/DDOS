from flask import Flask, render_template, request
from utils.detector import detect_attack
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/tool', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        packet_rate = float(request.form['packet_rate'])
        src_ip_count = int(request.form['src_ip_count'])
        dst_port = int(request.form['dst_port'])
        protocol_str = request.form['protocol']

        result = detect_attack(packet_rate, src_ip_count, dst_port, protocol_str)

        # Log the detection
        with open('logs/logs.csv', mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                packet_rate, src_ip_count, dst_port,
                protocol_str, result
            ])

    return render_template('tool.html', result=result)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/dashboard')
def dashboard():
    with open('logs/logs.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        logs = list(reader)

    total_logs = len(logs)
    ddos_count = sum(1 for log in logs if log['result'] == '🚨 DDoS Attack Detected!')
    normal_count = sum(1 for log in logs if log['result'] == '✅ Normal Traffic')

    return render_template('dashboard.html', logs=logs,
                           ddos_count=ddos_count,
                           normal_count=normal_count,
                           total_logs=total_logs)

if __name__ == '__main__':
    app.run(debug=True)
