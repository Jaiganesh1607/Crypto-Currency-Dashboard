# Crypto Currency Dashboard - Django

A sleek and informative cryptocurrency dashboard built with **Django** that displays live data from the [CoinGecko API](https://www.coingecko.com/). This dashboard includes:

- Top 5 Cryptocurrencies by Market Cap  
- Trending Coins  
- Pie Chart of Market Cap Distribution  
- Bar Chart for 24h Price Change  
- Line Chart for Bitcoin's 7-day Price History

---
# Tech Stack
- **Backend**: Django 5.1.5
- **Frontend**: HTML5, CSS3
- **Charts**: Chart.js
- **API**: CoinGecko (no API key required)
- **Authentication**: Django’s built-in login system

##  Features

- Live cryptocurrency data via CoinGecko API (no API key required)
- Beautiful and responsive dashboard layout
- Dynamic charts using Chart.js
- Django user authentication system
- Error handling with custom 404 and 500 pages

---
## Prerequisites

Before you begin, ensure you have:

- **Python 3.11+** installed  
- **pip** (Python package manager)

## Local Setup Instructions
Follow these steps to run the project locally on your machine:

1. Clone the Repository

```bash
git clone https://github.com/Jaiganesh1607/Crypto-Currency-Dashboard.git
cd crypto-dashboard-django
```
Or download the zip file [dashboard_project.zip](https://github.com/Jaiganesh1607/Crypto-Currency-Dashboard/blob/main/dashboard_project.zip) from the repository and extract its contents 

2.Create a new virtual environment:

```command prompt
 python3 -m venv venv
```

3. Activate the Environment
On macOS/Linux:

```bash
source venv/bin/activate
```
On Windows:

```bash
venv\Scripts\activate
```

4. Install the dependencies for this project if you haven't installed them yet:

```command prompt
(venv)  python -m pip install -r requirements.txt
```

5. Make and apply the migrations for the project to build your local database:

```command prompt
(venv)  python manage.py makemigrations
(venv)  python manage.py migrate
```

6.Run the Django development server:

```command prompt
(venv)  python manage.py runserver
```
7. Access the Dashboard:

Open your browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the login page and signup using new username and password


# Screenshots

## Login page
![Screenshot 2025-05-17 133813](https://github.com/user-attachments/assets/f74f5d90-9154-4116-8ae6-a835ddf1838a)

## Signup page
![Screenshot 2025-05-17 133915](https://github.com/user-attachments/assets/cb90d1f9-bb14-4ea1-bc25-bfe6fb42c2b4)

## DashBoard
![Screenshot 2025-05-17 133827](https://github.com/user-attachments/assets/32de90cb-ced7-43fc-925e-489af70d2b20)

![Screenshot 2025-05-17 133842](https://github.com/user-attachments/assets/0d3f8437-e210-4589-94fc-57b2565bb5e0)

![Screenshot 2025-05-17 133903](https://github.com/user-attachments/assets/8f37f086-8974-4f72-9da3-b1fc44339f0a)

### Project Objective
The goal of this project was to build a dynamic and visually appealing **Cryptocurrency Dashboard** using Django that displays real-time crypto data from the CoinGecko API without requiring any API key. The dashboard provides key metrics and trends in a simple and accessible manner for users.


###  Design Decisions

- **No Database Required**: The app does not store fetched data, keeping it lightweight and fast.
- **API Without Key**: Chose CoinGecko API specifically to remove the need for API key setup for beginners.
- **Minimal Dependencies**: Used only essential libraries to simplify setup and ensure compatibility.
- **Deployment Ready**: Designed with clean structure and versioned `requirements.txt` for easy deployment or local testing.

---

###  Testing & Validation
- Manually tested all views and endpoints.
- Validated rendering of charts and coin data against live CoinGecko data.
- Verified UI responsiveness across devices.

---
# Uses
This cryptocurrency dashboard can be utilized in a variety of real-world scenarios:

- ### Personal Finance Monitoring :
  Track real-time cryptocurrency trends to make better investment decisions.

- ### Market Research :
  Quickly analyze trending coins, market cap distributions, and price movements without needing an account or API key.

- ### Crypto Startups :
  Serve as a prototype or MVP for building a more advanced trading, analytics, or portfolio management platform.

## License

- MIT License ©  Jaiganesh1607
