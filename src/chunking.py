from loader import load_json

data = load_json()


def splitter() -> list:
    combined_text = []
    chunks = []
    # Combine Prompt and Response into a single document
    for item in data:
        for key, value in item.items():
            combined_text.append(str(value))  # Ensure all values are strings
    for i in range(0, len(combined_text), 100):
        chunk = " ".join(combined_text[i : i + 100])
        chunks.append(chunk)
    return chunks
