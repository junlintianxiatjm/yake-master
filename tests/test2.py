# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for yake package."""

import pytest

from click.testing import CliRunner

import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import yake


def test_simple_interface():
    text_content = """
    12月14日，2020年“陕西省三秦工匠、五一劳动奖章和工人先锋号表彰大会”在西安举行。公司水环境工程院/城建与交通工程院风景园林所（以下简称“风景园林所”）荣获“陕西省工人先锋号”称号。这也是近几年来公司首次获陕西省总工会（以下简称“省总”）表彰。

风景园林所自2016年成立以来，承担了国内一系列流域规划、河湖生态环境综合治理、城乡基础设施建设、湿地及矿山生态修复等工程类型的勘察设计及总承包业务。主持完成了陕西、广州、雄安、安徽、江西、甘肃、山东、江苏、河南等地区大中城市的60余项水环境治理、城乡基础环境、生态修复等类型的工程设计。近年来，团队积极服务陕西经济发展，开展了西安市小寨区域海绵城市建设项目、西安市长安区皂河黑臭水改造项目、西安市雁塔区老旧小区改造项目等工作，完成了一系列陕西省具有一定影响力的工程项目。

四年来先后获得市、区级团体奖3项，设计成果省级、公司级奖项10余项。其中，2017年度荣获共青团陕西省委“身边的陕西好青年集体”； 2018年度荣获长安区重点项目建设“突出贡献集体”；2019年度荣获陕西省总建设工会“工人先锋号”称号。

公司自2019年6月将工会关系调整至省总以来，主动学习了解省总工作机制、管理制度和活动平台，结合自身实际不断将各层面的先进集体和个人向省总各大平台推送，为职工搭建广阔的学习交流平台。公司也将以此次获奖为契机，不断向兄弟单位学习对标，选树典型推广典型，为公司转型发展助力添彩。
"""

    pyake = yake.KeywordExtractor(lan="en", n=3)

    result = pyake.extract_keywords(text_content)

    print(result)

    keywords = [kw[0] for kw in result]

    print(keywords)
    assert "google" in keywords
    assert "kaggle" in keywords
    assert "san francisco" in keywords
    assert "machine learning" in keywords


def test_simple_interface():
    text_content = """
    12月14日，2020年“陕西省三秦工匠、五一劳动奖章和工人先锋号表彰大会”在西安举行。公司水环境工程院/城建与交通工程院风景园林所（以下简称“风景园林所”）荣获“陕西省工人先锋号”称号。这也是近几年来公司首次获陕西省总工会（以下简称“省总”）表彰。

风景园林所自2016年成立以来，承担了国内一系列流域规划、河湖生态环境综合治理、城乡基础设施建设、湿地及矿山生态修复等工程类型的勘察设计及总承包业务。主持完成了陕西、广州、雄安、安徽、江西、甘肃、山东、江苏、河南等地区大中城市的60余项水环境治理、城乡基础环境、生态修复等类型的工程设计。近年来，团队积极服务陕西经济发展，开展了西安市小寨区域海绵城市建设项目、西安市长安区皂河黑臭水改造项目、西安市雁塔区老旧小区改造项目等工作，完成了一系列陕西省具有一定影响力的工程项目。

四年来先后获得市、区级团体奖3项，设计成果省级、公司级奖项10余项。其中，2017年度荣获共青团陕西省委“身边的陕西好青年集体”； 2018年度荣获长安区重点项目建设“突出贡献集体”；2019年度荣获陕西省总建设工会“工人先锋号”称号。

公司自2019年6月将工会关系调整至省总以来，主动学习了解省总工作机制、管理制度和活动平台，结合自身实际不断将各层面的先进集体和个人向省总各大平台推送，为职工搭建广阔的学习交流平台。公司也将以此次获奖为契机，不断向兄弟单位学习对标，选树典型推广典型，为公司转型发展助力添彩。

"""

    pyake = yake.KeywordExtractor(lan="ca", n=3)

    result = pyake.extract_keywords(text_content)

    print(result)

    assert len(result) > 0
