import streamlit as st
import spacy
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

from sumy.summarizers.lsa import LsaSummarizer #mathamatical approach
from sumy.summarizers.luhn import LuhnSummarizer # ranking based on word frequency


from sumy.summarizers.lex_rank import LexRankSummarizer #graph based approach {Sentance}
from sumy.summarizers.text_rank import TextRankSummarizer #graph based approach {Words + sentance}



## GUI
st.title("Text Summarization APP")
text = st.text_area("Enter Text to Summarize...", height=150)
options = st.selectbox("Choose Summarizer Model ", ["LsaSummarizer", "LuhnSummarizer", "LexRankSummarizer", "TextRankSummarizer"])
sen_count = st.slider("Select Number of Sentences for Summary", min_value=1, max_value=10, value=5)

def summarize_text(text, options = 'LsaSummarizer', sen_count= 5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))


    if options == "LsaSummarizer":
        summarizer = LsaSummarizer()
    elif options == "LuhnSummarizer":
        summarizer = LuhnSummarizer()
    elif options == "LexRankSummarizer":
        summarizer = LexRankSummarizer()
    else:
        summarizer = TextRankSummarizer()    

    summary = summarizer(parser.document,sen_count)

    return ' '.join([str(sentence) for sentence in summary]) #join words to make sentence

if st.button("Summarize"):
    if text:
        sammary = summarize_text(text, options, sen_count)
        st.subheader("Summarized Text")
        st.write(sammary)
    else:
        st.warning("Please enter text to summarize.")

