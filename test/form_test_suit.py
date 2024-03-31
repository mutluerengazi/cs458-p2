import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

def test_form(test_case, name, year, education, city, selected_genders, ai_names, cons, use, valid) -> None:
    name_element = test_case.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Name-surname"]')
    name_element.send_keys(name)

    birth_element = test_case.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Birth Year (YYYY)"]')
    birth_element.send_keys(year)

    education_element = test_case.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Education Level"]')
    education_element.send_keys(education)

    city_element = test_case.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="City"]')
    city_element.send_keys(city)

    for selected_gender in selected_genders:
        spinner_element = test_case.driver.find_element(AppiumBy.XPATH, '//android.widget.Spinner')
        spinner_element.click()

        gender_element = test_case.driver.find_element(AppiumBy.XPATH, f'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="{selected_gender}"]')
        gender_element.click()

    for ai_name in ai_names:
        ai_element = test_case.driver.find_element(AppiumBy.XPATH, f'//android.widget.TextView[@text="{ai_name}"]')
        ai_element.click()

    cons_element = test_case.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Defects or cons of the model(s)"]')
    cons_element.send_keys(cons)

    use_element = test_case.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Use case of AI in daily life"]')
    use_element.send_keys(use)

    try:
        test_case.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Send"]')

    except:
        if valid:
            raise "Send button is hidden for valid input!"
        
    else:
        if not valid:
            raise "Send button is present for invalid input!"

class TestForm(unittest.TestCase):
    def setUp(self) -> None:
        appium_server_url = 'http://localhost:4723'
        capabilities = dict(
            platformName='android',
            automationName='uiautomator2',
            appPackage='com.mutluerengazi.cs458p2',
            appActivity='.MainActivity',
        )
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_1_a(self) -> None:
        test_form(
            self, 
            name="Sahand Moslemi Yengejeh", 
            year="2000", 
            education="Graduate", 
            city="Ankara",
            selected_genders=["Male"],
            ai_names=["Bard"],
            cons="AI Cons",
            use="A Use Case",
            valid=True
        )
    
    def test_1_b(self) -> None:
        test_form(
            self, 
            name="Sahand Moslemi Yengejeh", 
            year="2000", 
            education="Graduate", 
            city="Ankara",
            selected_genders=["Male", "Female", "Other"],
            ai_names=["ChatGPT", "Bard", "Claude", "Copilot"],
            cons="AI Cons",
            use="A Use Case",
            valid=True
        )   
    
    def test_1_c(self) -> None:
        test_form(
            self, 
            name="Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature", 
            year="2000", 
            education="Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature", 
            city="Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature",
            selected_genders=["Male", "Female", "Other"],
            ai_names=["ChatGPT", "Bard", "Claude", "Copilot"],
            cons="Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature",
            use="Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature",
            valid=True
        )   

    def test_2_a(self) -> None:
        test_form(
            self, 
            name="Sah@!$and M!@$oslemi Yengejeh", 
            year="%!200@4", 
            education="Grad!@$uate", 
            city="Ank#!ara",
            selected_genders=["Male", "Female", "Other"],
            ai_names=["ChatGPT", "Bard", "Claude", "Copilot"],
            cons="AI Con@$!s",
            use="A Use Ca%!se",
            valid=False
        )

    def test_2_b(self) -> None:
        test_form(
            self, 
            name="Sah213and Mosle312mi Yengejeh", 
            year="2000", 
            education="Grad312uate", 
            city="312Ankara",
            selected_genders=["Male", "Female", "Other"],
            ai_names=["ChatGPT", "Bard", "Claude", "Copilot"],
            cons="AI Con321s",
            use="A Use 321Case",
            valid=False
        )

    def test_2_c(self) -> None:
        test_form(
            self, 
            name="Sahand Moslemi Yengejeh", 
            year="20dasd 04", 
            education="Graduate", 
            city="Ankara",
            selected_genders=["Male", "Female", "Other"],
            ai_names=["ChatGPT", "Bard", "Claude", "Copilot"],
            cons="AI Cons",
            use="A Use Case",
            valid=False
        )
    
    def test_3_a(self) -> None:
        test_form(
            self, 
            name="Sahand Moslemi Yengejeh", 
            year="1899", 
            education="Graduate", 
            city="Ankara",
            selected_genders=["Male", "Female", "Other"],
            ai_names=["ChatGPT", "Bard", "Claude", "Copilot"],
            cons="AI Cons",
            use="A Use Case",
            valid=False
        )       

    def test_3_b(self) -> None:
        test_form(
            self, 
            name="Sahand Moslemi Yengejeh", 
            year="2009", 
            education="Graduate", 
            city="Ankara",
            selected_genders=["Male", "Female", "Other"],
            ai_names=["ChatGPT", "Bard", "Claude", "Copilot"],
            cons="AI Cons",
            use="A Use Case",
            valid=False
        )   

    def test_4_a(self) -> None:
        test_form(
            self, 
            name="", 
            year="2009", 
            education="", 
            city="Ankara",
            selected_genders=["Male", "Female", "Other"],
            ai_names=["ChatGPT", "Bard", "Claude", "Copilot"],
            cons="AI Cons",
            use="A Use Case",
            valid=False
        )   

    def test_4_b(self) -> None:
        test_form(
            self, 
            name="Sahand Moslemi Yengejeh", 
            year="", 
            education="Graduate", 
            city="",
            selected_genders=["Male", "Female", "Other"],
            ai_names=["ChatGPT", "Bard", "Claude", "Copilot"],
            cons="AI Cons",
            use="A Use Case",
            valid=False
        )   

    def test_4_c(self) -> None:
        test_form(
            self, 
            name="Sahand Moslemi Yengejeh", 
            year="2009", 
            education="Graduate", 
            city="Ankara",
            selected_genders=[],
            ai_names=["ChatGPT", "Bard", "Claude", "Copilot"],
            cons="AI Cons",
            use="",
            valid=False
        )   

    def test_4_d(self) -> None:
        test_form(
            self, 
            name="Sahand Moslemi Yengejeh", 
            year="2009", 
            education="Graduate", 
            city="Ankara",
            selected_genders=["Male", "Female", "Other"],
            ai_names=[],
            cons="",
            use="A Use Case",
            valid=False
        )   

    def test_5_a(self) -> None:
        test_form(
            self, 
            name="Sahand Moslemi Yengejeh", 
            year="2000", 
            education="Graduate", 
            city="Ankara",
            selected_genders=["Select Gender"],
            ai_names=["Bard"],
            cons="AI Cons",
            use="A Use Case",
            valid=False
        )

if __name__ == '__main__':
    unittest.main()