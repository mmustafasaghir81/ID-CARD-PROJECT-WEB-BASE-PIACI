from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configuration for file uploads
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB maximum upload size

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        father_name = request.form['father_name']
        id_number = request.form['id_number']
        roll_number = request.form['roll_number']
        center = request.form['center']  # Updated field name
        city = request.form['city']  # New field
        campus = request.form['campus']  # New field
        batch_id = request.form['batch_id']

        # Handle file upload
        if 'photo' not in request.files:
            return redirect(request.url)
        photo = request.files['photo']
        if photo.filename == '':
            return redirect(request.url)
        if photo:
            filename = secure_filename(photo.filename)
            photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            photo.save(photo_path)

            # Render ID card page
            return render_template('id_card.html',
                                  name=name,
                                  father_name=father_name,
                                  id_number=id_number,
                                  roll_number=roll_number,
                                  center=center,  # Updated field
                                  city=city,  # New field
                                  campus=campus,  # New field
                                  batch_id=batch_id,
                                  photo=filename)

    return render_template('id_form.html')

if __name__ == '__main__':
    app.run(debug=True)
