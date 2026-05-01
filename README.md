<img width="4096" height="2304" alt="image" src="https://github.com/user-attachments/assets/8667ef13-757c-4df0-bf67-339ec9aceac7" />


<img width="635" height="628" alt="image" src="https://github.com/user-attachments/assets/83f3a6c9-f841-4d04-b52e-f528de8f25e0" />

<img width="452" height="325" alt="image" src="https://github.com/user-attachments/assets/54f02a96-4b9f-469b-95f9-cd73afaea202" />

<img width="754" height="604" alt="image" src="https://github.com/user-attachments/assets/4c4d8759-43e6-4317-b497-2144a1432792" />

<img width="1365" height="856" alt="image" src="https://github.com/user-attachments/assets/039bc8bc-1b59-4529-b7bf-ed708a3cb704" />

# UFC Stance Intelligence

**From personal question to practical tool.**

I am right-handed. I fight southpaw. Only 5% of UFC fighters share my stance. Does this give me an advantage?

This repository answers that question in three parts.

---

## Repository Structure

| Folder | Content |
|--------|---------|
| `1-analysis/` | Statistical analysis (Python, Excel, Tableau) |
| `2-matchmaker/` | PostgreSQL stored function + Tableau dashboard |
| `3-streamlit-app/` | Interactive web app (Streamlit, Scikit-learn) |

---

## Part 1: Statistical Analysis

**Tech:** Python (Pandas, SciPy), Excel, Tableau

- Analyzed 117 UFC fighters across 4 stance-hand groups
- T-test: Southpaw has +5.2% higher win rate (p < 0.05)
- My group (Right-handed Southpaw): 77.92% win rate
- Only 5% of fighters share my stance

**Tableau Dashboard:** [Link]

---

## Part 2: Fighter Matchmaker

**Tech:** PostgreSQL, Tableau

Stored function `match_fighters()` with weighted scoring:

| Factor | Weight |
|--------|--------|
| Stance match | 20 points |
| Handedness match | 20 points |
| Weight class match | 60 points |

Returns top 5 matching fighters with learning tips.

**Tableau Dashboard:** [Link]

---

## Part 3: Streamlit Web App

**Tech:** Python, Streamlit, Scikit-learn, Plotly

User inputs: height, weight, reach, stance, handedness

Returns:
- Predicted win rate vs my profile
- Top 5 fighter twins with similarity score
- Personalized study lessons

**Live Demo:** [Link]

---

## Run Locally

```bash
git clone https://github.com/brianphu2310/ufc-stance-intelligence.git
cd ufc-stance-intelligence/3-streamlit-app
pip install -r requirements.txt
streamlit run app.py


