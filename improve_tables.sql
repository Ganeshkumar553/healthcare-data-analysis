USE healthcare_analysis;

CREATE TABLE IF NOT EXISTS doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    doctor_name VARCHAR(100),
    specialization VARCHAR(100),
    experience_years INT,
    department VARCHAR(50)
);

INSERT IGNORE INTO doctors (doctor_name, specialization, experience_years, department) VALUES
('Dr. Mehta', 'Cardiology', 15, 'Cardiology'),
('Dr. Rao', 'Orthopedics', 10, 'Orthopedics'),
('Dr. Sharma', 'Neurology', 12, 'Neurology'),
('Dr. Patel', 'General Medicine', 8, 'General');

ALTER TABLE patients DROP INDEX IF EXISTS idx_department;
ALTER TABLE patients DROP INDEX IF EXISTS idx_city;
ALTER TABLE patients DROP INDEX IF EXISTS idx_diagnosis;
ALTER TABLE treatments DROP INDEX IF EXISTS idx_doctor;

ALTER TABLE patients ADD INDEX idx_department (department);
ALTER TABLE patients ADD INDEX idx_city (city);
ALTER TABLE patients ADD INDEX idx_diagnosis (diagnosis);
ALTER TABLE treatments ADD INDEX idx_doctor (doctor_name);