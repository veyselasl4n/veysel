import discord
import deepl

# Bot ve çeviri API anahtarlarını buraya güvenli şekilde ekleyin!
DISCORD_TOKEN = "MTM1NTQ3OTYxNTY0ODMwNTIyMg.GZJ7Ql.4i90JDmoyN9qq5Ch8bMWELtTyLB0t8giADOy-o"
DEEPL_API_KEY = "5376a140-5395-454e-9a3f-d04a6b6404ec:fx"

# DeepL çeviri istemcisi
translator = deepl.Translator(DEEPL_API_KEY)

# Discord istemcisi
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} olarak giriş yapıldı!")

@client.event
async def on_message(message):
    # Botun kendi mesajlarını çevirmemesi için kontrol ekliyoruz
    if message.author == client.user:
        return  # Bot kendi mesajlarını çevirmesin

    # Eğer mesaj boşsa, çevirmeye gerek yok
    if not message.content.strip():
        return  # Mesajı çevirmeyi atla

    try:
        # Mesajın dilini belirleme
        detected_lang = translator.translate_text(message.content, target_lang="EN-US", source_lang=None).detected_source_lang
        
        # Eğer mesaj İngilizceyse Türkçeye, Türkçeyse İngilizceye çevir
        if detected_lang == "EN":
            translated_text = translator.translate_text(message.content, target_lang="TR")
        else:
            translated_text = translator.translate_text(message.content, target_lang="EN-US")
        
        # Çeviriyi mesaj olarak gönder
        await message.channel.send(f"**Çeviri:** {translated_text.text}")
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Botu başlat
client.run(DISCORD_TOKEN)
