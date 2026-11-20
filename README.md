
# ✈️ Priyansh Travel – Explore the World, Create Memories

<p align="center">
  <b>Your Journey, Our Passion!</b><br>
  A Flask-powered travel and tourism booking website designed to make travel planning simple, convenient, and enjoyable.
</p>

---

## 🌍 About the Project

**Priyansh Travel** is a web-based travel booking platform developed using Python Flask, HTML, CSS, Bootstrap, and SQLite.

The platform allows users to explore beautiful travel destinations, discover holiday packages, learn about different places, and submit travel booking requests.

The main objective of this project is to provide users with a simple and user-friendly platform for discovering destinations and planning their next adventure.

---

## ✨ Key Features

- 🏝️ **Explore Destinations** – Discover popular destinations around the world.
- 🎒 **Travel Packages** – Browse exciting travel packages.
- ⭐ **Destination Ratings** – View destination ratings and customer reviews.
- 📅 **Online Booking** – Submit travel booking requests.
- 👥 **Traveler Details** – Enter customer information and number of travelers.
- 📩 **Contact Page** – Get in touch through the contact section.
- 🗄️ **Database Integration** – Store booking information using SQLite.
- 📱 **Responsive Design** – User-friendly interface across different screen sizes.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| Flask-SQLAlchemy | Database integration |
| SQLite | Database management |
| HTML5 | Website structure |
| CSS3 | Website styling |
| Bootstrap | Responsive UI design |
| JavaScript | Frontend interactions |
| Pillow | Image processing |

---

## 📂 Project Structure

```text
priyansh_travel/
│
├── app.py
│
├── templates/
│   ├── index.html
│   ├── destinations.html
│   ├── packages.html
│   ├── about.html
│   └── contact.html
│
├── static/
│   ├── css/
│   ├── js/
│   ├── img/
│   ├── destinations/
│   └── uploads/
│
├── instance/
│   └── travels.db
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project on your local machine.

### 1. Clone the Repository

```bash
https://github.com/iamsudeeprathod-sudo/priyansh_travel.git
```

### 2. Navigate to the Project Folder

```bash
cd priyansh_travel
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python app.py
```

### 7. Open in Browser

```text
http://127.0.0.1:5000/
```

---

## 📦 Required Dependencies

Add the following packages to your `requirements.txt`:

```text
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Werkzeug==2.3.7
Pillow==10.0.1
```

---

## 🗄️ Database Structure

The project uses SQLite with Flask-SQLAlchemy.

### Booking Table

| Column | Data Type | Description |
|---|---|---|
| id | Integer | Primary Key |
| name | String | Customer name |
| email | String | Customer email |
| destination | String | Selected destination |
| travelers | Integer | Number of travelers |
| date | DateTime | Booking creation date |

Booking information is stored in the SQLite database.

---

## 🌎 Available Destinations

The website currently includes the following destinations:

| Destination | Category |
|---|---|
| Maldives | Beach |
| Bali | Beach |
| Paris | Culture |
| Dubai | Luxury |
| Goa | Beach |
| Switzerland | Adventure |
| Thailand | Beach |
| New York | Culture |
| Mauritius | Luxury |
| Himachal | Adventure |
| Singapore | Luxury |
| Kerala | Culture |

---

## 🔮 Future Enhancements

The following features can be implemented in future versions:

- 🔐 User Registration and Login System
- 💳 Online Payment Gateway Integration
- 📧 Booking Confirmation Through Email
- 📍 Google Maps Integration
- 🤖 AI-Based Travel Recommendations
- ⭐ Customer Feedback and Review System
- 📊 Admin Dashboard for Booking Management
- 🔎 Advanced Destination Search and Filtering

---

## 🎯 Project Objective

The objective of Priyansh Travel is to develop a simple and accessible online travel booking platform that helps users explore destinations, compare travel options, and submit booking requests.

This project also demonstrates practical implementation of Python Flask, database connectivity, backend development, and frontend web technologies.

---

## 👨‍💻 Developer

**Project Name:** Priyansh Travel

**Developer:** Sudeep Rathod

**Project Type:** Travel & Tourism Website

**Backend:** Python Flask

**Database:** SQLite

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.

**Explore More. Travel More. Create Memories! ✈️**

---
<p align="center">
  Made with ❤️ using Python Flask
</p>
