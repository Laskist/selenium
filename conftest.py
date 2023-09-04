import pytest
import yaml

with open("config.yaml") as f:
    testdata = yaml.safe_load(f)
login = testdata["login"]
title = testdata["title"]

@pytest.fixture()
def x_selector1():
    return '//*[@id="login"]/div[1]/label/input'

@pytest.fixture()
def x_selector2():
    return '//*[@id="login"]/div[2]/label/input'

@pytest.fixture()
def x_selector3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""

@pytest.fixture()
def btn_selector():
    return "button"
@pytest.fixture()
def err_return():
    return "401"

@pytest.fixture()
def auth():
    return '//*[@id="app"]/main/nav/ul/li[3]/a'

@pytest.fixture()
def result():
    return f"Hello, {login}"

@pytest.fixture()
def create_new_post():
    return '//*[@id="create-btn"]'

@pytest.fixture()
def enter_title():
    return '//*[@id="create-item"]/div/div/div[1]/div/label/input'

@pytest.fixture()
def enter_description():
    return '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'

@pytest.fixture()
def enter_content():
    return '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'

@pytest.fixture()
def create_button():
    return '//*[@id="create-item"]/div/div/div[7]/div/button/span'

@pytest.fixture()
def check_create_post():
    return '//*[@id="app"]/main/div/div[1]/h1'

@pytest.fixture()
def check_create_actual_post():
    return f'{title}'


