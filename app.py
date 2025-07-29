from flask import Flask, render_template, request, redirect, url_for, flash
import os
import random
import string
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.urandom(24) 

DOWNLOAD_FOLDER = os.path.join(os.path.expanduser('~'), 'Downloads')

PIN = ''.join(random.choices(string.digits, k=4))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_pin = request.form.get('pin')
        if user_pin != PIN:
            flash('❌ Invalid PIN, please try again.', 'error')
            return redirect(url_for('index'))
        else:
            return redirect(url_for('upload'))

    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        user_pin = request.form.get('pin')
        if user_pin != PIN:
            flash('❌ Invalid PIN, please try again.', 'error')
            return redirect(url_for('index'))

        file = request.files.get('file')
        if not file or file.filename == '':
            flash('❌ No file selected.', 'error')
            return redirect(url_for('upload'))

        filename = secure_filename(file.filename)
        save_path = os.path.join(DOWNLOAD_FOLDER, filename)
        file.save(save_path)
        flash(f'✅ File "{filename}" saved successfully to Downloads.', 'success')
        return redirect(url_for('upload'))

    return render_template('upload.html', pin=PIN)


def run_server():
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    print(f"[Pivvo] Your session PIN is: {PIN}")
    run_server()
