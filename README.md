# GPA Calculation Module 🎓

A Flask-based web application designed to calculate **SGPA and CGPA** by taking subject-wise marks and credit hours.  
This project is built as a **learning-focused academic module**, suitable for university students and beginner Flask developers.

---

## 📌 Features

- Calculate **SGPA (Semester Grade Point Average)**
- Calculate **CGPA (Cumulative Grade Point Average)**
- Dynamic handling of multiple subjects
- Clean separation of logic (calculation, models, routes)
- Simple and beginner-friendly Flask architecture
- Basic authentication structure (extensible)

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **Flask-SQLAlchemy**
- **HTML / CSS**
- **SQLite / PostgreSQL (configurable)**

---

## 📂 Project Structure

```

GPA-Calculation-Module/
│
├── main.py              # Application entry point
├── calculation.py       # GPA calculation logic
├── auth.py              # Authentication routes
├── models.py            # Database models
├── templates/            # HTML templates
    ├── GPA.html
    ├── dashboard.html
    ├── index.html
    ├── login.html
    ├── signup.html
├── static/
│   └── css/              # Stylesheets
        └── style.css
├── pyproject.toml
└── README.md

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Alihassandev1/GPA-Calculation-Module.git
cd GPA-Calculation-Module
````

### 2️⃣ Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On Linux / macOS
venv\Scripts\activate         # On Windows
```

# No need to install dependencies manually if you use uv

## ▶️ Running the Application

```bash
uv run main.py
```

Then open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 📐 GPA Calculation Logic

* GPA is calculated using **standard academic grading formulas**
* Each subject contributes based on its **credit hours**
* Final GPA is computed as:

```
GPA = (Σ (Grade Point × Credit Hours)) / (Σ Credit Hours)
```

📖 Reference:

* GPA definition (Wikipedia): [https://en.wikipedia.org/wiki/Grade_point_average](https://en.wikipedia.org/wiki/Grade_point_average)

---

## 🎯 Purpose of This Project

* Academic practice project
* Learning Flask application structure
* Understanding modular Python design
* Useful for CS students and beginners

---

## 🚀 Future Improvements

* PDF / CSV export of GPA results
* Role-based access (Admin / Student)
* REST API support

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

GitHub contribution guide:
[https://docs.github.com/en/get-started/quickstart/contributing-to-projects](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)


---

## 👤 Author

**Ali Hassan**
BS Computer Science Student
GitHub: [https://github.com/Alihassandev1](https://github.com/Alihassandev1)

