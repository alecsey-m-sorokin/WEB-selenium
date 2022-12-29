import time
from random import randint

import pytest
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from cala66.locators.locators import Cala66GamePageData
from cala66.pages.base_element import BaseElement
from cala66.pages.base_page import BasePage
from cala66.pages.cala66_page import FindGameName, Cala66Page
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def get_games_id():
    games_result = []
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    base_page = BasePage(driver)
    driver.maximize_window()
    base_page.open_site(f'{"https://cala66.com/#our-games"}')
    cala66 = Cala66Page(driver)
    cala66.more_games_button(locator=Cala66GamePageData.gamePage_moreGames).click()
    locator = (By.CSS_SELECTOR, 'section#our-games img')
    results = base_page.find_all_elements_presence_by_locator(locator)
    random_game = randint(1, len(results))
    driver.execute_script("window.scrollTo(0,1500)")
    for _ in range(len(results)):
        game_src = results[_].get_attribute("src")
        game_id = game_src[game_src.rfind("/") + 1:game_src.rfind(".")]
        game_name = FindGameName(int(game_id)).get_game_name()[1]
        locator = f"(By.XPATH, '{Cala66GamePageData.gamePage_selectedGame % f'{_ + 1}'}')"
        print(f'{game_src} / {game_id} / {game_name} / {locator}')
        games_result.append({"gameId": game_id, "gameName": game_name, "gameURL": Cala66GamePageData.gamePage_selectedGame % f'{_ + 1}', "gameIframe": ""})

    for _ in range(2):
        cala66.click_game(Cala66GamePageData.gamePage_selectedGame % f'{_+1}').click()
        time.sleep(3)
        results = driver.find_element(By.CSS_SELECTOR, 'div > iframe')
        game_iframe = results.get_attribute("src")
        print(f'game_iframe = {game_iframe}')
        games_result[_].update({"gameIframe": game_iframe})
        driver.switch_to.frame(WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe'))))
        error = base_page.find_element_presence(locator=(By.CSS_SELECTOR, '#text'))
        print(f'"error.text" iframe игры "{games_result[_]["gameName"]}" = {error.text}')

        driver.switch_to.default_content()

        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]').click()
        time.sleep(1)

    return games_result


if __name__ == "__main__":
    get_games_id()
