BEGIN TRANSACTION;

--
-- Database: Covid-19 database
--

-- Table structure for table Country_Code

DROP TABLE IF EXISTS Country_Code;
CREATE TABLE Country_Code (
	name varchar(40) NOT NULL,
	code varchar(3) NOT NULL,
	PRIMARY KEY (code)
);

-- Table structure for table Country_Continent

DROP TABLE IF EXISTS Country_Continent;
CREATE TABLE Country_Continent (
	continent_name  varchar(15) NOT NULL,
	country_code varchar(3) NOT NULL,
	PRIMARY KEY (country_code)
);

-- Table structure for table Country

DROP TABLE IF EXISTS Country;
CREATE TABLE Country (
	country_code varchar(3) NOT NULL,
	population float(8) DEFAULT NULL,
	life_expectancy float(8) DEFAULT NULL,
	hospital_beds_per_thousand float(8) DEFAULT NULL,
	handwashing_facilities float(8) DEFAULT NULL,
	male_smokers float(8) DEFAULT NULL,
	female_smokers float(8) DEFAULT NULL,
	diabetes_prevalence float(8) DEFAULT NULL,
	cardiovasc_death_rate float(8) DEFAULT NULL,
	extreme_poverty float(8) DEFAULT NULL,
	gdp_per_capita float(8) DEFAULT NULL, 
	aged_70_older float(8) DEFAULT NULL,  
	aged_65_older float(8) DEFAULT NULL,  
	median_age float(8) DEFAULT NULL,  
	population_density float(8) DEFAULT NULL,
	stringency_index float(8) DEFAULT NULL,

	PRIMARY KEY (country_code)
	-- CONSTRAINT fk_franchID_teams
	-- FOREIGN KEY(franchID)
	-- REFERENCES Country_Continent(franchID) 
);

-- Table structure for table Hosp_defence

DROP TABLE IF EXISTS Hosp_defence;
CREATE TABLE Hosp_defence (
	name varchar(30) NOT NULL,
	no_hospitals int DEFAULT NULL,
	no_beds int DEFAULT NULL,
	PRIMARY KEY (name)
);

-- Table structure for table Hosp_gov

DROP TABLE IF EXISTS Hosp_gov;
CREATE TABLE Hosp_gov (
	state_name varchar(30) NOT NULL,
	rural_hosp int DEFAULT NULL,
	rural_beds int DEFAULT NULL,
	urban_hosp int DEFAULT NULL,
	urban_beds int DEFAULT NULL,
	PRIMARY KEY (state_name)
);

-- Table structure for table Hosp_railways

DROP TABLE IF EXISTS Hosp_railways;
CREATE TABLE Hosp_railways (
	zone varchar(50) NOT NULL,
	no_hospitals int DEFAULT NULL,
	no_beds int DEFAULT NULL,
	PRIMARY KEY (zone)
);

-- Table structure for table India_cases

DROP TABLE IF EXISTS India_cases;
CREATE TABLE India_cases (
	date varchar(20) NOT NULL,
	conf int DEFAULT 0,
	total_conf int DEFAULT 0,
	rec int DEFAULT 0,
	total_rec int DEFAULT 0,
	deceased  int DEFAULT 0,
	total_deceased int DEFAULT 0,
	PRIMARY KEY (date)
);

-- Table structure for table India_tests

DROP TABLE IF EXISTS India_tests;
CREATE TABLE India_tests (
	date DATE NOT NULL,
	total_samples float(8) DEFAULT NULL,
	total_positive int DEFAULT NULL,
	tpcc float(8) DEFAULT NULL,
	tpm float(8) DEFAULT NULL,
	PRIMARY KEY (date)
);

-- Table structure for table India_vaccine

DROP TABLE IF EXISTS India_vaccine;
CREATE TABLE India_vaccine (
	date DATE NOT NULL,
	total_doses float(8) DEFAULT NULL,
	sessions float(8) DEFAULT NULL,
	sites  float(8) DEFAULT NULL,
	first_dose float(8) DEFAULT NULL,  
	second_dose float(8) DEFAULT NULL,
	male float(8) DEFAULT NULL,
	female float(8) DEFAULT NULL,
	trans float(8) DEFAULT NULL,
	covaxin  float(8) DEFAULT NULL,
	covishield float(8) DEFAULT NULL,  
	sputnikv float(8) DEFAULT NULL,
	doses_18to44 float(8) DEFAULT NULL,
	doses_45to60 float(8) DEFAULT NULL,
	doses_60plus float(8) DEFAULT NULL,
	PRIMARY KEY (date)
);

-- Table structure for table Patients

