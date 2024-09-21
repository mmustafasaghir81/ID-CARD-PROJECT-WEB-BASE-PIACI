# 📇 ID Card Generation Project

## 🌟 Overview
Welcome to the **ID Card Generation Project**! This web application allows users to generate personalized ID cards by providing their details such as name, roll number, campus, and more. Users can upload a profile photo and download the generated ID card in PDF format. The card also includes a barcode for authentication.

## ✨ Key Features
- **Dynamic Input**: Enter user data through a form to dynamically generate the ID card.
- **Photo Upload**: Upload a profile picture to be displayed on the ID card.
- **PDF Export**: Download the ID card in PDF format.
- **Barcode**: Each ID card comes with a barcode for quick identification.
- **Responsive Design**: Works seamlessly across different devices and screen sizes.

---

## 🛠️ Technologies Used
- **Flask**: Python web framework.
- **HTML5 & CSS3**: For structuring and styling the front-end.
- **Bootstrap**: A responsive CSS framework.
- **JavaScript**: For additional interactivity and PDF generation using `html2pdf.js`.
- **Jinja2**: Templating engine used with Flask for rendering dynamic HTML.

---

## 📋 Prerequisites

Before running the project, ensure you have the following installed:
- **Python 3.x**: [Download and install from python.org](https://www.python.org/downloads/).
- **Flask**: Install Flask via pip using the command `pip install flask`.

---

## 🚀 Getting Started

### 🛠️ Installation Steps

Follow the steps below to set up and run the project locally.

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your_username/id_card_project.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd id_card_project
    ```

3. **Install Required Dependencies**:
    Install all dependencies from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4. **Create Static Folders**:
    Create the necessary folders inside the `static` directory:
    ```bash
    mkdir static/img static/uploads
    ```

5. **Run the Application**:
    Start the Flask development server with the following command:
    ```bash
    python app.py
    ```

6. **Open in Browser**:
    Once the server is running, open your browser and visit:
    ```bash
    http://127.0.0.1:5000/
    ```

---
## 📂 Project Folder Structure

```bash
id_card_project/
├── static/
│   ├── img/
│   │   └── Barcode.jpg        # Barcode image for ID card
│   │   └── icard-background.jpg  # Background image for ID card
│   ├── uploads/               # Stores uploaded profile photos
├── templates/
│   ├── id_card.html           # Template for generated ID card
│   └── id_form.html           # Template for the form input
├── app.py                     # Main Flask application file
└── README.md                  # Project documentation
# 📇 ID Card Generation Project
```
---

# 📁 Static Folder Explanation

- **static/img/**: This folder stores all static images, including the **ID card background** and the **barcode image**.
- **static/uploads/**: This folder will hold the **uploaded profile photos** from users.

**Note**: Make sure to create the `static/` folder with the above sub-folders before running the project. The **img** folder should contain required images like the **ID card background**, and the **uploads** folder will handle dynamically uploaded images.


# 📝 Template Explanation

- **id_form.html**: This is the form where users enter their details like **name**, **role**, **center**, **batch ID**, and upload their **profile photo**.
- **id_card.html**: This template generates the final ID card, displaying the user's information dynamically, along with the **barcode** and uploaded photo.

# ⚡ How to Use the Application

1. Open the application on your local server.
2. Fill in the form with your details: **Name**, **Father's Name**, **ID number**, **Roll number**, **Campus**, **Batch ID**, etc.
3. Upload a profile photo to be included on the ID card.
4. Click **Submit** to generate the ID card.
5. Once the card is generated, you can download it as a PDF by clicking the **"Create PDF"** button.

# 📦 Dependencies

The project uses the following Python packages, which can be installed via pip:

- **Flask**: For serving the web pages.
- **html2pdf.js**: For generating the downloadable PDF file of the ID card.

# 📑 Useful Links

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [html2pdf.js Documentation](https://github.com/ephremme/html2pdf.js)

# 📧 Contact

If you have any questions or suggestions, feel free to reach out:

- **GitHub**: mmustafasaghir81
- **Email**: akifsaghirai@gmail.com

# 🔗 Useful Links

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Official Website](https://www.python.org/)
- [html2pdf.js GitHub](https://github.com/ephremme/html2pdf.js)

# 🎉 Screenshots

Example of a generated ID card with profile photo, barcode, and user details.

