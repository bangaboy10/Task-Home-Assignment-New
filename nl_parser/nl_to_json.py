import re

def parse_nl(text):
    text = text.lower()

    result = {"entry": [], "exit": []}

    target = "entry" if any(k in text for k in ["buy", "enter", "trigger entry"]) else "exit"

    if "moving average" in text:
        period = int(re.search(r'(\d+)-day', text).group(1))
        result[target].append({
            "left": "close",
            "operator": ">",
            "right": f"sma(close,{period})"
        })

    if "volume" in text and "million" in text:
        result[target].append({
            "left": "volume",
            "operator": ">",
            "right": 1000000
        })

    if "rsi" in text:
        period = int(re.search(r'rsi\((\d+)\)', text).group(1))
        value = int(re.search(r'below (\d+)', text).group(1))
        result["exit"].append({
            "left": f"rsi(close,{period})",
            "operator": "<",
            "right": value
        })

    return result
