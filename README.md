# Bitcoin Direction Classification with Sentiment

## Project setting and subject
**Graduate coursework at Özyeğin University — CS540, Machine Learning in Finance.** This project was conducted during Emre Öztürk’s master’s studies, jointly and equally with Ali Baki Türköz. The subject is Bitcoin direction classification using market features, news/social-media sentiment and the Fear & Greed index, with temporal evaluation.

An academic research portfolio exploring whether news, Twitter sentiment and the Fear & Greed index add useful information to Bitcoin price-based features. Emre Öztürk and Ali Baki Türköz conducted all stages jointly and equally for CS540, Machine Learning in Finance, at Özyeğin University.

## What was done and why
The team filtered Bitcoin-related text, calculated VADER sentiment scores, aggregated records by date and aligned them with price observations. They compared price-only and sentiment-enriched feature sets using classical classifiers and small MLP networks. Lagged returns, rolling volatility and price/volume features describe market history. The task is three-class future-return classification, not a deployed trading service.

Two panels were studied: a shorter, irregular Price–Tweets–News panel and a longer Price–Fear & Greed–News panel. Their sizes and horizons differ. In the irregular panel, a shifted target refers to the next retained observation; it cannot automatically be called the next calendar day.

## How the evaluation worked
The latest supplied notebook uses expanding walk-forward windows, with thresholds for the three return classes computed from each outer training window. The longer-panel configuration starts with 400 rows and uses 30-row test windows; the shorter configuration starts with 90 rows and uses 15-row windows. The archived runs show nine and three outer folds respectively. Scaling is placed in model pipelines.

## Archived outcomes
These values are copied from saved notebook outputs and have not been rerun:

| Saved analysis | Selected row | Macro-F1 | Accuracy | Folds |
|---|---|---:|---:|---:|
| Longer panel, classical tuned table, cell 30 | Price / Logistic regression | 0.3478 ± 0.0588 | 0.4926 ± 0.1402 | 9 |
| Shorter panel, classical tuned table, cell 32 | Price / Linear SVM | 0.3361 ± 0.0922 | 0.3778 ± 0.0770 | 3 |
| Shorter panel, MLP selected search, cell 36 | All / MLP with one 4-unit hidden layer | 0.421602 ± 0.137876 | 0.466667 | 3 |

The selected macro-F1 values are modest and the sentiment benefit is inconclusive. No majority/persistence or other naive-baseline comparison is present in the exported result tables; a fixed 0.33 should not be treated as a verified chance baseline because class proportions and prediction distributions matter. The evidence does not establish a consistent sentiment advantage or trading profitability. Candidate ranking uses the evaluated outer results. The MLP search also chooses settings using mean outer-fold scores, so its selected score is a development result, not an untouched final test. Classical inner tuning uses TimeSeriesSplit on the first outer training window; inner labels use thresholds from that whole first window, rather than recomputing thresholds inside each inner split. Historical target availability at fold boundaries also needs review before claiming a fully purged, leakage-free forecasting protocol.

[Archived output extracts](results/), [source manifest](docs/SOURCE_MANIFEST.json), [method and sharing notes](docs/METHOD_AND_SHARING.md).

## Selected code example
`examples/temporal_split.py` is a newly prepared educational excerpt showing an expanding split with a one-row embargo. It is not the original training pipeline and does not reproduce the archived scores. No full training notebook or raw tweet/news collection is shared here.

The repository is private. Dataset redistribution and source licences require separate review before public release. The project demonstrates data alignment, text sentiment processing, feature engineering, comparative modelling and careful interpretation of time-series evaluation.

## Portfolio preparation
Documentation, selected examples and portfolio packaging were prepared with Codex and Claude assistance. This later preparation is distinct from the authors’ original project work. Contact: emre.ozturk.2098@gmail.com.
