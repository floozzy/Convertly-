# Termux setup

1. Install Python and Git in Termux:
   - pkg update
   - pkg install python git

2. Clone the repository:
   - git clone https://github.com/floozzy/Convertly-.git
   - cd Convertly-

3. Install dependencies:
   - pip install -r requirements.txt

4. Create .env with your token:
   - echo 'BOT_TOKEN=your_token_here' > .env

5. Start the bot:
   - bash start.sh
