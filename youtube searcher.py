from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from time import sleep

class ChromeAuto:
    def __init__(self):
        self.driver_path = "chromedriver.exe"
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r"user-data-dir=E:\Users\Mathe\Documents\novoselenium\Perfil")
        self.chrome = webdriver.Chrome(service = Service(
         self.driver_path,
        ))


    def pesquisa(self,pesquisa):
        try:
            btn_search = self.chrome.find_element(By.NAME, "search_query")
            btn_search.send_keys(pesquisa)
            # btn_search.send_keys(Keys.ENTER)

        except Exception as e :
            print("Erro em pesquisa:", e)

    def acess(self):
        self.chrome.get("https://www.youtube.com")

    def sair(self):
        self.chrome.quit()

    def clica(self):
        try:
            btn_search = self.chrome.find_element(By.ID, "search-icon-legacy")
            btn_search.click()
        except Exception as e:
            print("Erro em clica:", e)

    def clica_video(self):
        try:
            video = self.chrome.find_element(By.CSS_SELECTOR, "#video-title > yt-formatted-string")
            video.click()
        except Exception as e:
            print("Erro ao clicar no video:", e)


if __name__ == "__main__":
    pesquisa = input("O que voce quer pesquisar no youtube: ")
    chrome = ChromeAuto()
    chrome.acess()
    chrome.pesquisa(pesquisa)
    chrome.clica()
    sleep(2)
    chrome.clica_video()


