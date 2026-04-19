from transformers import pipeline


detector = pipeline("text-classification", model="hamzab/roberta-fake-news-classification")

def check_news(text):
    result = detector(text, truncation=True, max_length=512)[0]
    label = result["label"]
    score = round(result["score"] * 100, 2)

    if label == "FAKE":
        print(f"\n🚨 FAKE NEWS — {score}% confidence")
    else:
        print(f"\n✅ REAL NEWS — {score}% confidence")

if __name__ == "__main__":
    print("=== Fake News Detector ===")
    text = input("\nPaste a headline or article snippet:\n> ")
    check_news(text)