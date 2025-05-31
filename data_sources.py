import requests

def get_gold_price():
    """
    Holt den aktuellen Spotpreis für XAU/USD von Yahoo Finance (inoffiziell).
    Kein API-Key erforderlich.
    """
    url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=XAUUSD=X"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        price = data["quoteResponse"]["result"][0]["regularMarketPrice"]
        return round(price, 2)
    except Exception as e:
        print("Fehler beim Abrufen des Goldpreises:", e)
        return None

def get_dxy():
    """US-Dollar Index DXY von Yahoo Finance"""
    url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=DX-Y.NYB"
    try:
        response = requests.get(url, timeout=5)
        return round(response.json()["quoteResponse"]["result"][0]["regularMarketPrice"], 2)
    except:
        return None

def get_vix():
    """Volatilitätsindex (VIX) von Yahoo Finance"""
    url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=^VIX"
    try:
        response = requests.get(url, timeout=5)
        return round(response.json()["quoteResponse"]["result"][0]["regularMarketPrice"], 2)
    except:
        return None

def get_yield_10y():
    """10-jährige US-Staatsanleihe Rendite"""
    url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=^TNX"
    try:
        response = requests.get(url, timeout=5)
        return round(response.json()["quoteResponse"]["result"][0]["regularMarketPrice"] / 10, 2)  # ^TNX gibt 10x Wert zurück
    except:
        return None

def get_ig_sentiment():
    return 66  # % Long

def get_cot_data():
    return 164000  # Netto-Longs
