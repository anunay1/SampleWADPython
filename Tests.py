import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class SampleTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        desired_caps = {}
        desired_caps['app'] = "root"
        desired_caps['platformName'] = "Windows"
        self.desktopSession = webdriver.Remote(
            command_executor="http://127.0.0.1:4725/wd/hub",
            desired_capabilities=desired_caps)

        rs_window = self.desktopSession.find_element(AppiumBy.NAME("RobotStudio"))
        rs_windowHandle = rs_window.get_attribute("NativeWindowHandle")
        topLevelWindow = format(int(rs_windowHandle), 'x')

        desired_caps = {}
        desired_caps["appTopLevelWindow"] = topLevelWindow
        desired_caps['platformName'] = "Windows"
        self.desktopSession1 = webdriver.Remote(
            command_executor="http://127.0.0.1:4725/wd/hub",
            desired_capabilities=desired_caps
        )

        self.desktopSession1.find_element(AppiumBy.NAME("CmdBarCtl_VirtualFlexPendant")).click()

        desired_caps = {}
        desired_caps['app'] = "root"
        desired_caps['platformName'] = "Windows"
        self.desktopSession2 = webdriver.Remote(
            command_executor="http://127.0.0.1:4725/wd/hub",
            desired_capabilities=desired_caps)

        vp_window = self.desktopSession2.find_element(AppiumBy.NAME("Virtual FlexPendant"))
        vp_windowHandle = vp_window.get_attribute("NativeWindowHandle")
        vp_topLevelWindow = format(int(vp_windowHandle), 'x')

        desired_caps = {}
        desired_caps["appTopLevelWindow"] = vp_topLevelWindow
        desired_caps['platformName'] = "Windows"

        self.desktopSession3 = webdriver.Remote(
            command_executor="http://127.0.0.1:4725/wd/hub",
            desired_capabilities=desired_caps)

        self.desktopSession3.find_element(AppiumBy.ACCESSIBILITY_ID("ABBbutton")).click()
        self.desktopSession3.update_settings({"imageMatchThreshold": 0.9})
        self.desktopSession3.find_element(AppiumBy.IMAGE("C:\Images\Systeminfo.jpeg")).click()
        sleep(2)
    @classmethod
    def Teardown(self):
        self.desktopSession.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SampleTest)
    unittest.TextTestRunner(verbosity=2).run(suite)