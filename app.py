from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/caesar_process', methods=['POST'])
def caesar_process():
    data = request.get_json()
    text = data['text']
    operation = data['operation']
    key = int(data.get('key', 3))

    if operation == 'encrypt':
        result = caesar_encrypt(text, key)
    elif operation == 'decrypt':
        result = caesar_decrypt(text, key)
    else:
        return jsonify({'error': 'Invalid operation'})

    return jsonify({'result': result})

def caesar_encrypt(plain_text, key):
    cipher_text = ''
    for char in plain_text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                shifted = (shifted - ord('a')) % 26 + ord('a')
            elif char.isupper():
                shifted = (shifted - ord('A')) % 26 + ord('A')
            cipher_text += chr(shifted)
        else:
            cipher_text += char
    return cipher_text

def caesar_decrypt(cipher_text, key):
    return caesar_encrypt(cipher_text, -key)

if __name__ == '__main__':
    app.run(debug=True)
