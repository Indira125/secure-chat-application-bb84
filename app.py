from flask import Flask, render_template, request
from bb84 import generate_bits, generate_bases, generate_key, detect_eavesdropping
from crypto_utils import hash_key, encrypt_message, decrypt_message

app = Flask(__name__)

shared_key = None
stored_nonce = None
stored_tag = None
stored_ciphertext = ""   # 🔥 STORE ENCRYPTED MESSAGE

@app.route("/", methods=["GET", "POST"])
def index():
    global shared_key, stored_nonce, stored_tag, stored_ciphertext

    status = ""
    decrypted_output = ""

    if request.method == "POST":

        # 1️⃣ Generate Quantum Key
        if "generate" in request.form:
            n = 100
            alice_bits = generate_bits(n)
            alice_bases = generate_bases(n)
            bob_bases = generate_bases(n)

            alice_key = generate_key(alice_bits, alice_bases, bob_bases)
            bob_key = generate_key(alice_bits, alice_bases, bob_bases)

            if detect_eavesdropping(alice_key, bob_key):
                status = "❌ Eavesdropping Detected! Secure session aborted."
                shared_key = None
            else:
                shared_key = hash_key(alice_key)
                status = "✅ Secure Quantum Channel Established"

        # 2️⃣ Encrypt Message
        if "encrypt" in request.form and shared_key:
            message = request.form["plain_message"]
            nonce, ciphertext, tag = encrypt_message(message, shared_key)

            stored_ciphertext = ciphertext.hex()   # 🔐 SAVE IT
            stored_nonce = nonce
            stored_tag = tag

        # 3️⃣ Decrypt Message (DO NOT ERASE ENCRYPTED)
        if "decrypt" in request.form and shared_key:
            try:
                encrypted_hex = request.form["encrypted_message"]
                ciphertext = bytes.fromhex(encrypted_hex)

                decrypted_output = decrypt_message(
                    stored_nonce,
                    ciphertext,
                    stored_tag,
                    shared_key
                )
            except:
                decrypted_output = "❌ Invalid encrypted data"

        # 4️⃣ Reset Session
        if "reset" in request.form:
            shared_key = None
            stored_nonce = None
            stored_tag = None
            stored_ciphertext = ""
            status = "🔄 Session reset. Ready for new quantum key generation."

    return render_template(
        "index.html",
        status=status,
        encrypted=stored_ciphertext,   # ✅ ALWAYS SHOW
        decrypted=decrypted_output
    )

if __name__ == "__main__":
    app.run(debug=True)
