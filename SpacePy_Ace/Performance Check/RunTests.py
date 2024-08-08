# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 07:36:28 2024

@author: Ace Stratton

This will run all the tests and generate an output html
"""

import os
import pytest
from datetime import datetime

def main():
    # Define directories
    project_dir = os.getcwd()
    test_dir = os.path.join(project_dir, 'tests')
    report_dir = os.path.join(project_dir, 'reports')

    # Ensure the reports directory exists
    os.makedirs(report_dir, exist_ok=True)

    # Generate a report file name with the current date and time
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = os.path.join(report_dir, f'report_{now}.html')

    # Check if the virtual environment exists and activate it
    venv_activate_script = os.path.join(project_dir, 'venv', 'Scripts', 'activate_this.py')
    if os.path.exists(venv_activate_script):
        exec(open(venv_activate_script).read(), {'__file__': venv_activate_script})

    # Run pytest and generate the HTML report
    pytest_args = [test_dir, f'--html={report_file}', '--self-contained-html']
    pytest.main(pytest_args)

    # Modify the HTML report to include a custom title
    set_html_report_title(report_file, "My Test Report")

    print(f'Test report generated at {report_file}')

def set_html_report_title(report_file, title):
    # Read the contents of the report
    with open(report_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace the default title with the custom title
    content = content.replace('<title>Test Report</title>', f'<title>{title}</title>', 1)

    # Write the modified content back to the file
    with open(report_file, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == '__main__':
    main()
