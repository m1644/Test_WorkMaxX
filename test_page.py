from base_app import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["XPATH"].keys():
        ids[locator] = (By.XPATH, locators["XPATH"][locator])
    for locator in locators["CSS"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["CSS"][locator])


class OperationsHelper(BasePage):
    def enter_text_info_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f'We find text "{text}" in field {element_name}')
        return text

# Enter text
    def enter_email(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_CONTACT_EMAIL_FIELD"], word, description="Email field")

    def enter_name(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_CONTACT_NAME_FIELD"], word, description="Name field")

    def enter_message(self, word):
        self.enter_text_info_field(TestSearchLocators.ids["LOCATOR_CONTACT_MESSAGE_FIELD"], word, description="Message field")

# Click button
    def click_contact_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="КОНТАКТЫ")

    def click_heder_about_me_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_HEDER_ABOUT_ME_BTN"], description="in heder 'Обо мне'")

    def click_heder_servise_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_HEDER_SERVISE_BTN"], description="in heder 'Услуги'")

    def click_heder_advantages_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_HEDER_ADVANTAGES_BTN"], description="in heder 'Преимущества'")

    def click_heder_contact_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_HEDER_CONTACT_BTN"], description="in heder 'Контакты'")

    def click_heder_ux_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_HEDER_UX_BTN"], description="in heder 'UI-UX'")

    def click_heder_tilda_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_HEDER_TILDA_BTN"], description="in heder 'Tilda'")

    def click_heder_seo_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_HEDER_SEO_BTN"], description="in heder 'SEO'")

    def click_block_advantages_ux_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BLOCK_ADVANTAGES_UX_BTN"], description="in block advantage 'UI-UX'")

    def click_block_advantages_tilda_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BLOCK_ADVANTAGES_TILDA_BTN"], description="in block advantage 'TILDA'")

    def click_block_advantages_seo_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BLOCK_ADVANTAGES_SEO_BTN"], description="in block advantage 'SEO'")

    def click_back_to_top_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_BACK_TO_TOP_BTN"], description="in futer 'Back to top'")

    def click_contact_cont_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_CONT_BTN"], description="in contacts 'Отправить'")

    def click_heder_workmaxx_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CLICK_HEDER_WORKMAXX_BTN"], description="in heder 'WorkMaxX'")

# Get text
    def get_good_contact_btn_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_GOOD_CONTACT_FIELD"], description="contact btn")

    def get_good_heder_about_me_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_GOOD_HEDER_ABOUT_ME_FIELD"], description="about me")

    def get_good_heder_servise_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_GOOD_HEDER_SERVISE_FIELD"], description="servise")

    def get_good_heder_advantages_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_GOOD_HEDER_ADVANTAGES_FIELD"], description="advantages")

    def get_good_ux_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_GOOD_UX_FIELD"], description="ux-ui")

    def get_good_tilda_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_GOOD_TILDA_FIELD"], description="tilda")

    def get_good_seo_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_GOOD_SEO_FIELD"], description="seo")

    def get_good_back_to_top_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_BACK_TO_TOP_FIELD"], description="back to top")

    def get_good_contact_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_GOOD_CONTACT_CONT_FIELD"], description="contact")

    def get_good_workmaxx_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_GOOD_WORKMAXX_FIELD"], description="contact")