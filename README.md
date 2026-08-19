# Sales Insights AI

An AI-powered sales analysis project — starting with data cleaning and
exploratory analysis, building toward a RAG + agent system that can answer
natural-language questions about sales performance.

## 🎯 Motive

Sales data is often scattered and hard for non-technical people to query
directly. This project turns a raw sales dataset into clean, analyzable
data, surfaces real trends, and (in later phases) lets anyone ask
plain-English questions and get grounded answers — combining computed
metrics with contextual retrieval.

## 📊 Dataset

- **Source:** [Sample Sales Data (Kaggle)](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)
- **Size:** 2,823 order records, 25 original columns
- **Content:** Order-level sales transactions — quantity, price, revenue,
  product line, customer, territory, deal size, and order date
  (2003–2005)

## 🧹 Data Cleaning

Raw data (`data/raw/sales_data_raw.csv`) had:
- Text-formatted dates (`2/24/2003 0:00`) instead of real dates
- Non-UTF-8 encoding requiring `ISO-8859-1` to read correctly
- Irrelevant columns (addresses, phone numbers) for sales analysis
- Missing `TERRITORY` values for ~38% of rows

`src/clean_data.py` produces `data/sales_data_clean.csv`:
- Parsed `order_date` as a real datetime column
- Dropped irrelevant address/contact columns
- Filled missing territory values with `"Unknown"`
- Renamed columns to clear, lowercase `snake_case` names
- Kept 15 relevant columns: `order_id`, `order_date`, `quantity`,
  `unit_price`, `revenue`, `status`, `product_category`, `product_code`,
  `customer_name`, `country`, `territory`, `deal_size`, `quarter`,
  `month`, `year`

## 🛠️ Tech Stack

- Python, pandas (data cleaning + analysis)
- matplotlib (charts)
- Vector DB + embeddings (RAG layer — planned)
- Claude / LLM API (agent layer — planned)
- Streamlit (dashboard — planned)

## 📂 Project Structure

```
sales-insights-ai/
├── data/
│   ├── raw/
│   │   └── sales_data_raw.csv       # original Kaggle download
│   └── sales_data_clean.csv         # cleaned, analysis-ready data
├── src/
│   ├── explore_data.py              # initial data inspection
│   └── clean_data.py                # cleaning pipeline
├── notebooks/                       # exploratory notebooks (WIP)
├── .gitignore
└── README.md
```

## 🚀 Setup

```bash
git clone https://github.com/vanshikatandxn/sales-insights-ai.git
cd sales-insights-ai
python -m venv venv
venv\Scripts\activate      # Windows
pip install pandas matplotlib jupyter openpyxl
```

## 📌 Roadmap

- [x] Environment setup
- [x] Get real sales data (Kaggle)
- [x] Clean and structure the data
- [ ] Exploratory analysis (trends, top products, top territories)
- [ ] Dashboard
- [ ] RAG pipeline over sales notes/context
- [ ] AI agent for natural-language sales queries

## 📄 License
MIT
