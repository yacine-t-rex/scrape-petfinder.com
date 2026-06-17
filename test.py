from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

driver = webdriver.Chrome()

paths = [
    "https://www.petfinder.com/search/dogs-for-adoption/us/il/chicago",
    "https://www.petfinder.com/search/cats-for-adoption/us/il/chicago"
]

for path in paths:

    driver.get(path)
    #time.sleep(random.uniform(3, 6))
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.PFPetDetailCard_flipWrapper__Wd3__")
        )
    )

    cards = driver.find_elements(
        By.CSS_SELECTOR,
        "div.PFPetDetailCard_flipWrapper__Wd3__"
    )

    print(f"Found {len(cards)} cards")
    profile_urls = []
    for card in cards:
       try:
           link = card.find_element(
                  By.CSS_SELECTOR,
                  'a[href*="/details/"]'
           )
           href = link.get_attribute("href")
           profile_urls.append(href)
       except:
          pass

    print(profile_urls)

    for url in profile_urls:
        #time.sleep(random.uniform(3, 8))
        driver.get(url)

    # attendre que la page soit chargée
        WebDriverWait(driver, 30).until(
             EC.presence_of_element_located(
            (By.ID, "pet-details-about-section")
             )
        )

        name=driver.find_element(By.CSS_SELECTOR,"section#abbreviatedCard h1")
        print(name)

driver.quit()