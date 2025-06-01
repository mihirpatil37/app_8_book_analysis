# Book & Diary Sentiment Analysis

This project consists of two main components:

1. **Book Analysis** of *Miracle in the Andes* using natural language processing techniques  
2. **Diary Sentiment Dashboard** built with Streamlit to visualize sentiment trends across diary entries

---

## Book Analysis

The `Book_Analysis.ipynb` notebook performs textual analysis on the book *Miracle in the Andes*. Key tasks include:

- **Chapter Counting**
  - Uses string methods and regex to count the number of chapters.
- **Keyword Search**
  - Extracts sentences containing the word `"love"` using regex patterns.
- **Word Frequency Analysis**
  - Identifies and ranks the most frequently used words in the book.

### Techniques Used:

- Regular Expressions (`re`)
- Dictionary-based frequency counting
- Text normalization (e.g., `.lower()` for case folding)

---

## Diary Sentiment Dashboard

The `main.py` script uses Streamlit and NLTK’s `SentimentIntensityAnalyzer` to evaluate and visualize the **positivity** and **negativity** in a set of diary entries.

### Workflow:

1. **Load Diary Files**
   - Reads multiple `.txt` files from the `diary/` directory.
2. **Sentiment Analysis**
   - Applies `analyzer.polarity_scores()` on each diary entry.
3. **Interactive Dashboard**
   - Uses Plotly to plot line charts for:
     - **Positivity over time**
     - **Negativity over time**

---

## Folder Structure
```css
diary/
├── 2023-10-21.txt
├── 2023-10-22.txt
├── 2023-10-23.txt
├── 2023-10-24.txt
├── 2023-10-25.txt
├── 2023-10-26.txt
├── 2023-10-27.txt
Book_Analysis.ipynb
main.py
miracle_in_the_andes.txt
```

## Requirements

- Python 3.7+
- `nltk`
- `streamlit`
- `plotly`

### Install requirements

```bash
pip install nltk streamlit plotly
```
### Download the VADER lexicon for sentiment analysis:
```python
import nltk
nltk.download('vader_lexicon')
```
## Run the App
```python
streamlit run main.py
```
## Insights
- The book analysis reveals word patterns and thematic content like frequent mentions of “love”.
- The dashboard shows how emotional tones in diary entries shift over time—useful for journaling, self-reflection, or mental health monitoring.

## Acknowledgments
- Book: Miracle in the Andes by Nando Parrado
- Sentiment Analysis: NLTK VADER
- Dashboard Tools: Streamlit and Plotly
