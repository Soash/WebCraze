git clone https://github.com/Soash/WebCraze.git
cd .\WebCraze\

python -m venv venv
.\venv\Scripts\activate

pip install requests bs4 selenium pandas webdriver-manager

python .\main.py
