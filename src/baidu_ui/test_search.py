import pytest
import xlrd
from selenium import webdriver
from  time import sleep, ctime
import os
from .const import *

class Test_baidu_search():
    def test_search_from_excel(self,excel_dir=EXCEL_DIR):

        driver = webdriver.Chrome();
        driver.get("http://www.baidu.com")

        #打开excel
        excel_file = xlrd.open_workbook(EXCEL_DIR)
        #获取第一个sheet
        sheet = excel_file.sheet_by_index(0)
        #获取第一列数据返回列表
        cols = sheet.col_values(0)
        #print(cols)
        #遍历列表，拿取数据作为测试输入
        for query in cols:
            driver.find_element_by_id("kw").clear()
            driver.find_element_by_id("kw").send_keys(str(query))
            driver.find_element_by_id("su").click()
            sleep(10)

        driver.quit()

    def test_ssss(self):
        print("1111111")
        assert 1==1

    def test_failed(self):
        print("2222222")
        assert 1==0