DROP TABLE IF EXISTS Patients;
CREATE TABLE Patients (
	date DATE DEFAULT NULL,
	patient_no int NOT NULL,
	age float(8) DEFAULT NULL,
	gender varchar(10) DEFAULT NULL,
	city varchar(40) DEFAULT NULL,  
	district varchar(30) DEFAULT NULL,
	state varchar(40) DEFAULT NULL,
	state_code varchar(2) DEFAULT NULL,
	nationality varchar(50) DEFAULT NULL,  
	transmission varchar(10) DEFAULT NULL,
	PRIMARY KEY (patient_no)
);

-- Table structure for table State_cases

DROP TABLE IF EXISTS State_cases;
CREATE TABLE State_cases (
	date DATE NOT NULL,
	state_code varchar(2) NOT NULL,
	conf int DEFAULT NULL,
	deceased int DEFAULT NULL,
	rec int DEFAULT NULL,
	state_name varchar(40) NOT NULL,
	PRIMARY KEY (date, state_code)
);

-- Table structure for table State_tests

DROP TABLE IF EXISTS State_tests;
CREATE TABLE State_tests (
	date DATE NOT NULL,
	state varchar(40) NOT NULL,
	total_test float(8) DEFAULT NULL,
	positive float(8) DEFAULT NULL,
	negative float(8) DEFAULT NULL,
	unconfirmed float(8) DEFAULT NULL,
	total_quarantine float(8) DEFAULT NULL,
	total_quarantine_released float(8) DEFAULT NULL,
	people_icu float(8) DEFAULT NULL,
	people_venti float(8) DEFAULT NULL,
	num_iso_beds float(8) DEFAULT NULL,
	num_icu_beds float(8) DEFAULT NULL,
	num_venti float(8) DEFAULT NULL,
	tpm float(8) DEFAULT NULL,
	tpcc int DEFAULT NULL,
	PRIMARY KEY (date, state)
);

-- Table structure for table State_vaccine

DROP TABLE IF EXISTS State_vaccine;
CREATE TABLE State_vaccine (
	date DATE NOT NULL,
	state varchar(40) NOT NULL,
	total_doses float(8) DEFAULT NULL,
	sessions float(8) DEFAULT NULL,
	sites  float(8) DEFAULT NULL,
	first_dose float(8) DEFAULT NULL,
	second_dose float(8) DEFAULT NULL,  
	male float(8) DEFAULT NULL,
	female float(8) DEFAULT NULL,
	trans float(8) DEFAULT NULL,
	covaxin float(8) DEFAULT NULL,
	covishield float(8) DEFAULT NULL,
	sputnikv float(8) DEFAULT NULL,
	doses_18to44  float(8) DEFAULT NULL,
	doses_45to60 float(8) DEFAULT NULL,
	doses_60plus float(8) DEFAULT NULL,  
	PRIMARY KEY (date, state)
);

-- Table structure for table World_cases

DROP TABLE IF EXISTS World_cases;
CREATE TABLE World_cases (
	country_code varchar(15) NOT NULL,
	date DATE NOT NULL,
	total_cases float(8) DEFAULT NULL,
	new_cases float(8) DEFAULT NULL,
	new_cases_smoothed float(8) DEFAULT NULL,
	total_deaths float(8) DEFAULT NULL,
	new_deaths float(8) DEFAULT NULL,
	new_deaths_smoothed float(8) DEFAULT NULL,
	reproduction_rate float(8) DEFAULT NULL,
	icu_patients float(8) DEFAULT NULL,
	hosp_patients float(8) DEFAULT NULL,
	weekly_icu_admissions float(8) DEFAULT NULL,
	weekly_hosp_admissions float(8) DEFAULT NULL,
	PRIMARY KEY (date, country_code)
);

-- Table structure for table World_tests

DROP TABLE IF EXISTS World_tests;
CREATE TABLE World_tests (
	country_code varchar(15) NOT NULL,
	date DATE NOT NULL,
	total_tests float(8) DEFAULT NULL,
	new_tests float(8) DEFAULT NULL,
	new_tests_smoothed float(8) DEFAULT NULL,
	positive_rate float(8) DEFAULT NULL,
	tests_per_case float(8) DEFAULT NULL,
	PRIMARY KEY (date, country_code)
);

-- Table structure for table World_vaccine

DROP TABLE IF EXISTS World_vaccine;
CREATE TABLE World_vaccine (
	country_code varchar(15) NOT NULL,
	date DATE NOT NULL,
	total_vaccinations float(8) DEFAULT NULL,
	people_vaccinated float(8) DEFAULT NULL,
	people_fully_vaccinated float(8) DEFAULT NULL,
	total_boosters float(8) DEFAULT NULL,
	new_vaccinations float(8) DEFAULT NULL,
	new_vaccinations_smoothed float(8) DEFAULT NULL,
	new_people_vaccinated_smoothed float(8) DEFAULT NULL,
	PRIMARY KEY (date, country_code)
);

-- --------------------------------------------------------

END TRANSACTION;

