# TWEC – Temporal Semantic Change

Example of using [TWEC](https://github.com/loretoparisi/twec) to track **semantic change over time** with aligned word embeddings.

## How it works
1. Load a TSV corpus with `text_content` and `text_date`.
2. Bucket texts by **year** or **custom date ranges**.
3. Train a **compass** model on the whole corpus.
4. Train **aligned slice models** per time bucket.
5. Print nearest neighbors of a target word for each time slice.

## Requirements
```bash
pip install pandas gensim twec
```

## Run 
```bash
python twec_temporal.py
```

## Configure in the script:
- TSV_PATH – path to your TSV file
- BUCKET_MODE – "year" or "custom"
- TARGET_WORD – word to track

Example output
```bash
=== Nearest neighbors for 'Organspende' across time ===
y1992: Transplantation (0.46), Spender (0.42)
y2010: Organspender (0.48), Transplantationsgesetz (0.44)
y2020: Gewebespende (0.47), Zustimmungslösung (0.41)
```
Outputs:
	•	data/ – sentence files per time bucket
	•	model/ – trained compass + slice models
