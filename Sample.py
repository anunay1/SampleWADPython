
from time import sleep
from appium import webdriver
#from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def Test1():
    try:

        desired_caps = {}
        desired_caps['app'] = "Root"
        desired_caps['platformName'] = "Windows"
        driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4725/wd/hub",
            desired_capabilities=desired_caps)

        print('Window Handles: ',driver.window_handles)

        rs_window = driver.find_element(By.NAME,"Solution6 - RobotStudio [Internal build 21.3.9543.0]")
        rs_windowHandle = rs_window.get_attribute("NativeWindowHandle")
        topLevelWindow = format(int(rs_windowHandle), 'x')

        desired_caps = {}
        desired_caps["appTopLevelWindow"] = topLevelWindow
        desired_caps['platformName'] = "Windows"
        desktopSession1 = webdriver.Remote(
            command_executor="http://127.0.0.1:4725/wd/hub",
            desired_capabilities=desired_caps)

        desktopSession1.find_element(By.NAME,"CmdBarCtl_VirtualFlexPendant").click()

        desired_caps = {}
        desired_caps['app'] = "Root"
        desired_caps['platformName'] = "Windows"
        desktopSession2 = webdriver.Remote(
            command_executor="http://127.0.0.1:4725/wd/hub",
            desired_capabilities=desired_caps)

        vp_window = desktopSession2.find_element(By.NAME,"Virtual FlexPendant")
        vp_windowHandle = vp_window.get_attribute("NativeWindowHandle")
        vp_topLevelWindow = format(int(vp_windowHandle), 'x')

        desired_caps = {}
        desired_caps["appTopLevelWindow"] = vp_topLevelWindow
        desired_caps['platformName'] = "Windows"

        desktopSession3 = webdriver.Remote(
            command_executor="http://127.0.0.1:4725/wd/hub",
            desired_capabilities=desired_caps)

        desktopSession3.find_element_by_accessibility_id("ABBbutton").click()
        sleep(5)
        desktopSession3.update_settings({"imageMatchThreshold": 0.5})
        desktopSession3.update_settings({"getMatchedImageResult": True})
        #desktopSession3.update_settings({"imageMatchMethod":"TM_SQDIFF_NORMED" })
        smiliarity = desktopSession3.find_elements_by_image("C:\Images\Systeminf.png")
        smiliarity[1].click()
        score = desktopSession3.find_element_by_image("C:\Images\Systeminf.png").get_attribute("score")
        location = smiliarity.location
        x = location.get("x")
        y = location.get("y")
        action = ActionChains(desktopSession3)
        action.move_to_element(smiliarity)
        smiliarity.click()
        desktopSession3.find_element_by_image("C:\Images\Systeminf.png").click()
        sleep(2)

    except Exception as exception:
        print(exception)

def getAppDriver(self, classname):
        # Launch a driver for the Windows Desktop (Root)
    desired_caps = {}
    desired_caps["app"] = "Root"
    desktop = self.launchApp(desired_caps)

        # Use the desktop driver to locate the window for Edge browser
    win = WebDriverWait(desktop, 120).until(EC.presence_of_element_located((By.CLASS_NAME,classname)))
        # Get an app driver for Edge from the window
    app_driver = self.getDriverFromWin(win)
    return app_driver

def getDriverFromWin(self, win):
    win_handle1 = win.get_attribute("NativeWindowHandle")
    win_handle = format(int(win_handle1), 'x') # convert to hex string

        # Launch new session attached to the window
    desired_caps = {}
    desired_caps["appTopLevelWindow"] = win_handle
    driver = self.launchApp(desired_caps)
    driver.switch_to_window(win_handle)
    return driver

def launchApp(self, desired_caps):
    dut_url = "http://" + self.dut_ip + ":" + self.app_port
    driver = webdriver.Remote(
            command_executor = dut_url,
            desired_capabilities = desired_caps)
    return driver

if __name__ == '__main__':
    Test1()