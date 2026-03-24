# Healthcare Data Analysis System

A end-to-end data analysis project using MySQL and Python to analyze patient, doctor, and treatment data across departments — generating automated Excel reports and visualizations for clinical insights.

---

## Technologies Used

- **MySQL** — Database design, optimized queries, stored procedures, indexes
- **Python** — Data processing and automation (pandas, SQLAlchemy, matplotlib, openpyxl)
- **Excel** — Automated 6-sheet report generation

---

## Database Design

- 3 normalized tables with 4 performance indexes
- 1,020+ patient records across 4 departments
- Indexes on: `patient_id`, `department`, `doctor_id`, `admission_date`

---

## Features

### SQL Layer
- 10+ optimized queries — JOINs, GROUP BY, aggregations, date functions
- 5 stored procedures for dynamic analysis:
  - Department-based patient analysis
  - Doctor revenue analysis
  - City-based patient distribution
  - Cost-based treatment analysis
  - Date-range filtering

### Python Layer
- Connected to MySQL via **SQLAlchemy**
- Automated data extraction using pandas
- 6-sheet Excel report auto-generated
- 6 matplotlib visualizations rendered and saved

---

## Sample Output

### Patients by Department
| Department   | Total Patients |
|--------------|---------------|
| Neurology    | 273           |
| Orthopedics  | 254           |
| Cardiology   | 247           |
| General      | 246           |

### Average Cost by Department
| Department   | Avg Cost (₹)  |
|--------------|--------------|
| Cardiology   | 63,795        |
| Neurology    | 42,207        |
| Orthopedics  | 21,846        |
| General      | 7,797         |

### Doctor Revenue
| Doctor      | Total Revenue (₹) |
|-------------|------------------|
| Dr. Mehta   | 1,57,57,395       |
| Dr. Sharma  | 1,15,22,422       |
| Dr. Rao     | 55,48,943         |
| Dr. Patel   | 19,18,095         |

---

## Excel Report — 6 Sheets

| Sheet | Content |
|-------|---------|
| Summary | Overall patient and revenue statistics |
| Department Analysis | Patient count and cost per department |
| Doctor Revenue | Revenue breakdown by doctor |
| City Report | City-wise patient distribution |
| Cost Analysis | Treatment cost analysis |
| Monthly Trends | Admission trends over time |

---

## How to Run

### 1. Set up the database
```sql
-- Run in order
source create_tables.sql
source insert_data.sql
source queries.sql
source stored_procedures.sql
```

### 2. Install Python dependencies
```bash
pip install pandas sqlalchemy matplotlib openpyxl mysql-connector-python
```

### 3. Run the analysis
```bash
python analysis.py
```

### Output files generated
```
healthcare_report.xlsx       ← 6-sheet Excel report
healthcare_dashboard.png     ← combined dashboard chart
patients_by_department.png   ← department distribution
doctor_revenue.png           ← revenue by doctor
```

---

## Project Structure

```
healthcare-data-analysis/
├── create_tables.sql        ← table schema with indexes
├── insert_data.sql          ← 1,020+ patient records
├── queries.sql              ← 10+ optimized SQL queries
├── stored_procedures.sql    ← 5 stored procedures
├── analysis.py              ← Python automation script
└── README.md
```

---

## Key Learnings

- Designed normalized relational schema for real-world healthcare data
- Applied SQL performance optimization using indexes and stored procedures
- Built an end-to-end Python data pipeline from MySQL to Excel reports
- Automated multi-sheet report generation for client-ready analytical dashboards
