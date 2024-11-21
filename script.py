from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    user_message = request.json.get('message')
    response = get_ollama_response(user_message)
    return jsonify({'reply': response})

def get_ollama_response(user_message):
    url = "https://api.ollama.com/v1/query"  # Replace with Ollama's actual API endpoint
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",  # Replace with your Ollama API key
        "Content-Type": "application/json"
    }
    data = {"input": user_message}
    response = requests.post(url, json=data, headers=headers)
    response_data = response.json()
    return response_data.get("response", "Sorry, I didn't get that.")

if __name__ == '__main__':
    app.run(debug=True)
