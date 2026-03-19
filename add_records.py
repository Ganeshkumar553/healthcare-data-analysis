import mysql.connector
import random
from datetime import datetime, timedelta

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password",
    database="healthcare_analysis"
)

cursor = conn.cursor()

names = [
    'Ravi Kumar', 'Priya Sharma', 'Suresh Reddy', 'Anita Singh',
    'Kiran Rao', 'Meena Patel', 'Vijay Das', 'Lakshmi Nair',
    'Arun Kumar', 'Deepa Joshi', 'Ramesh Babu', 'Sunita Rao',
    'Mahesh Kumar', 'Kavitha Reddy', 'Sanjay Gupta', 'Pooja Singh',
    'Rajesh Nair', 'Divya Patel', 'Venkat Rao', 'Anjali Kumar',
    'Amit Shah', 'Rekha Verma', 'Sunil Mehta', 'Geeta Singh',
    'Prakash Rao', 'Nisha Patel', 'Manoj Kumar', 'Swati Reddy'
]

cities = ['Hyderabad', 'Bangalore', 'Chennai', 'Mumbai', 'Delhi', 'Pune', 'Kolkata']
departments = ['Cardiology', 'Orthopedics', 'Neurology', 'General']
diagnoses = {
    'Cardiology': ['Heart Disease', 'Hypertension', 'Arrhythmia'],
    'Orthopedics': ['Fracture', 'Back Pain', 'Arthritis'],
    'Neurology': ['Stroke', 'Migraine', 'Epilepsy'],
    'General': ['Fever', 'Diabetes', 'Infection']
}
treatments = {
    'Cardiology': [('Bypass Surgery', 85000), ('Angioplasty', 95000), ('Medication', 5000)],
    'Orthopedics': [('Plaster Cast', 12000), ('Physiotherapy', 8000), ('Surgery', 45000)],
    'Neurology': [('MRI + Medication', 45000), ('Medication', 6000), ('Surgery', 75000)],
    'General': [('Medication', 3000), ('Insulin Therapy', 15000), ('IV Drip', 5000)]
}
doctors = {
    'Cardiology': 'Dr. Mehta',
    'Orthopedics': 'Dr. Rao',
    'Neurology': 'Dr. Sharma',
    'General': 'Dr. Patel'
}

def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

print("Adding 1000 patient records...")

for i in range(1000):
    name = random.choice(names)
    age = random.randint(18, 80)
    gender = random.choice(['Male', 'Female'])
    city = random.choice(cities)
    department = random.choice(departments)
    diagnosis = random.choice(diagnoses[department])
    admission = random_date(start_date, end_date)
    stay_days = random.randint(2, 14)
    discharge = admission + timedelta(days=stay_days)

    cursor.execute("""
        INSERT INTO patients (name, age, gender, city, admission_date, discharge_date, department, diagnosis)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (name, age, gender, city, admission.date(), discharge.date(), department, diagnosis))

    patient_id = cursor.lastrowid
    treatment = random.choice(treatments[department])
    doctor = doctors[department]
    cost_variation = random.randint(-5000, 5000)
    final_cost = max(1000, treatment[1] + cost_variation)

    cursor.execute("""
        INSERT INTO treatments (patient_id, treatment_name, cost, doctor_name, status)
        VALUES (%s, %s, %s, %s, %s)
    """, (patient_id, treatment[0], final_cost, doctor, 'Completed'))

conn.commit()
print("✅ 1000 records added successfully!")

cursor.execute("SELECT COUNT(*) FROM patients")
count = cursor.fetchone()
print(f"Total patients in database: {count[0]}")

cursor.close()
conn.close()