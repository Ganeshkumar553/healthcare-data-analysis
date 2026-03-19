USE healthcare_analysis;

DELIMITER //
CREATE PROCEDURE GetPatientsByCity(IN city_name VARCHAR(50))
BEGIN
    SELECT p.name, p.age, p.department,
    p.diagnosis, t.treatment_name, t.cost
    FROM patients p
    JOIN treatments t ON p.patient_id = t.patient_id
    WHERE p.city = city_name;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetHighCostTreatments(IN min_cost DECIMAL(10,2))
BEGIN
    SELECT p.name, p.department, p.diagnosis,
    t.treatment_name, t.cost, t.doctor_name
    FROM patients p
    JOIN treatments t ON p.patient_id = t.patient_id
    WHERE t.cost > min_cost
    ORDER BY t.cost DESC;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetMonthlyAdmissions(IN month_num INT)
BEGIN
    SELECT COUNT(*) as total_admissions,
    department,
    AVG(cost) as avg_cost
    FROM patients p
    JOIN treatments t ON p.patient_id = t.patient_id
    WHERE MONTH(admission_date) = month_num
    GROUP BY department;
END //
DELIMITER ;

CALL GetPatientsByCity('Hyderabad');
CALL GetHighCostTreatments(50000);
CALL GetMonthlyAdmissions(1);