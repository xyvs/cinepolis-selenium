from selenium.webdriver import Chrome
from pages.home import CinepolisHome
from pages.search import CinepolisSearch
from pages.details import CinepolisMovieDetail

if __name__ == "__main__":
    with Chrome() as driver:

        home = CinepolisHome(driver)
        home.load()
        home.change_city()
        home.change_cinema()

        search = CinepolisSearch(driver)
        search.change_hours()
        search.wait_for_movies()
        search.check_hours()
        search.choose_random_movie()

        details = CinepolisMovieDetail(driver)
        details.get_video()
        details.get_description()
