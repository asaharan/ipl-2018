from threading import Timer
from selenium import webdriver
timeout = 10*60 #10 minutes
url = raw_input("Enter the url:")
driver = "chrome"
#Hotstar fullscreen button selector
fullscreen_button_css_selector = "#my_video_1 > div.vjs-control-bar.vjs-dvrseekbar-control-bar > button.vjs-fullscreen-control.vjs-control.vjs-button"
def focus():
    browser.execute_script("window.focus();")
    # browser.switch_to_window(browser.current_window_handle)
    fullscreen_button = browser.find_element_by_css_selector(fullscreen_button_css_selector)
    fullscreen_button.click()

def start():
    global browser
    global driver
    print "Starting", driver
    if driver == "chrome":
        browser = webdriver.Chrome()
    else:
        if driver == "gecko":
            browser = webdriver.Firefox()
        else:
            print "Unknown driver"
            print "Exiting..."
            return
    # browser.maximize_window()
    browser.get(url)
    s = Timer(10,focus)
    s.start()
    

def reopen():
    global browser
    print "Closing browser"
    browser.close()
    print "Closed browser"
    start()
    setTimeout()

def setTimeout():
    global r
    global timeout
    print "Setting timeout"
    r = Timer(timeout, reopen)
    r.start()
    print "Timeout set for", timeout / 60, "minutes"


start()
setTimeout()
