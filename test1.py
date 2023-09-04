import yaml
from module import Site
import time

with open("config.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])
login = testdata["login"]
password = testdata["pass"]
title = testdata["title"]
description = testdata["description"]
contest = testdata["contest"]


def test_step1(x_selector1, x_selector2, x_selector3, btn_selector, err_return):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn = site.find_element("css", btn_selector)
    btn.click()
    err_lable = site.find_element("xpath", x_selector3)
    res = err_lable.text
    assert res == err_return

def test_step2(x_selector1, x_selector2, btn_selector, auth, result):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(login)
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(password)
    btn = site.find_element("css", btn_selector)
    btn.click()
    time.sleep(3)
    auth = site.find_element("xpath", auth)
    res = auth.text
    assert res == result

def test_step3(x_selector1, x_selector2, btn_selector, create_new_post, enter_title, enter_description, enter_content,
               create_button, check_create_post, check_create_actual_post):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(login)
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(password)
    btn = site.find_element("css", btn_selector)
    btn.click()
    time.sleep(3)

    input3 = site.find_element("xpath", create_new_post)
    input3.click()
    create_title = site.find_element("xpath", enter_title)
    create_title.send_keys(title)
    create_descr = site.find_element("xpath", enter_description)
    create_descr.send_keys(description)
    create_cont = site.find_element("xpath", enter_content)
    create_cont.send_keys(contest)
    btn = site.find_element("xpath", create_button)
    btn.click()
    time.sleep(3)
    check_post = site.find_element("xpath", check_create_post)
    res = check_post.text
    assert res == check_create_actual_post
