__author__='mardasov'
import selenium
from selenium import webdriver

def main():
    print('Hello, world!')
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://www.di.fm/channels')
    link_headlines = driver.find_elements_by_css_selector('div.channel-list > ul > li > div.info > h3.title > a')
    for link_headline in link_headlines:
        print(link_headline.text)
        if (link_headline.text == 'AMBIENT'):
            link_headline.click()
            break
    link_button_tune = driver.find_element_by_css_selector('div.controls-region > ul.controls > li.tune-in')
    link_button_tune.click()

if __name__ == '__main__':
    main()