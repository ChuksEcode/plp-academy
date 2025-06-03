# chatbot.py
# CryptoBuddy – My First AI-Powered Financial Sidekick

from pycoingecko import CoinGeckoAPI

# Simple token splitting — no NLTK required
def preprocess_query(query):
    return query.lower().split()

# Show welcome message
print("👋 Welcome! I'm CryptoBuddy — your AI-powered financial sidekick!")
print("Ask me about trending cryptos, sustainability, or long-term investments. Type 'exit' to leave. 💸\n")
print("⚠️ Disclaimer: Cryptocurrency investing is risky. Always do your own research (DYOR) before making decisions.\n")

# Step 1: Fetch real-time crypto data
def get_crypto_data():
    cg = CoinGeckoAPI()
    try:
        live_data = {
            "bitcoin": cg.get_coin_by_id('bitcoin'),
            "ethereum": cg.get_coin_by_id('ethereum'),
            "cardano": cg.get_coin_by_id('cardano')
        }

        crypto_db = {}
        for coin, data in live_data.items():
            price_change = data["market_data"]["price_change_percentage_7d"] or 0
            crypto_db[data["name"]] = {
                "price_trend": "rising" if price_change > 0 else "falling",
                "market_cap": "high" if data["market_cap_rank"] <= 5 else "medium",
                "energy_use": "low" if coin == "cardano" else ("medium" if coin == "ethereum" else "high"),
                "sustainability_score": 8 if coin == "cardano" else (6 if coin == "ethereum" else 3)
            }
        return crypto_db
    except Exception as e:
        print(f"⚠️ Error fetching live data: {e}")
        print("Using fallback crypto data.\n")
        return {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3
            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8
            }
        }

crypto_db = get_crypto_data()

# Step 2: Rule-based AI logic
def get_recommendation(user_query):
    tokens = preprocess_query(user_query)

    if "sustainable" in tokens or "eco" in tokens or "green" in tokens:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 {recommend} is a great pick! It scores high in sustainability and uses less energy."

    if "trending" in tokens or "rising" in tokens or "up" in tokens:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        return f"📈 Trending cryptos right now: {', '.join(trending)}"

    if "invest" in tokens or "growth" in tokens or "long-term" in tokens:
        best = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["market_cap"] == "high"]
        if best:
            return f"🚀 Based on trends and market cap, {best[0]} is ideal for long-term growth!"
        return "💡 No perfect high-growth picks now, but Cardano and Ethereum show good potential."

    if "energy" in tokens or "efficient" in tokens or "eco-friendly" in tokens:
        efficient = [coin for coin in crypto_db if crypto_db[coin]["energy_use"] == "low"]
        return f"🔋 {', '.join(efficient)} uses low energy and is environmentally friendly."

    return "🤖 Sorry, I didn't catch that. Try asking about trending coins, sustainability, or long-term growth."

# Step 3: Chat loop
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("CryptoBuddy: See you next time! Stay savvy and sustainable! ✨")
        break
    response = get_recommendation(user_input)
    print(f"CryptoBuddy: {response}")
    print("⚠️ Disclaimer: Cryptocurrency investing is risky. Always do your own research.\n")
