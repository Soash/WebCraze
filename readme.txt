git clone https://github.com/Soash/Sky_Loom_Bot.git
cd .\Sky_Loom_Bot\

python -m venv venv
.\venv\Scripts\activate

pip install requests bs4 selenium pandas webdriver-manager

python .\main.py
