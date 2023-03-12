# Automation tests for simple html form
This is a simple project for testing using **Pytest** and **Selenium**.
Example report is available in the repository: _report.html_
These tests are made just for Chrome browser.

### Prerequisites
In order to run these tests:
  - **Chrome Web Browser** and compatible ChromeDriver
  - **Python 3** are needed

### Run project
Get clone from this repo

Open cmd

Run commands:
```
cd "the_repo_folder_path"
pip install pip
pip install -r requirements.txt
```
Run tests:
* Just for run all of the tests put:
```
pytest
```
* For run tests with the report:
```
pytest --html=report.html
```
