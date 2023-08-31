from test_page import OperationsHelper
import logging
import time


def test_step_01_main_contact_btn(browser):
    """ Тест функции кнопки "КОНТАКТЫ" на главной странице """
    logging.info("Test_01 Starting...")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    time.sleep(2)
    testpage.click_contact_btn()
    time.sleep(2)
    assert testpage.get_good_contact_btn_text() == "Контакты"

def test_step_02_btn_about_me(browser):
    """ Тест функции кнопки "Обо мне" в хедере на главной странице """
    logging.info("Test_02 Starting...")
    testpage = OperationsHelper(browser)
    testpage.click_heder_about_me_btn()
    time.sleep(2)
    assert testpage.get_good_heder_about_me_text() == "Обо мне"

def test_step_03_btn_servise(browser):
    """ Тест функции кнопки "Услуги" в хедере на главной странице """
    logging.info("Test_03 Starting...")
    testpage = OperationsHelper(browser)
    testpage.click_heder_servise_btn()
    time.sleep(2)
    assert testpage.get_good_heder_servise_text() == "UI - UX дизайн"

def test_step_04_btn_benefits(browser):
    """ Тест функции кнопки "Преимущества" в хедере на главной странице """
    logging.info("Test_04 Starting...")
    testpage = OperationsHelper(browser)
    testpage.click_heder_advantages_btn()
    time.sleep(2)
    assert testpage.get_good_heder_advantages_text() == "Основные преимущества"

def test_step_05_btn_contact(browser):
    """ Тест функции кнопки "Контакты" в хедере на главной странице """
    logging.info("Test_05 Starting...")
    testpage = OperationsHelper(browser)
    testpage.click_heder_contact_btn()
    time.sleep(2)
    assert testpage.get_good_contact_btn_text() == "Контакты"

def test_step_06_heder_ui_ux_btn(browser):
    """ Тест функции кнопки 'UI - UX' в хедере на главной странице и перехода в раздел 'UI - UX ДИЗАЙН' """
    logging.info("Test_06 Starting...")
    testpage = OperationsHelper(browser)
    testpage.click_heder_ux_btn()
    time.sleep(2)
    assert testpage.get_good_ux_text() == "UI - UX ДИЗАЙН"

def test_step_07_heder_tilda_btn(browser):
    """ Тест функции кнопки 'Tilda' в хедере на главной странице и перехода в раздел 'Tilda' """
    logging.info("Test_07 Starting...")
    testpage = OperationsHelper(browser)
    testpage.click_heder_tilda_btn()
    time.sleep(2)
    assert testpage.get_good_tilda_text() == "TILDA"

def test_step_08_heder_seo_btn(browser):
    """ Тест функции кнопки 'SEO' в хедере на главной странице и перехода в раздел 'SEO' """
    logging.info("Test_08 Starting...")
    testpage = OperationsHelper(browser)
    testpage.click_heder_seo_btn()
    time.sleep(2)
    assert testpage.get_good_seo_text() == "SEO ОПТИМИЗАЦИЯ"

def test_step_09_block_servise_ux_ui_btn(browser):
    """ Тест функции кнопки 'UI - UX' в блоке 'Услуги' на главной странице и перехода в раздел 'UI - UX' """
    logging.info("Test_09 Starting...")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    time.sleep(2)
    testpage.click_block_advantages_ux_btn()
    time.sleep(2)
    assert testpage.get_good_ux_text() == "UI - UX ДИЗАЙН"

def test_step_10_block_servise_tilda_btn(browser):
    """ Тест функции кнопки 'TILDA' в блоке 'Услуги' на главной странице и перехода в раздел 'TILDA' """
    logging.info("Test_10 Starting...")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    time.sleep(2)
    testpage.click_block_advantages_tilda_btn()
    time.sleep(2)
    assert testpage.get_good_tilda_text() == "TILDA"

def test_step_11_block_servise_seo_btn(browser):
    """ Тест функции кнопки 'SEO' в блоке 'Услуги' на главной странице и перехода в раздел 'SEO ОПТИМИЗАЦИЯ' """
    logging.info("Test_11 Starting...")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    time.sleep(2)
    testpage.click_block_advantages_seo_btn()
    time.sleep(2)
    assert testpage.get_good_seo_text() == "SEO ОПТИМИЗАЦИЯ"

def test_step_12_futer_backtop_btn(browser):
    """ Тест функции кнопки 'Back to top' в футере на главной странице и перехода к хедеру """
    logging.info("Test_12 Starting...")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.click_back_to_top_btn()
    assert testpage.get_good_back_to_top_text() == "WorkMaxX"

def test_step_13_contact_send_message(browser):
    """ Тест заполнения формы в разделе "Контакты" """
    logging.info("Test_13 Starting...")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_email("4444@bk.ru")
    testpage.enter_name("John")
    testpage.enter_message("Hello world")
    time.sleep(2)
    testpage.click_contact_cont_btn()
    time.sleep(10)
    assert testpage.get_good_contact_text() == "Спасибо! Данные успешно отправлены."

def test_step_14_heder_workmaxx_btn(browser):
    """ Тест функции кнопки "WorkMaxX" на главной странице в хедере """
    logging.info("Test_14 Starting...")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    time.sleep(2)
    testpage.click_heder_ux_btn()
    time.sleep(2)
    testpage.click_heder_workmaxx_btn()
    time.sleep(2)
    assert testpage.get_good_workmaxx_text() == "WorkMaxX"


#python -m pytest --html-report=report.html
