USE healthcare_analysis;

SELECT * FROM patients;

SELECT department, COUNT(*) AS total_patients
FROM patients
GROUP BY department;

SELECT diagnosis, COUNT(*) AS cases
FROM patients
GROUP BY diagnosis
ORDER BY cases DESC;

SELECT p.department, AVG(t.cost) AS avg_cost
FROM patients p
JOIN treatments t ON p.patient_id = t.patient_id
GROUP BY p.department;

SELECT p.name, p.diagnosis, t.cost
FROM patients p
JOIN treatments t ON p.patient_id = t.patient_id
WHERE t.cost > 50000;

SELECT doctor_name, SUM(cost) AS total_revenue
FROM treatments
GROUP BY doctor_name
ORDER BY total_revenue DESC;

SELECT department,
AVG(DATEDIFF(discharge_date, admission_date)) AS avg_stay_days
FROM patients
GROUP BY department;

SELECT gender, COUNT(*) AS total
FROM patients
GROUP BY gender;

SELECT * FROM patients
WHERE city = 'Hyderabad';

SELECT p.name, p.age, p.diagnosis,
t.treatment_name, t.cost, t.doctor_name
FROM patients p
JOIN treatments t ON p.patient_id = t.patient_id;