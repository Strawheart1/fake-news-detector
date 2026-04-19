# 🚨 Fake News Detector

A Python-powered CLI tool that uses AI to detect whether a news headline or article snippet is **real or fake** — running completely locally with no paid API needed.

-----

## 🖥️ Demo

```
=== Fake News Detector ===

Paste a headline or article snippet:
> Scientists CONFIRM that 5G towers are secretly controlling human emotions

🚨 FAKE NEWS — 94.21% confidence
```

-----

## 🧠 How It Works

This tool uses a pre-trained AI model from HuggingFace (`roberta-fake-news-classification`) that was trained on thousands of real and fake news articles. It analyzes the language patterns in your text and returns a **REAL or FAKE** label with a confidence score.

- **Fake news** tends to use emotional, exaggerated, or vague language
- **Real news** tends to be neutral, specific, and fact-based

-----

## ⚙️ Installation

**1. Clone the repo**

```bash
git clone https://github.com/Strawheart1/fake-news-detector.git
cd fake-news-detector
```

**2. Install dependencies**

```bash
pip install transformers torch requests
```

**3. Run the tool**

```bash
python detector.py
```

> ⏳ The first run will download the AI model (~500MB). After that it runs instantly offline.

-----

## 📦 Requirements

```
transformers
torch
requests
```

Or install all at once:

```bash
pip install -r requirements.txt
```

-----

## ✅ Tips for Best Results

|Input                             |Result                     |
|----------------------------------|---------------------------|
|Full headline with context        |✅ Most accurate            |
|Paragraph from an article         |✅ Great                    |
|WhatsApp forwards / rumors        |✅ Works well               |
|Single words or very short phrases|❌ Too little context       |
|Very long articles                |⚠️ Gets trimmed to 512 words|

**Example inputs to try:**

- `"The Federal Reserve raised interest rates by 0.25% following its monthly policy meeting."`
- `"SHOCKING: Government secretly adding chemicals to water supply to control population!"`

-----

## ⚠️ Disclaimer

This tool is **not 100% accurate**. It works best on full sentences with enough context. Short or technical phrases may be misclassified.

Always verify surprising results with trusted fact-checking sources:

- 🔍 [Snopes](https://www.snopes.com)
- 🔍 [FactCheck.org](https://www.factcheck.org)
- 🔍 [Reuters Fact Check](https://www.reuters.com/fact-check)

-----

## 🚀 Planned Features

- [ ] Color output using the `rich` library
- [ ] `--url` flag to scrape and check any news article link
- [ ] Save results to a log file with timestamps
- [ ] Batch mode to check multiple headlines at once
- [ ] Simple web UI using Streamlit

-----

## 🛠️ Built With

- [Python](https://www.python.org/)
- [HuggingFace Transformers](https://huggingface.co/transformers/)
- [RoBERTa](https://huggingface.co/hamzab/roberta-fake-news-classification)

-----

## 📄 License

MIT License — free to use, modify, and share.

-----

## 🙌 Contributing

Pull requests are welcome! If you find a bug or have a feature idea, open an issue and let’s build it together.

-----

> Made with ❤️ to fight misinformation
