import argparse

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

parser = argparse.ArgumentParser(description="Open url with firefox webdriver")
parser.add_argument("--url", type=str, required=True, help="url to open in browser")

args = parser.parse_args()

service = Service(log_path="/dev/null")
driver = webdriver.Firefox(service=service)
driver.get(args.url)
