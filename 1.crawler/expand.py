from selenium import webdriver
import time

"""
url: the douban page we will get html from
loadmore: whether or not click load more on the bottom 
waittime: seconds the broswer will wait after intial load and 
"""
#sdf

def getHtml(url, loadmore=False, waittime=5):
    browser = webdriver.Chrome('chromedriver')
    browser.get(url)

    time.sleep(waittime)
    #count = 0
    if loadmore:
        while True:
        #while count < 1:
            try:
                next_button = browser.find_element_by_class_name("more")
                next_button.click()
                time.sleep(waittime)
                #count += 1
            except:
                break
    html = browser.page_source
    # print(html)
    browser.quit()
    return html


# for test
# url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,剧情,美国"
# html = getHtml(url)
# print(html)
