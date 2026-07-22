# Convertly

A modular Telegram bot platform designed for future SaaS growth.

## Structure

- app/clients/telegram - Telegram bot entrypoints and handlers
- app/engines/image - image processing engine
- app/services - domain services and message builders
- config - environment and configuration
- tests - automated checks

## Run

1. Install dependencies: `pip install -r requirements.txt`
2. Set BOT_TOKEN environment variable.
3. Start the bot: `python -m app.clients.telegram.bot`
