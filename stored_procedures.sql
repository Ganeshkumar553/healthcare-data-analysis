USE healthcare_analysis;

DELIMITER //
CREATE PROCEDURE GetPatientsByDepartment(IN dept_name VARCHAR(50))
BEGIN
    SELECT p.name, p.age, p.diagnosis,
    t.treatment_name, t.cost
    FROM patients p
    JOIN treatments t ON p.patient_id = t.patient_id
    WHERE p.department = dept_name;
END //
DELIMITER ;

CALL GetPatientsByDepartment('Cardiology');

DELIMITER //
CREATE PROCEDURE GetDoctorRevenue(IN doc_name VARCHAR(100))
BEGIN
    SELECT doctor_name,
    COUNT(*) AS total_patients,
    SUM(cost) AS total_revenue,
    AVG(cost) AS avg_cost
    FROM treatments
    WHERE doctor_name = doc_name;
END //
DELIMITER ;

CALL GetDoctorRevenue('Dr. Mehta');