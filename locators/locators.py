from selenium.webdriver.common.by import By


class Cala66MainPageData:
    mainPage_Games_XPATH = (By.XPATH, '//*[@id="__next"]/div[1]/header/div[1]/div[1]/a[1]')
    mainPage_Games_TEXT = (By.LINK_TEXT, 'GAMES')


class Cala66GamePageData:
    gamePage_sliderCatalog = (By.CSS_SELECTOR, 'section#our-games img')
    gamePage_selectedGame = '//*[@id="our-games"]/div/div[3]/a[%s]/span/span/img'
    gamePage_selectedGame_close = (By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[1]')
    gamePage_moreGames = (By.XPATH, '//section[@id="our-games"]/div/button')
    gamePage_iframeSelector = (By.XPATH, '//*[@id="root"]/div/div[1]/main/div/div[2]/div/div/iframe')

    gamePage_gamesCatalog = [
        {'gameName': 'Barry the Leprechaun', 'gameURL': 'https://mancalagaming.org/games/Barry_the_Leprechaun', 'gameIframe': ''},
        {'gameName': 'Neon Light Fruits', 'gameURL': 'https://mancalagaming.org/games/Neon_Light_Fruits', 'gameIframe': ''},
        {'gameName': 'Seth vs Horus', 'gameURL': 'https://mancalagaming.org/games/Seth_vs_Horus', 'gameIframe': ''},
        # {"gameName": 'Hot Fruits on MARS', "gameURL": 'https://mancalagaming.org/games/Hot_Fruits_on_MARS ', "gameIframe": 'bad_iframe'},
        {'gameName': 'Jewel_Mania', 'gameURL': 'https://mancalagaming.org/games/Jewel_Mania', 'gameIframe': ''},
        {'gameName': 'barsandbells', 'gameURL': 'https://mancalagaming.org/games/barsandbells', 'gameIframe': ''},
    ]
