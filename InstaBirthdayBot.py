#Import necessary libraries
from playwright.sync_api import sync_playwright
import datetime
import time

playwright = sync_playwright().start()
data = {'diya.kunwar':[datetime.datetime(2005,6,16),'Diya']}
if __name__ == '__main__':
    # today's date in format : DD-MM
    today = datetime.datetime.now().strftime("%d-%m")

for item in data:
        bday = data[item][0].strftime("%d-%m")
        if (today == bday): #Check if anyone in the dictionary has birthday today!
            url = 'https://www.instagram.com/'
            #USER INPUT
            username = input('Enter username: ')
            pwd = input('Enter password: ')
            msg = f"Many Many Happy Returns of the day dear {data[item][1]}!!"

            #
            def run(playwright):
                browser = playwright.chromium.launch(headless=False)
                #Open the browser
                context = browser.new_context() #try adding .new_page() here to save lines!!!!!!!!!!!!!!!
                #Open new page
                page = context.new_page()
                #Open Instagram
                page.goto(url)

                #Login to Instagram
                page.wait_for_selector('input[name="username"]')
                page.fill('input[name="username"]', username)
                page.fill('input[name="password"]', pwd)
                page.click('button[type="submit"]')
                time.sleep(1)

                #Open Messages
                page.wait_for_selector('path[d="M12.003 2.001a9.705 9.705 0 1 1 0 19.4 10.876 10.876 0 0 1-2.895-.384.798.798 0 0 0-.533.04l-1.984.876a.801.801 0 0 1-1.123-.708l-.054-1.78a.806.806 0 0 0-.27-.569 9.49 9.49 0 0 1-3.14-7.175 9.65 9.65 0 0 1 10-9.7Z"]')
                page.click('path[d="M12.003 2.001a9.705 9.705 0 1 1 0 19.4 10.876 10.876 0 0 1-2.895-.384.798.798 0 0 0-.533.04l-1.984.876a.801.801 0 0 1-1.123-.708l-.054-1.78a.806.806 0 0 0-.27-.569 9.49 9.49 0 0 1-3.14-7.175 9.65 9.65 0 0 1 10-9.7Z"]')
                time.sleep(.5)

                #Cancel Notification
                page.wait_for_selector('div[class="_a9-z"]')
                page.click('button[class ="_a9-- _ap36 _a9_1"]')
                time.sleep(1)

                #Search for the username in the search field and select the username
                page.click('path[d="M12.202 3.203H5.25a3 3 0 0 0-3 3V18.75a3 3 0 0 0 3 3h12.547a3 3 0 0 0 3-3v-6.952"]')
                page.fill('input[name="queryBox"]', username)
                page.click('input[name="ContactSearchResultCheckbox"]')
                page.click('div[class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x9bdzbf x1ypdohk x78zum5 x1f6kntn xwhw2v2 xl56j7k x17ydfre x1n2onr6 x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xn3w4p2 x5ib6vp xc73u3c x1tu34mt xzloghq"]')

                #Write the Birthday message for the person and send!
                page.fill('p[class="xat24cr xdj266r"]', msg)
                page.click('div[class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37 xfs2ol5"]')
                time.sleep(5)

            #Run the program!
            run(playwright)

        else: #if none had a birthday on the given date
            print('Nobody has birthday today!')