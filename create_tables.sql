CREATE DATABASE IF NOT EXISTS healthcare_analysis;
USE healthcare_analysis;

CREATE TABLE IF NOT EXISTS patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    city VARCHAR(50),
    admission_date DATE,
    discharge_date DATE,
    department VARCHAR(50),
    diagnosis VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS treatments (
    treatment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    treatment_name VARCHAR(100),
    cost DECIMAL(10,2),
    doctor_name VARCHAR(100),
    status VARCHAR(20),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);