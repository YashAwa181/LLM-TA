# Market-Level Sentiment Trading Strategy

## 📈 Project Overview
This repository contains the implementation of **Project A: Market-Level Sentiment Trading Strategy**, a coursework project designed to predict daily movements of the S&P 500 Index using financial Natural Language Processing (NLP). By processing and learning from over 146,000 Wall Street Journal headlines spanning from 2016 to 2023, the notebook demonstrates the end-to-end process of generating an actionable macroeconomic trading signal from raw text.

## 🗃️ Datasets
The project depends on several key datasets to compute predictions and evaluation metrics:
1. `Shared_wsj_headlines_2023.csv`: ~146,000 Wall Street Journal headlines from 2016-2023.
2. `Shared_spx_index_daily_2023.csv`: Daily price data of the S&P 500 Index used for calculating next-day returns.
3. `Shared_ff_factors_daily_2023.csv`: Fama-French 3-Factor Model data (Market excess return, SMB, HML) and Risk-Free rates used for evaluating strategy Alpha.
4. `wsj_finbert_labeled_16000.csv`: A labeled subset of 16k headlines used for training the sentiment classification models.

## 🧠 Part A: NLP Pipeline
The project benchmarks an explainable baseline text-classification model against an advanced deep learning model:
- **Benchmark Model:** Evaluates a traditional pipeline consisting of **TF-IDF Vectorization -> PCA Dimensionality Reduction -> Logistic Regression**.
- **Advanced Model:** Incorporates an **LSTM (Long Short-Term Memory)** neural network using tokenized padded sequences to improve upon the baseline.
- **Visualizations:** Generates insights into the NLP pipeline, highlighting the top defining positive/negative TF-IDF terms, K-Means headline topic clusters, and Precision/Recall/F1 classification metrics.

## 📊 Part B: Strategy Design
Predictions obtained from the NLP models are computationally aggregated to form a daily macroeconomic signal $S_t$.
Three specific strategies are formulated around this signal to capture market inefficiencies:
- **Momentum Strategy:** Standard risk-on/risk-off approach mapping positive sentiment direct to long SPX entries.
- **Mean-Reversion Strategy:** Contrarian methodology targeting days where the market overreacts to short-term negative sentiment.
- **Surprise Strategy:** Trading based on sudden deviations in sentiment, defined by a 30-day trailing moving average window.

## 💸 Part C: Quantitative Evaluation
We split our strategy's performance into an **In-Sample Period (2016-2021)** and an out-of-sample **Test Period (2022-2023)**, calculating rigorous evaluation metrics:
- **Basic Returns:** Cumulative Returns and Annualised Returns.
- **Risk-Adjusted Performance:** Annualised Volatility and Sharpe Ratio compared against standard Buy & Hold and 50/50 portfolio baselines. 
- **Risk Diagnostics:** Maximum Drawdowns and Calmar Ratio.
- **Factor Constraints:** Fama-French 3-Factor (FF3) standard OLS regression yielding Annualised Alphas and t-stats.
- **Cost Realities:** Net-of-cost performance tracking portfolio turnover at both 5 bps and 10 bps transaction costs.

## 🚀 Usage 
Open the `ProjectA_Market_Strategy.ipynb` notebook and execute all cells sequentially to regenerate the NLP models, construct the sentiment bounds, and evaluate the strategy plotting directly natively inside the notebook environment.
