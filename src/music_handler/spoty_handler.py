from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


class Musica:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def music(self, busqueda):
        print("estoy en musica")

        # Optional argument, if not specified will search path.
        print(busqueda)
        self.driver.get(f'https://www.youtube.com/results?search_query={busqueda}')
        time.sleep(5)  # Let the user actually see something!
        first_song = self.driver.find_elements_by_xpath('//*[@id="video-title"]')
        first_song[0].click()
        time.sleep(30)

    def para(self):
        self.driver.quit()
