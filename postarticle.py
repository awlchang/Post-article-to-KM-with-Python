# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select

chromedriver = "C:\\Users\\nschen\\Documents\\chromedriver.exe"
browser = webdriver.Chrome(chromedriver)

browser.get("http://km.mis.nsysu.edu.tw/")
browser.find_element_by_id("username").send_keys("account")
browser.find_element_by_id("password").send_keys("password")
browser.find_element_by_name('Submit').click()

browser.implicitly_wait(10)
all = browser.window_handles

browser.switch_to.window(browser.window_handles[-1])

frame = browser.find_element_by_xpath('//*[@id="s_sysbar"]')
browser.switch_to.frame(frame)
selector = Select(browser.find_element_by_name("selcourse"))
selector.select_by_visible_text(u"網路學習研究中心")

browser.switch_to.parent_frame()

frame = browser.find_element_by_xpath('//*[@id="s_catalog"]')
browser.switch_to.frame(frame)
browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="pathtree"]'))
browser.find_element_by_xpath('//*[@id="I_SCO_10010082_1437963668901"]/span/a[@title="張偉倫的研究專區"]')

browser.switch_to.default_content()

frame = browser.find_element_by_xpath('//*[@id="s_main"]')
browser.switch_to.frame(frame)
browser.find_element_by_xpath('//input[@value="張貼"]').click()

browser.find_element_by_name("subject").send_keys("weekly report(7/16-20) & plan(7/23-27) ")
browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe'))
browser.find_element_by_xpath("/html/body").send_keys("\
Completed (7/16-20)\n\
‧    7/17(二)到雲科與黃國豪老師的團隊開穿戴技術討論會議\n\
‧    程式訓練課程\n\
      ‧Raspberry Pi 3介紹和系統環境建置\n\
")
browser.switch_to.parent_frame()
browser.find_element_by_id('btnPost').click()