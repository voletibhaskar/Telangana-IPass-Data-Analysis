# Telangana-IPass-Data-Analysis
## Introduction to the Dataset

[Dataset Link](https://data.telangana.gov.in/dataset/telangana-industries-ts-ipass-data)

| Columns | Entries  |
| ------------- | ------------- |
| district_name  | 4316  |
| mandal_name | 4316  |
| village_name | 4316  |
| name_of_the_unit | 4316  |
| line_of_activity | 17282  |
| sector | 17279  |
| investment | 17282  |
| number_of_employees | 17282  |
| application_date | 17282  |
| approval_date | 17282  |
| progress_of_implementation | 17282  |
| is_online | 4316  |
| social_status | 17282  |
| district | 12966  |
| mandal | 12966  |
| village | 12966  |
| unit_name | 12966  |
| in_online | 12966  |

Data Shape

* Columns - 18 
* Rows - 17282

Requirements:
1. Download all the csv files from the link and extract all the files under the folder name 'Telangana_Industries_TS_IPass'.
2. Installation of all the requirements.
   - Pandas
   - csv
   - os

## GPU System Installation for Windows 11
1. Install pip
2. Install python 3.9
3. Install VSCode and install Virtual Environment - venv

### To run venv we need to initiate the following command:
```
Set-ExecutionPolicy Unrestricted -Scope Process
```

### Enter the following code to initialize the Virtual Environment Testenv:
```
 & "d:/Linkedin Learning/PythonTraining/Testenv/Scripts/Activate.ps1"
 & "d:/Linkedin Learning/PythonTraining/Testenv/Scripts/python.exe" "d:/Linkedin Learning/PythonTraining/Time_Series_Analysis/Time_Series.py"
```

#### If we have to install GPU we need to follow the following: 

 - Install Visual Studio (2019) for Windows 10/11 for CUDA and CUDANN
 - After Visual Studio installation install CUDA (11.2) for 2019 as we can't install any other version as they are not compatible
 - Download CUDANN and extract the 3 files /bin, /lib, /include and copy them and replace them with the folders of CUDA GPU Toolkit
 - C:Users/Program Files/NVIDIA GPU Toolkit /CUDA.11/ 
 - Add the path of  C:Users/Program Files/NVIDIA GPU Toolkit /CUDA.11/bin folder as a path and save
 - Add the path of  C:Users/Program Files/NVIDIA GPU Toolkit /CUDA.11/libmnrv folder as a path and save


#### After installing GPU we need to add the following line to your code in the beginning if using VSCode:
```
 - import os 
 - os.add_dll_directory("C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.2/bin")
```
