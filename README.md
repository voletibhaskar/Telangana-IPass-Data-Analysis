# Telangana-IPass-Data-Analysis

Analyzed a multivariate dataset "Telangana IPASS Data 2017-2022". Applied ETL methods to raw data to generate a clean master dataset. Applied Data Visualization techniques to generate unique inisghts about India's startup state's current standing in Investments, Employees etc.

## [Understand Telangana's Growth as the Fastest Growing State in India](https://medium.com/@bhaskarvoleti.curiousity/telangana-a-rising-economic-growth-story-for-india-481ecdf8f6fd)

## [Telangana Investment Data Analysis Webiste on Heroku](https://telangana-ipass-analysis.herokuapp.com/)

## Introduction to the Dataset

| Columns | Entries | About |
| ------------- | ------------- | ------------- |
| line_of_activity | 17282 | Activity Purpose of the Company |
| sector | 17279 | Sector of the Company | 
| investment | 17282 | Amount of Investment in Cr. | 
| number_of_employees | 17282 | Total no of employees employed by the company |
| application_date | 17282 | Application date of the Company |
| approval_date | 17282 | Approval date of the Company |
| progress_of_implementation | 17282 | Current standing of the company development |
| is_online | 17282 | Whether the company is running or not |
| social_status | 17282 | Social Status of the person who applied |
| district | 17282 | District Name |
| mandal | 17282 | Mandal Name |
| village | 17282 | Village Name |
| unit_name | 17282 | Name of the unit |
| in_online | 17282 | Whether the company is running or not |

Data Shape

* Columns - 18 
* Rows - 17282

Download Requirements:
1. Install [pip](https://pip.pypa.io/en/stable/installation/)
2. Install [python 3.9](https://docs.python.org/3/installing/index.html)
3. Install [VSCode](https://code.visualstudio.com/)
4. Install [Virtual Environment - venv](https://docs.python.org/3/library/venv.html)
5. Download all the csv files from the [Dataset Link](https://data.telangana.gov.in/dataset/telangana-industries-ts-ipass-data) and extract all the files under the folder name 'Telangana_Industries_TS_IPass'.
6. Install [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)
7. Install [MatplotLib](https://matplotlib.org/stable/users/installing/index.html)

Noteable Insights:
1. Average Investment in Telangana across all industries was 10.028852 with an average of 85 employees in every company.
2. Median Investment across Districts in Telangana are varied with Mahbubnagar, Medak, Rangareddy getting more than 1.02 Cr.
3. Highest investment in Telangana comes under Real Estate,Industrial Parks and IT Buildings	with a median amount of 129.50 Cr. followed by Thermal Power Plant with 87.0 Cr. and Solar and Other Renewable Energy with 73.4831 Cr. 

4. Top 7 Sectors in terms of Units are:

| Sector | No of Units |
| ------------- | ------------- |
| Pharmaceuticals and Chemicals  | 1077 |
| Plastic and Rubber  | 1112 |
| Granite and Stone Crushing  | 1264 |
| Cement, Cement & Concrete Products, Fly Ash Bricks  | 1690 |
| Agro based incl Cold Storages  | 2124 |
| Food Processing  | 3271 |
| Engineering  | 3311 |

### Project Status

- [x] Data Cleansing & Visualization v1.0
  - [x] Collected data from [Telangana IPass Dataset](https://data.telangana.gov.in/dataset/telangana-industries-ts-ipass-data) and generated a master dataset. Applied basic data cleaning techniques and generated visualizations under "Time_jupyter.ipynb" 
- [ ] Data Cleansing & Visualization v2.0
  - [x] Hosted an interactive streamlit website on Heroku [Telangana Investment Data Analysis](https://telangana-ipass-analysis.herokuapp.com/) using the existing "all_time_data.csv" master dataset. Created different categories such as "Sector Insights", "District Insights", "Investment Insights".
  - [x] Created a current [Telangana Investment Map]("https://www.google.com/maps/d/u/0/embed?mid=15PbXco8n_UAmg6XMnvwYX_paQy5g5BQ&ehbc=2E312F") with all the companies geo-tagged for easy understanding of position. (FYI: Still need to remove outliers without impacting the data).
  - [ ] Create a Dataset Selector for the latest dataset usability. Apply internal data cleansing techniques and generate analytics for the latest Telangana IPass Dataset with an optional choice of using pre-existing dataset. (FYI: Currently working on this.)
- [ ] Data Cleansing & Visualization v3.0
  - [ ] Host a multi-page React + Redux website on Heroku with multiple view selections for a generic Analytical Website.  
- [ ] Project Extension - Continous Integration
  - [ ] Generate re-usable code for simple re-traceability and re-usability.
  - [ ] Generate seperate folders and python files for ease of understanding. Functions -> Functions.py, Variables -> Variables.py
