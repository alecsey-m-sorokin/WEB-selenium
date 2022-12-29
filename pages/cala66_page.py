# this is a sample page file

class Cala66Page(BasePage):
    """ Cala66 page.
    """
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.stand_url = settings.stand_url
        self.reddy_chat = settings.id_reddy

    def games_page_link(self, locator) -> BaseElement:
        """ button 'GAMES' top page menu """
        return BaseElement(self.driver, locator)

    def more_games_button(self, locator) -> BaseElement:
        """ button 'MORE GAMES' our games page """
        return BaseElement(self.driver, locator)

    def click_game(self, locator) -> BaseElement:
        """ click selected game """
        locator = (By.XPATH, locator)
        return BaseElement(self.driver, locator)

    def screenshot(self, filename='screenshot.png'):
        print(f'saved_file = {filename}')
        self.driver.save_screenshot(filename)

    def check_stand_state(self, **data):
        start_time = datetime.now()
        base_page = BasePage(self.driver)
        response = HttpMethods.get(data['test_stand'], params=None, headers={"Connection": "close"})
        # response.status_code = 500
        self.driver.get(data['test_stand'])
        text = "This page could not be found."
        result = base_page.check_exists_in_page_source(text)
        print(f'result "{text}" для ресурса "{data["test_stand"]}" = {result}')

        if response.status_code == 404 and result or response.status_code == 500:
            for _ in range(0, data['retries']):  # повтор запроса на ресурс 3 раза
                try:
                    time.sleep(data['time_out'])  # с интервалом timeOut
                    response = HttpMethods.get(data['test_stand'], params=None, headers={"Connection": "close"})
                    # response.status_code = 500
                    self.driver.get(data['test_stand'])
                    # self.driver.refresh()
                    text = "This page could not be found."
                    result = self.check_exists_in_page_source(text)
                    if response.status_code == 404 and result or response.status_code == 500:
                        print(f'ресурс "{data["test_stand"]}" недоступен. Попытка = {_}. Код ошибки {response.status_code}')
                        text_bot_1 = f'ресурс [url={data["test_stand"]}]{data["test_stand"]}[/url] недоступен. Попытка = {_+1} после {data["time_out"]} секунд времени. Код ошибки {response.status_code}\n' \
                                     f'Timeout = {datetime.now() - start_time}'
                        Reddy(to_reddy=True, game_line=data['game_line']).send_message2reddy(text_bot_1)
                    elif response.status_code == 200 and not result:
                        print(f'ресурс "{data["test_stand"]}" доступен. Код response = {response.status_code}')
                except Exception as E:
                    print(f'\nчто то пошло не так при проверке ресурса "{data["test_stand"]}" на 404 ошибку и доступность страницы,\nошибка = {E}\n'
                          f'Timeout = {datetime.now() - start_time}')
                    text_bot_1 = f'\nчто то пошло не так при проверке ресурса [url={data["test_stand"]}]{data["test_stand"]}[/url] на 404 ошибку и доступность страницы,\nошибка = {E}\n' \
                                 f'Timeout = {datetime.now() - start_time}'
                    Reddy(to_reddy=True, game_line=data['game_line']).send_message2reddy(text_bot_1)

        return response.status_code, result
