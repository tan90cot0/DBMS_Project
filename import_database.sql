BEGIN TRANSACTION;

COPY Country_Code FROM '/Users/aryan/Desktop/DBMS_Project/data/country_code.csv' WITH CSV HEADER DELIMITER AS ',';
COPY Country_Continent FROM '/Users/aryan/Desktop/DBMS_Project/data/country_continent.csv' WITH CSV HEADER DELIMITER AS ',';
COPY Country FROM '/Users/aryan/Desktop/DBMS_Project/data/country.csv' WITH CSV HEADER DELIMITER AS ',';
COPY Hosp_defence FROM '/Users/aryan/Desktop/DBMS_Project/data/hosp_defence.csv' WITH CSV HEADER DELIMITER AS ',';
COPY Hosp_gov FROM '/Users/aryan/Desktop/DBMS_Project/data/hosp_gov.csv' WITH CSV HEADER DELIMITER AS ',';
COPY Hosp_railways FROM '/Users/aryan/Desktop/DBMS_Project/data/hosp_railways.csv' WITH CSV HEADER DELIMITER AS ',';
COPY India_cases FROM '/Users/aryan/Desktop/DBMS_Project/data/india_cases.csv' WITH CSV HEADER DELIMITER AS ',';
COPY India_tests FROM '/Users/aryan/Desktop/DBMS_Project/data/india_tests.csv' WITH CSV HEADER DELIMITER AS ','; 
COPY India_vaccine FROM '/Users/aryan/Desktop/DBMS_Project/data/india_vaccine.csv' WITH CSV HEADER DELIMITER AS ',';
COPY Patients FROM '/Users/aryan/Desktop/DBMS_Project/data/patients.csv' WITH CSV HEADER DELIMITER AS ',';
COPY State_cases FROM '/Users/aryan/Desktop/DBMS_Project/data/state_cases.csv' WITH CSV HEADER DELIMITER AS ',';
COPY State_tests FROM '/Users/aryan/Desktop/DBMS_Project/data/state_tests.csv' WITH CSV HEADER DELIMITER AS ','; 
COPY State_vaccine FROM '/Users/aryan/Desktop/DBMS_Project/data/state_vaccine.csv' WITH CSV HEADER DELIMITER AS ',';
COPY World_cases FROM '/Users/aryan/Desktop/DBMS_Project/data/world_cases.csv' WITH CSV HEADER DELIMITER AS ',';
COPY World_tests FROM '/Users/aryan/Desktop/DBMS_Project/data/world_tests.csv' WITH CSV HEADER DELIMITER AS ',';
COPY World_vaccine FROM '/Users/aryan/Desktop/DBMS_Project/data/world_vaccine.csv' WITH CSV HEADER DELIMITER AS ',';

END TRANSACTION;

