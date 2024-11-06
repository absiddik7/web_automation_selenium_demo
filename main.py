import pytest
from src.utils.helper_function import update_default_browser, update_headless_mode
import os
import subprocess

def main():
    args = ["-v", "-s", "--alluredir=./reports/allure-results"]  # Specify Allure results directory
    pytest.main(args + test_files)

    generate_allure_report()
    #serve_allure_report()

def generate_allure_report():
    # Full report generation
    #os.system("allure generate ./reports/allure-results -o ./reports/allure-report --clean")

    # Simple report generation
    os.system("allure generate --single-file ./reports/allure-results -o ./reports/allure-report --clean")
    
    
def serve_allure_report():
    subprocess.run(["allure", "serve", "./reports/allure-results"], shell=True)

if __name__ == "__main__":
    # Choose browser from "chrome" or "firefox"
    browser = "chrome"

    # Define headless mode - True or False
    headless = True

    # Update default browser setting
    update_default_browser(browser)

    # Update headless mode setting
    update_headless_mode(headless)

    # Specify the test files to run
    test_files = [
        "src/tests/login/test_login.py",
    ]

    # Run tests
    main()
