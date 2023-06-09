# Generated by Django 4.2 on 2023-04-26 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('population', models.DecimalField(decimal_places=1, max_digits=11, null=True)),
                ('life_expectancy', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('hospital_beds_per_thousand', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('handwashing_facilities', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('male_smokers', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('female_smokers', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('diabetes_prevalence', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('cardiovasc_death_rate', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('extreme_poverty', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('gdp_per_capita', models.DecimalField(decimal_places=3, max_digits=9, null=True)),
                ('aged_70_older', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('aged_65_older', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('median_age', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('population_density', models.DecimalField(decimal_places=3, max_digits=8, null=True)),
                ('stringency_index', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country_Code',
            fields=[
                ('name', models.CharField(max_length=40, null=True)),
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Country_Continent',
            fields=[
                ('continent_name', models.CharField(max_length=15, null=True)),
                ('country_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hosp_defence',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('no_hospitals', models.IntegerField(null=True)),
                ('no_beds', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hosp_gov',
            fields=[
                ('state_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('rural_hosp', models.IntegerField(null=True)),
                ('rural_beds', models.IntegerField(null=True)),
                ('urban_hosp', models.IntegerField(null=True)),
                ('urban_beds', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hosp_railways',
            fields=[
                ('zone', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('no_hospitals', models.IntegerField(null=True)),
                ('no_beds', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='India_cases',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('conf', models.IntegerField(null=True)),
                ('total_conf', models.IntegerField(null=True)),
                ('rec', models.IntegerField(null=True)),
                ('total_rec', models.IntegerField(null=True)),
                ('deceased', models.IntegerField(null=True)),
                ('total_deceased', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='India_tests',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('total_samples', models.DecimalField(decimal_places=1, max_digits=9, null=True)),
                ('total_positive', models.IntegerField(null=True)),
                ('tpcc', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('tpm', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='India_vaccine',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('total_doses', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('sessions', models.DecimalField(decimal_places=1, max_digits=9, null=True)),
                ('sites', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('first_dose', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('second_dose', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('male', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('female', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('trans', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('covaxin', models.DecimalField(decimal_places=1, max_digits=9, null=True)),
                ('covishield', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('sputnikv', models.DecimalField(decimal_places=1, max_digits=7, null=True)),
                ('doses_18to44', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('doses_45to60', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('doses_60plus', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('date', models.DateField(null=True)),
                ('patient_no', models.IntegerField(primary_key=True, serialize=False)),
                ('age', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('city', models.CharField(max_length=40, null=True)),
                ('district', models.CharField(max_length=30, null=True)),
                ('state', models.CharField(max_length=40, null=True)),
                ('state_code', models.CharField(max_length=2, null=True)),
                ('nationality', models.CharField(max_length=50, null=True)),
                ('transmission', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State_cases',
            fields=[
                ('record_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField(null=True)),
                ('state_code', models.CharField(max_length=2, null=True)),
                ('conf', models.IntegerField(null=True)),
                ('rec', models.IntegerField(null=True)),
                ('deceased', models.IntegerField(null=True)),
                ('state_name', models.CharField(max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State_tests',
            fields=[
                ('record_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField(null=True)),
                ('state', models.CharField(max_length=40, null=True)),
                ('total_test', models.DecimalField(decimal_places=1, max_digits=8, null=True)),
                ('positive', models.DecimalField(decimal_places=1, max_digits=7, null=True)),
                ('negative', models.DecimalField(decimal_places=0, max_digits=7, null=True)),
                ('unconfirmed', models.DecimalField(decimal_places=1, max_digits=7, null=True)),
                ('total_quarantine', models.DecimalField(decimal_places=1, max_digits=7, null=True)),
                ('total_quarantine_released', models.DecimalField(decimal_places=1, max_digits=8, null=True)),
                ('people_icu', models.DecimalField(decimal_places=1, max_digits=7, null=True)),
                ('people_venti', models.DecimalField(decimal_places=1, max_digits=7, null=True)),
                ('num_iso_beds', models.DecimalField(decimal_places=1, max_digits=7, null=True)),
                ('num_icu_beds', models.DecimalField(decimal_places=1, max_digits=7, null=True)),
                ('num_venti', models.DecimalField(decimal_places=1, max_digits=7, null=True)),
                ('tpm', models.DecimalField(decimal_places=1, max_digits=7, null=True)),
                ('tpcc', models.DecimalField(decimal_places=1, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State_vaccine',
            fields=[
                ('record_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField(null=True)),
                ('state', models.CharField(max_length=40, null=True)),
                ('total_doses', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('sessions', models.DecimalField(decimal_places=1, max_digits=9, null=True)),
                ('sites', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('first_dose', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('second_dose', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('male', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('female', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('trans', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('covaxin', models.DecimalField(decimal_places=1, max_digits=9, null=True)),
                ('covishield', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('sputnikv', models.DecimalField(decimal_places=1, max_digits=7, null=True)),
                ('doses_18to44', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('doses_45to60', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
                ('doses_60plus', models.DecimalField(decimal_places=1, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='World_cases',
            fields=[
                ('record_id', models.IntegerField(primary_key=True, serialize=False)),
                ('country_code', models.CharField(max_length=15, null=True)),
                ('date', models.DateField(null=True)),
                ('total_cases', models.DecimalField(decimal_places=1, max_digits=11, null=True)),
                ('new_cases', models.DecimalField(decimal_places=1, max_digits=9, null=True)),
                ('new_cases_smoothed', models.DecimalField(decimal_places=1, max_digits=9, null=True)),
                ('total_deaths', models.DecimalField(decimal_places=1, max_digits=8, null=True)),
                ('new_deaths', models.DecimalField(decimal_places=1, max_digits=8, null=True)),
                ('new_deaths_smoothed', models.DecimalField(decimal_places=1, max_digits=8, null=True)),
                ('reproduction_rate', models.DecimalField(decimal_places=1, max_digits=4, null=True)),
                ('icu_patients', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('hosp_patients', models.DecimalField(decimal_places=1, max_digits=7, null=True)),
                ('weekly_icu_admissions', models.DecimalField(decimal_places=1, max_digits=6, null=True)),
                ('weekly_hosp_admissions', models.DecimalField(decimal_places=1, max_digits=7, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='World_tests',
            fields=[
                ('record_id', models.IntegerField(primary_key=True, serialize=False)),
                ('country_code', models.CharField(max_length=15, null=True)),
                ('date', models.DateField(null=True)),
                ('total_tests', models.DecimalField(decimal_places=1, max_digits=11, null=True)),
                ('new_tests', models.DecimalField(decimal_places=1, max_digits=9, null=True)),
                ('new_tests_smoothed', models.DecimalField(decimal_places=1, max_digits=9, null=True)),
                ('postive_rate', models.DecimalField(decimal_places=5, max_digits=8, null=True)),
                ('tests_per_case', models.DecimalField(decimal_places=1, max_digits=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='World_vaccine',
            fields=[
                ('record_id', models.IntegerField(primary_key=True, serialize=False)),
                ('country_code', models.CharField(max_length=15, null=True)),
                ('date', models.DateField(null=True)),
                ('total_vaccinations', models.DecimalField(decimal_places=1, max_digits=11, null=True)),
                ('people_vaccinated', models.DecimalField(decimal_places=1, max_digits=11, null=True)),
                ('people_fully_vaccinated', models.DecimalField(decimal_places=1, max_digits=11, null=True)),
                ('total_boosters', models.DecimalField(decimal_places=1, max_digits=11, null=True)),
                ('new_vaccinations', models.DecimalField(decimal_places=1, max_digits=9, null=True)),
                ('new_vaccinations_smoothed', models.DecimalField(decimal_places=1, max_digits=9, null=True)),
                ('new_people_vaccinated_smoothed', models.DecimalField(decimal_places=1, max_digits=9, null=True)),
            ],
        ),
    ]
