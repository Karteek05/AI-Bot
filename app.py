from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=60, min_length=20, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    print("Welcome to Tiny AI Summarizer!")
    article = input("Paste a news article or blog text:\n\n")
    print("\n--- Summary ---")
    print(summarize_text(article))