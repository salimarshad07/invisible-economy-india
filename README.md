# The Invisible Economy
### India's Street Vendors & Urban Homeless — Data Project 2026

> *"The last time India counted its homeless, Manmohan Singh was Prime Minister."*

A data journalism investigation into India's informal survival economy — street vendors and homeless populations — using live government data, SQL analysis, Python EDA, and Tableau visualisation.

**Published:** [The Data Desk](https://data-desk.vercel.app/stories/invisible-economy) · June 2026  
**Author:** [Salim Arshad](https://github.com/salimarshad07)  
**Dashboard:** [Tableau Public](https://public.tableau.com/views/TheInvisibleEconomyIndiaStreetVendorsHomelessData2026/Dashboard)
📄 Research Paper: https://www.researchgate.net/publication/407045444

---

## The Story

Millions of Indians survive on the margins of cities that don't count them properly. This project uses the government's own data to reveal:

- A **6x gap** between official homeless counts and ground reality in Delhi
- A scheme that reached **76 lakh vendors** but left millions out
- A shelter programme that **quietly shut down in September 2024** with no announcement
- India's last national homeless survey: **2011** — 15 years ago

---

## Repository Structure

```
invisible-economy-india/
├── data/
│   ├── 01_homeless_population_statewise_2011.csv
│   ├── 02_svanidhi_yearwise_national.csv
│   ├── 03_svanidhi_statewise_loans.csv
│   ├── 04_shelter_vs_homeless_gap.csv
│   ├── 05_key_indicators_reference.csv
│   └── svanidhi_2026_live.xlsx
├── sql/
│   ├── create_tables.sql
│   └── analysis_queries.sql
├── python/
│   ├── eda.py
│   ├── top10_beneficiaries.png
│   └── bottom10_repayment.png
└── README.md
```

---

## Key Findings

| Indicator | Figure |
|---|---|
| SVANidhi beneficiaries | 76 lakh |
| Total amount disbursed | ₹18,083 crore |
| Bihar loan conversion rate | 58.7% |
| Delhi loan conversion rate | 60.1% |
| Haryana repayment rate | 45% (lowest) |
| West Bengal repayment rate | 46.3% |
| Mizoram digital adoption | 88.8% (highest) |
| Official urban homeless (2011) | 9.38 lakh |
| Delhi gap (official vs actual) | 6.4× — 46,724 vs 3,00,000 |
| Shelter shortfall | 7.97 lakh spaces |
| DAY-NULM closure | 30 September 2024 |
| Last national homeless survey | 2011 |

---

## Data Sources

| Dataset | Source |
|---|---|
| PM SVANidhi MIS Dashboard | pmsvanidhi.mohua.gov.in (live, 13 Jun 2026) |
| Homeless population by state | Census 2011 via MoHUA PIB Reply PRID 1783924 |
| SVANidhi year-wise disbursement | Rajya Sabha replies (Sessions 260, 262, 266) |
| State-wise loan data | RTI 2022 via National Herald India + Lok Sabha reply Aug 2023 |
| Shelter vs homeless gap | MoHUA Press Release July 2024 + civil society reports |
| Key indicators reference | PolicyCircle Nov 2025, PIB Factsheet Mar 2024 |

---

## Methodology

### Phase 1 — Data Collection
All datasets were built from primary government sources: parliamentary replies, RTI disclosures, MoHUA press releases, and live MIS dashboards. No secondary aggregators were used for headline numbers.

### Phase 2 — SQL Analysis
MySQL database `invisible_economy` with 4 tables:
- `dim_states` — master state list with region groupings (36 rows)
- `fact_homeless` — Census 2011 homeless data (35 rows)
- `fact_svanidhi` — Live SVANidhi 2026 data (36 rows)
- `fact_shelter_gap` — Shelter capacity vs homeless gap (9 rows)

Six analytical queries: conversion rates, repayment rates, digital adoption, regional performance, and a JOIN query comparing homeless burden vs vendor support by state.

### Phase 3 — Python EDA
Libraries: `pandas`, `matplotlib`  
Computed: `conversion_rate`, `repayment_rate`, `digital_adoption`  
Output: two chart PNGs in `/python/`

### Phase 4 — Tableau Dashboard
Connected `svanidhi_2026_live.xlsx` + `01_homeless_population_statewise_2011.csv`  
Built: choropleth map, top-10 bar chart, repayment rate chart, homeless population chart  
Published: [Tableau Public](https://public.tableau.com/views/TheInvisibleEconomyIndiaStreetVendorsHomelessData2026/Dashboard)

---

## Tools Used

- **MySQL Workbench** — database and SQL analysis
- **Python 3.14** + pandas + matplotlib — EDA and charts
- **Tableau Public** — dashboard and visualisation
- **VS Code** — development environment
- **Excel** — data collection and cleaning

---

## How to Use This Data

All datasets are in `/data/` and are free to use for research and journalism with attribution.

```bash
git clone https://github.com/salimarshad07/invisible-economy-india.git
cd invisible-economy-india
```

To run the SQL analysis, import the scripts in `/sql/` into MySQL Workbench in order:
1. `create_tables.sql`
2. `analysis_queries.sql`

To run the Python EDA:
```bash
pip install pandas matplotlib openpyxl
python python/eda.py
```

---

## Part of The Data Desk

This project is part of [The Data Desk](https://data-desk.vercel.app), an independent data journalism publication by Salim Arshad examining public claims and the numbers behind the headlines.

**Other projects:**
- [India GDP Fact Check](https://data-desk.vercel.app/stories/india-gdp-fact-check) — Was India really growing at 7.7%?
- [West Bengal Election 2026 Analysis](https://github.com/salimarshad07/west_bengal_election_2026_analysis)

---

*Data is public. Methods are open. Show your work.*
