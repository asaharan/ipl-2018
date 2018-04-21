from threading import Timer
from selenium import webdriver
timeout = 10*60 #10 minutes
url = raw_input("Enter the url:")
driver = "chrome"

def start():
    global browser
    global driver
    print "Starting", driver
    if driver == "chrome":
        browser = webdriver.Chrome()
    else:
        print "Unknown driver"
        print "Exiting..."
        return
    browser.get(url)
    

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
