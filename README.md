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
- **Frontend**: HTML5, CSS3, Bootstrap 5
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

## License

- MIT License ©  Jaiganesh1607
