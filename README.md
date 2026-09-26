# Pandas Python Projects

Small, practical Python examples for learning pandas step by step.

This repository brings together examples for reading, exploring, cleaning, changing, joining, grouping, and saving tabular data. The files are beginner-friendly practice projects, so you can open one script at a time and learn by running it.

## Contents

- [What you can learn](#what-you-can-learn)
- [Getting started](#getting-started)
- [Run a project](#run-a-project)
- [Sample data](#sample-data)
- [Project files](#project-files)
- [Join guide](#join-guide)

## What You Can Learn

### Read and explore data

- Read CSV, Excel, and JSON files with **read_csv.py**, **read_excel.py**, **read_json.py**, and **read_project.py**.
- View the first or last rows with **head_tail.py**.
- Check columns, rows, and DataFrame details with **info.py** and **colum_shape.py**.
- Review summary statistics with **describe.py**.

### Select, filter, sort, and update

- Choose one or more columns with **single_multiple_column.py**.
- Filter rows with **row_filter.py**.
- Update values with **update.py**.
- Add a column with **add_column.py**.
- Sort rows with **sorting.py**.

### Clean and prepare data

- Find or handle missing values with **data_handle_missing.py**, **fill_handle.py**, and **dropna_handle.py**.
- Remove rows or columns with **delete.py**.

### Combine and group data

- Practice grouping with **group.py** and **multi_group.py**.
- Combine DataFrames with **concat.py**.
- Compare pandas join types with **join.py**.
- Join files interactively with **join_project.py**.

### Save data

- Export data to CSV with **save_csv.py**.
- Export data to Excel with **save_excel.py**.

### Try the larger projects

- **second_pandas_project.py** brings several common operations together in an interactive menu.
- **read_project.py** is an example project for reading and saving data in common formats.

## Getting Started

You need Python 3 and pandas. Excel examples may also need openpyxl.

1. Download or clone this repository and open a terminal in its folder.
2. (Optional) Create and activate a virtual environment.
3. Install the packages:

~~~bash
python -m pip install pandas openpyxl
~~~

To create a virtual environment:

~~~bash
python -m venv .venv
~~~

Activate it on Windows PowerShell:

~~~powershell
.venv\Scripts\Activate.ps1
~~~

Activate it on macOS or Linux:

~~~bash
source .venv/bin/activate
~~~

## Run a Project

Run a Python file from the repository folder. For example:

~~~bash
python second_pandas_project.py
~~~

Or run the interactive join example:

~~~bash
python join_project.py
~~~

Follow the prompts in the terminal. When a script asks for a file path, enter the path to your CSV, Excel, or JSON file. If your data file is in the repository folder, you can usually enter its filename.

Here is a small example of reading the included CSV file:

~~~python
import pandas as pd

df = pd.read_csv("sales_data_sample.csv")
print(df.head())
~~~

## Sample Data

The repository includes sample files you can use while practicing:

- **sales_data_sample.csv** — sample CSV data.
- **SampleSuperstore.xlsx** — sample Excel workbook.
- **output.json** — sample JSON data.

Use the filename when you run a script from the repository folder, or enter the full path if the file is somewhere else.

## Project Files

| File | What it demonstrates |
| --- | --- |
| **add_column.py** | Add a new column using user-provided values |
| **colum_shape.py** | Inspect DataFrame size and shape |
| **concat.py** | Concatenate DataFrames |
| **data_handle_missing.py** | Find missing values |
| **delete.py** | Remove rows or columns |
| **describe.py** | Display summary statistics |
| **dropna_handle.py** | Remove rows with missing values |
| **fill_handle.py** | Fill missing values |
| **group.py** | Group rows and summarize data |
| **head_tail.py** | Display the first or last rows |
| **info.py** | Inspect DataFrame information |
| **join.py** | Examples of inner, left, right, outer, and cross joins |
| **join_project.py** | Interactive joins for CSV, Excel, or JSON files |
| **linear_poly_time.py** | Practice filling missing values with interpolation methods |
| **multi_group.py** | Group by more than one column |
| **read_csv.py**, **read_excel.py**, **read_json.py** | Read common data file formats |
| **read_project.py** | Practice reading and saving common data formats |
| **row_filter.py** | Filter rows using conditions |
| **save_csv.py**, **save_excel.py** | Save DataFrames to files |
| **second_pandas_project.py** | Use several pandas operations from an interactive menu |
| **single_multiple_column.py** | Select one or more columns |
| **sorting.py** | Sort rows by one or more columns |
| **update.py** | Update DataFrame values |

## Join Guide

The detailed explanation of the join loop, key columns, join types, and examples is in [JOIN_GUIDE.md](JOIN_GUIDE.md).

## Learning Tip

Start with one small script, run it, and change one thing at a time. Try your own file after you understand the sample. This makes it easier to see how each pandas operation changes the DataFrame.
