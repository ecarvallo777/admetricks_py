import argparse

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.firefox.service import Service

parser = argparse.ArgumentParser(description="Open url with firefox webdriver")
parser.add_argument("--url", type=str, required=True, help="url to open in browser")

args = parser.parse_args()
options = FirefoxOptions()
options.headless = True

service = Service(executable_path="/home/pin/.local/bin/geckodriver")
driver = webdriver.Firefox(options=options, service=service)
driver.get(args.url)
print("Finish")
