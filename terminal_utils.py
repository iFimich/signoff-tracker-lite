# terminal_utils.py

def color_text(text, category):
    if category == "Ready":
        return f"\033[92m{text}\033[0m"  # Green
    elif category == "Needs Review":
        return f"\033[93m{text}\033[0m"  # Yellow
    elif category == "Failing":
        return f"\033[91m{text}\033[0m"  # Red
    return text