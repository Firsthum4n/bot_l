from settings import BotSettings

bot_b = BotSettings()
gpt_header = {'GPT_KEY': bot_b.site_api_key.get_secret_value()}

