import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/whatsapp-bot', methods=['POST'])
def bot():
    data = request.json
    incoming_msg = data.get('query', '') 

    # અહીં તમે જે મેસેજ સેટ કરશો તે સામેવાળાને જશે
    ai_response = f"નમસ્તે! આ મારો ઓટોમેટેડ રિપ્લાય છે. તમે મોકલેલો મેસેજ: '{incoming_msg}'"

    return jsonify({
        "replies": [
            {
                "message": ai_response
            }
        ]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
