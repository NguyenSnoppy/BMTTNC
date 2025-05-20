from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import Vigenere_cipher
app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#Vigenere
vigenere_cipher = Vigenere_cipher()
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    text = data['plain_text']
    key = data['key']
    return jsonify({'encrypted_text': vigenere_cipher.encrypt_text(text, key)})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    text = data['cipher_text']
    key = data['key']
    return jsonify({'decrypted_text': vigenere_cipher.decrypt_text(text, key)})

# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)