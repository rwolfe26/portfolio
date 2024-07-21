import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import os
import time

def scrape_data():
    print("Starting data scrape...")

    login_url = "https://analytics.estrack.com/login"
    dashboard_url = "https://analytics.estrack.com/dashboard/fleet-utilization-dashboard-708?dashboardId=725&filters=eyJkYXRlUmFuZ2UiOnsic3RhcnQiOiIyMDI0LTA3LTA5IiwiZW5kIjoiMjAyNC0wNy0xNSIsImxhYmVsIjoibGFzdCA3IGRheXMifSwiYXNzZXRUeXBlIjpbIkVxdWlwbWVudCIsIlZlaGljbGUiXSwib3duZXJzaGlwIjoiQWxsIiwic2hvd0luUHJvZ3Jlc3NUcmlwcyI6Ik5vIiwic2hvd0Fzc2V0c05vQ29udGFjdCI6Ik5vIiwic2hvd1dlZWtlbmRzIjoiWWVzIiwidHJhY2tlckNhcGFiaWxpdHkiOlsiQUVNUCIsIkRhdGEgYW5kIExvY2F0aW9uIE9ubHkiXSwidXRpbGl6YXRpb25Ib3VycyI6WyI4IEhvdXJzIl0sImxhc3RMb2NhdGlvbiI6IkRlZmF1bHQiLCJqb2JOYW1lIjpbXSwicGhhc2VKb2JOYW1lIjpbXX0%3D"
    
    payload = {
        'username': '',
        'password': ''
    }

    with requests.Session() as session:
        # Login
        response = session.post(login_url, data=payload)
        if response.status_code != 200:
            print(f"Failed to login, status code: {response.status_code}")
            return
        print("Logged in successfully using requests.")

        # Get the cookies
        cookies = session.cookies.get_dict()

    # Use Selenium to load the dynamic content
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (no GUI)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the dashboard page
    driver.get(dashboard_url)
    
    # Add cookies to the driver
    for name, value in cookies.items():
        driver.add_cookie({'name': name, 'value': value, 'domain': '.estrack.com'})

    # Refresh the page to apply cookies
    driver.refresh()

    # Wait for the table to load
    try:
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.TAG_NAME, 'table'))
        )
        time.sleep(10)  # Additional sleep to ensure all dynamic content is loaded
        print("Page fully loaded.")
    except Exception as e:
        print(f"Page did not load in time: {e}")
        with open('debug_dashboard_page_source.html', 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        driver.quit()
        return

    # Parse the page content
    page_content = driver.page_source
    with open('debug_final_page_source.html', 'w', encoding='utf-8') as f:
        f.write(page_content)
        
    soup = BeautifulSoup(page_content, 'html.parser')
    table = soup.find('table')
    if not table:
        print("Table not found!")
        driver.quit()
        return

    print("Table found, extracting data...")

    # Extract headers
    headers = [header.text.strip() for header in table.find('thead').find_all('th')]
    print(f"Extracted headers: {headers}")

    # Extract rows
    rows = table.find('tbody').find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        data.append([col.text.strip() for col in cols])

    print(f"Extracted {len(data)} rows of data.")
    print(f"Data: {data}")

    # Create a DataFrame with the new data
    new_data_df = pd.DataFrame(data, columns=headers)
    print("DataFrame created.")

    # Define the path to the Excel file
    excel_file_path = 'fleet_utilization_data.xlsx'

    # Check if the Excel file already exists
    if os.path.exists(excel_file_path):
        # Load existing data
        existing_data_df = pd.read_excel(excel_file_path)
        print("Existing data loaded from Excel file.")

        # Append new data
        combined_df = pd.concat([existing_data_df, new_data_df], ignore_index=True)
        print("New data appended to existing data.")
    else:
        # No existing file, use new data as is
        combined_df = new_data_df
        print("No existing Excel file found, using new data as is.")

    # Export the combined data to Excel
    combined_df.to_excel(excel_file_path, index=False)
    print(f"Data successfully saved to {excel_file_path}")

    driver.quit()

# Run the function
scrape_data()
