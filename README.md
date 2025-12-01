# 🔹 AI Text Summarizer (Streamlit App)

A simple yet powerful **AI-based Text Summarization Web App** built using  
`Streamlit + Sumy NLP summarization models`.

The app allows users to paste any text, choose the summarization algorithm,  
and instantly generate a compressed summary while keeping the main meaning.

---

## 🚀 Features

✓ Clean & interactive Streamlit UI  
✓ Supports multiple summarization models  
✓ Choose number of summary sentences  
✓ Download summary as `.txt` file  
✓ Fast processing & lightweight NLP backend  

---

## 🎬 Demo Video

<video width="400" controls>
  <source src="assets/demo.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

---

## 🧠 Summarization Models Included

| Model | Type | Notes |
|---|---|---|
| **LsaSummarizer** | Mathematical/Matrix-based | Great for structured text |
| **LuhnSummarizer** | Frequency-based | Focuses on most important words |
| **LexRankSummarizer** | Graph-based | Sentence ranking by similarity |
| **TextRankSummarizer** | Graph-based (Python version of Google TextRank) | Powerful for longer text |

---

## 📦 Installation

```bash
pip install streamlit sumy
