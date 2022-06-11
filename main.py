from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui


def main() -> None:
    driver = webdriver.Chrome()
    driver.get("https://thetypingcat.com/typing-speed-test/1m")
    screen = driver.find_element_by_xpath('//*[@id="body"]/div/div/div[2]/div/div[2]/div[1]/div[1]/'
                                          + 'div/div/div[2]/div/div[1]/div/div[1]')
    print("waiting...")
    sleep(10)
    print("wait over")
    with open("log.txt", 'w') as log:
        while True:
            try:
                txt = screen.find_element(By.XPATH, '//*[@id="body"]/div/div/div[2]/div/div[2]/'
                                                    + 'div[1]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div[2]')
                line_active = txt.find_element(By.CSS_SELECTOR, ".line.active")
                line_to_type = str(line_active.text).replace('⏎', '\n')

            except: break
            pyautogui.typewrite(line_to_type, 0.05)
            log.write(line_to_type)


if __name__ == "__main__":
    main()
    print("Finished executing")
