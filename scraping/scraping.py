import re
import time

import pandas as pd
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

# the category for which we seek reviews
CATEGORY = "restaurants"
# the location
LOCATION = "Gare de Lyon, Paris"
# google's main URL
URL = "https://www.google.com/"
if __name__ == "__main__":
    with sync_playwright() as pw:
        # creates an instance of the Chromium browser and launches it
        browser = pw.chromium.launch(headless=False)
        # creates a new browser page (tab) within the browser instance
        page = browser.new_page()
        # go to url with Playwright page element
        page.goto(URL)
        # deal with cookies page
        page.click(".QS5gu.sy4vM")
        # write what you're looking for
        page.fill("textarea", f"{CATEGORY} near {LOCATION}")
        # press enter
        page.keyboard.press("Enter")
        # change to english
        # page.locator("text='Change to English'").click()
        # time.sleep(4)
        # click in the "Maps" HTML element
        page.click(".GKS7s")
        time.sleep(4)
        # scrolling
        for i in range(2):
            # tackle the body element
            html = page.inner_html("body")
            # create beautiful soup element
            soup = BeautifulSoup(html, "html.parser")
            # select items
            categories = soup.select(".hfpxzc")
            last_category_in_page = categories[-1].get("aria-label")
            # scroll to the last item
            last_category_location = page.locator(f"text={last_category_in_page}")
            last_category_location.scroll_into_view_if_needed()
            # wait to load contents
            time.sleep(4)
        # get links of all categories after scroll
        links = [item.get("href") for item in soup.select(".hfpxzc")]
        names = []
        scores = []
        addresses = []
        for link in links:
            # go to subject link
            page.goto(link)
            time.sleep(4)
            try:
                name = re.search(r"place/(.*?),", link).group(1).replace("+", " ")
            except:
                name = re.search(r"place/(.*?)/", link).group(1).replace("+", " ")
            main_html = page.inner_html("body")
            main_soup = BeautifulSoup(html, "html.parser")
            short_html = main_html[: main_html.find('data-item-id="address"')]
            pattern_address = r'aria-label="([^"]*)"'
            address = re.findall(pattern_address, short_html)[-1]
            address = address[len("Adresse: ") :]
            page.locator("text='Avis'").first.click()
            time.sleep(4)
            # create new soup
            html = page.inner_html("body")
            # create beautiful soup element
            soup = BeautifulSoup(html, "html.parser")
            # scrape reviews
            score = soup.select(".fontDisplayLarge")
            score = score[0].text
            names.append(name)
            scores.append(score)
            addresses.append(address)

df = pd.DataFrame(
    {
        "noms": names,
        "notes": scores,
        "adresse": addresses,
        "lien": links,
    }
)
df.to_csv("data/scraping.csv", index=False)
