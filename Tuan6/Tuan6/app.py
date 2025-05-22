from flask import Flask, render_template, request, send_file, redirect, flash
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def aes_encrypt(file_path, key, output_path):
    key = key.encode('utf-8')
    key = key.ljust(16, b'0')[:16]  # Đảm bảo key dài đúng 16 byte
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(file_path, 'rb') as f:
        data = f.read()
    padded_data = pad(data, AES.block_size)
    encrypted_data = iv + cipher.encrypt(padded_data)

    with open(output_path, 'wb') as f:
        f.write(encrypted_data)

def aes_decrypt(file_path, key, output_path):
    key = key.encode('utf-8')
    key = key.ljust(16, b'0')[:16]  # Đảm bảo key dài đúng 16 byte

    with open(file_path, 'rb') as f:
        iv = f.read(16)
        encrypted_data = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)
    try:
        unpadded_data = unpad(decrypted_data, AES.block_size)
    except ValueError:
        raise ValueError("Invalid key or corrupted file.")
    with open(output_path, 'wb') as f:
        f.write(unpadded_data)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        key = request.form.get('key')
        operation = request.form.get('operation')

        if not file or not key or len(key) < 8:
            flash('Vui lòng tải tệp và nhập khóa (ít nhất 8 ký tự).')
            return redirect(request.url)

        input_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(input_path)

        output_filename = f"{operation}ed_{file.filename}"
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)

        try:
            if operation == 'encrypt':
                aes_encrypt(input_path, key, output_path)
            elif operation == 'decrypt':
                aes_decrypt(input_path, key, output_path)
        except Exception as e:
            flash(str(e))
            return redirect(request.url)

        return send_file(output_path, as_attachment=True, download_name=output_filename)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
