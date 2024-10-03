from behave import given, when, then
from selenium import webdriver
from pages.login_intu_page import LoginFBPage
from pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By

@given('the user is on the intu login page')
def step_given_user_on_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.icesi.edu.co/moodle/login/index.php")
    context.login_intu_page = LoginFBPage(context.driver)

@when('the user logs to intu in with valid credentials')
def step_when_user_logs_in_valid(context):
    context.login_intu_page.login("1109186291", "Ju4n0nUniIcesi.")

@then('the user should be redirected to the dashboard page')
def step_then_dashboard_page(context):
    dashboard_page = DashboardPage(context.driver)
    assert dashboard_page.is_top_bar_displayed()