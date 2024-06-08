from settings import BotSettings


bot_a = BotSettings()
header_tg = {'BOT_TOKEN': bot_a.tg_api_key.get_secret_value()}