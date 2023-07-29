from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/logClick', methods=['POST'])
def log_click():
    try:
        click_info = request.get_json()
        clicked_time = click_info['clickedTime']
        visitor_ip = request.remote_addr
        log_message = f"Clicked Time: {clicked_time}, Visitor IP: {visitor_ip}\n"
        
        with open('click.log', 'a') as log_file:
            log_file.write(log_message)
        
        print('Click data received:', click_info)
        return jsonify({'message': 'Click data recorded successfully'}), 200
    except Exception as e:
        print('Error:', str(e))
        return jsonify({'message': 'Error recording click data'}), 500

@app.route('/logEntry', methods=['POST'])
def log_entry():
    try:
        entry_info = request.get_json()
        entry_time = entry_info['entryTime']
        visitor_ip = request.remote_addr
        log_message = f"Entry Time: {entry_time}, Visitor IP: {visitor_ip}\n"
        
        with open('entry.log', 'a') as log_file:
            log_file.write(log_message)
        
        print('Entry data received:', entry_info)
        return jsonify({'message': 'Entry data recorded successfully'}), 200
    except Exception as e:
        print('Error:', str(e))
        return jsonify({'message': 'Error recording entry data'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)