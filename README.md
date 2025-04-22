# 🩺 Doctor Dashboard - AI Disease Prediction

Welcome to the **Doctor Dashboard**, a Flask-based web application for disease prediction using AI models. It supports predictions for:

- Lung Cancer (Image-based)
- Breast Cancer (Image-based)
- Diabetes (CSV/Text input-based)

---

## 🚀 Getting Started

### ✅ 1. Prerequisites
Make sure these tools are installed:

- Python 3.7+
- Git
- pip (Python package installer)

### ✅ 2. Clone the Repository
```bash
git clone https://github.com/shetalkothari/doctor_dashboard.git
cd doctor_dashboard
```

### ✅ 3. Create a Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### ✅ 4. Install Dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:
```bash
pip install flask pandas matplotlib
```
(Add more packages if used)

### ✅ 5. Prepare the Folder Structure
Ensure the following structure exists:

```
doctor_dashboard/
├── static/
├── templates/
├── uploads/             # Create manually if missing
├── app.py               # Main Flask file
├── requirements.txt
```

Create `uploads` folder if missing:
```bash
mkdir uploads
```

### ✅ 6. Run the Application
```bash
python app.py
```

Visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

### ✅ 7. Stop the Server
Use `Ctrl + C` in terminal to stop the app.

---

## 📁 Features
- Clean and interactive dashboard
- Real-time prediction feedback
- Multi-image upload for lung and breast cancer
- CSV-based input for diabetes
- Graphs & insights for predictions

---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License
MIT License - free to use, modify, and distribute.

---

**Made with ❤️ for medical professionals**

