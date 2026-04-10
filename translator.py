# translator.py

EN_TO_IT = {
    "hello": "ciao",
    "goodbye": "addio",
    "please": "per favore",
    "thank you": "grazie",
    "yes": "sì",
    "no": "no",
    "cat": "gatto",
    "dog": "cane",
    "food": "cibo",
    "water": "acqua",
}

# Build reverse dictionary for Italian -> English
IT_TO_EN = {v: k for k, v in EN_TO_IT.items()}


def translate_en_to_it(text: str) -> str:
    words = text.lower().split()
    translated = [EN_TO_IT.get(w, f"[{w}]") for w in words]
    return " ".join(translated)


def translate_it_to_en(text: str) -> str:
    words = text.lower().split()
    translated = [IT_TO_EN.get(w, f"[{w}]") for w in words]
    return " ".join(translated)


def main():
    print("Simple English ↔ Italian Translator")
    print("Type 'exit' to quit.\n")

    while True:
        direction = input("Direction (en-it / it-en): ").strip().lower()
        if direction == "exit":
            break

        if direction not in ("en-it", "it-en"):
            print("Invalid direction. Use 'en-it' or 'it-en'.\n")
            continue

        text = input("Text: ").strip()
        if text.lower() == "exit":
            break

        if direction == "en-it":
            print("→", translate_en_to_it(text), "\n")
        else:
            print("→", translate_it_to_en(text), "\n")


if __name__ == "__main__":
    main()
