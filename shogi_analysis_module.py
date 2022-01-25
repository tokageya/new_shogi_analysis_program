#import sys
import time
import datetime
#from typing import Match, ValuesView
#import matplotlib.pyplot as plt # データプロット
#import matplotlib.ticker as ticker
import glob # ファイル名検索
#import csv
#from statistics import variance # 分散表示
import pprint

"""
MASTER_DIR
    解析した棋譜ファイルのディレクトリ情報が入ったもの
"""

MASTER_DIR = {
    "水匠4改" : {
        "No79" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\79期(2020,21年)(途中)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\79期(2020,21年)(途中)\B級1組",
        },
        "No78" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\78期(2019,20年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\78期(2019,20年)\B級1組",
        },
        "No77" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\77期(2018,19年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\77期(2018,19年)\B級1組",
        },
        "No76" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\76期(2017,18年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\76期(2017,18年)\B級1組",
        },
        "No75" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\75期(2016,17年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\75期(2016,17年)\B級1組",
        },
        "No74" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\74期(2015,16年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\74期(2015,16年)\B級1組",
        },
        "No73" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\73期(2014,15年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\73期(2014,15年)\B級1組",
        },
        "No72" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\72期(2013,14年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\72期(2013,14年)\B級1組",
        },
        "No71" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\71期(2012,13年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\71期(2012,13年)\B級1組",
        },
        "No70" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\70期(2011,12年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\70期(2011,12年)\B級1組",
        },
        "No69" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\69期(2010,11年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\69期(2010,11年)\B級1組",
        },
        "No68" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\68期(2009,10年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\68期(2009,10年)\B級1組",
        },
        "No67" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\67期(2008,09年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\67期(2008,09年)\B級1組",
        },
        "No66" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\66期(2007,08年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\66期(2007,08年)\B級1組",
        },
        "No65" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\65期(2006,07年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\65期(2006,07年)\B級1組",
        },
        "No64" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\64期(2005,06年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\64期(2005,06年)\B級1組",
        },
        "No63" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\63期(2004,05年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\63期(2004,05年)\B級1組",
        },
        "No62" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\62期(2003,04年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\62期(2003,04年)\B級1組",
        },
        "No61" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\61期(2002,03年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\61期(2002,03年)\B級1組",
        },
        "No60" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\60期(2001,02年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\60期(2001,02年)\B級1組",
        },
        "No59" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\59期(2000,01年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\59期(2000,01年)\B級1組",
        },
        "No58" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\58期(1999,2000年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\58期(1999,2000年)\B級1組",
        },
        "No57" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\57期(1998,99年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\57期(1998,99年)\B級1組",
        },
        "No56" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\56期(1997,98年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\56期(1997,98年)\B級1組",
        },
        "No55" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\55期(1996,97年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\55期(1996,97年)\B級1組",
        },
        "No54" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\54期(1995,96年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\54期(1995,96年)\B級1組",
        },
        "No53" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\53期(1994,95年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\53期(1994,95年)\B級1組",
        },
        "No52" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\52期(1993,94年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\52期(1993,94年)\B級1組",
        },
        "No51" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\51期(1992,93年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\51期(1992,93年)\B級1組",
        },
        "No50" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\50期(1991,92年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\50期(1991,92年)\B級1組",
        },
        "No49" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\49期(1990,91年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\49期(1990,91年)\B級1組",
        },
        "No48" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\48期(1989,90年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\48期(1989,90年)\B級1組",
        },
        "No47" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\47期(1988,89年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\47期(1988,89年)\B級1組",
        },
        "No46" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\46期(1987,88年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\46期(1987,88年)\B級1組",
        },
        "No45" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\45期(1986,87年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\45期(1986,87年)\B級1組",
        },
        "No44" : {
            "A級" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\44期(1985,86年)\A級",
            "B級1組" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦A級,B級1組_水匠4改解析(7千万ノード)\44期(1985,86年)\B級1組",
        },
    },
    "水匠2" : {
        "No79" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\79期(2020,21年)\順位戦\B級1組",
        "No78" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\78期(2019,20年)\順位戦\B級1組",
        "No77" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\77期(2018,19年)\順位戦\B級1組",
        "No76" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\76期(2017,18年)\順位戦\B級1組",
        "No75" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\75期(2016,17年)\順位戦\B級1組",
        "No74" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\74期(2015,16年)\順位戦\B級1組",
        "No73" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\73期(2014,15年)\順位戦\B級1組",
        "No72" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\72期(2013,14年)\順位戦\B級1組",
        "No71" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\71期(2012,13年)\順位戦\B級1組",
        "No70" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\70期(2011,12年)\順位戦\B級1組",
        "No69" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\69期(2010,11年)\順位戦\B級1組",
        "No68" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\68期(2009,10年)\順位戦\B級1組",
        "No67" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\67期(2008,09年)\順位戦\B級1組",
        "No66" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\66期(2007,08年)\順位戦\B級1組",
        "No65" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\65期(2006,07年)\順位戦\B級1組",
        "No64" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\64期(2005,06年)\順位戦\B級1組",
        "No63" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\63期(2004,05年)\順位戦\B級1組",
        "No62" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦78~62期順位戦B級1組(水匠2解析結果(最終手まで))\62期(2003,04年)\順位戦\B級1組",
        "No61" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\61期(2002,03年)\順位戦\B級1組",
        "No60" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\60期(2001,02年)\順位戦\B級1組",
        "No59" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\59期(2000,01年)\順位戦\B級1組",
        "No58" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\58期(1999,00年)\順位戦\B級1組",
        "No57" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\57期(1998,99年)\順位戦\B級1組",
        "No56" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\56期(1997,98年)\順位戦\B級1組",
        "No55" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\55期(1996,97年)\順位戦\B級1組",
        "No54" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\54期(1995,96年)\順位戦\B級1組",
        "No53" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\53期(1994,95年)\順位戦\B級1組",
        "No52" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\52期(1993,94年)\順位戦\B級1組",
        "No51" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\51期(1992,93年)\順位戦\B級1組",
        "No50" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\50期(1991,92年)\順位戦\B級1組",
        "No49" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\49期(1990,91年)\順位戦\B級1組",
        "No48" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\48期(1989,90年)\順位戦\B級1組",
        "No47" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\47期(1988,89年)\順位戦\B級1組",
        "No46" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\46期(1987,88年)\順位戦\B級1組",
        "No45" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\45期(1986,87年)\順位戦\B級1組",
        "No44" : r"C:\Users\msait\Documents\research\shogi\kifu\名人戦61~44期順位戦B級1組(水匠2解析結果(最終手まで))\44期(1985,86年)\順位戦\B級1組",
    },
    "elmo" : {
        "No79" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\79期(2020,21年)\順位戦\B級1組",
        "No78" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\78期(2019,20年)\順位戦\B級1組",
        "No77" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\77期(2018,19年)\順位戦\B級1組",
        "No76" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\76期(2017,18年)\順位戦\B級1組",
        "No75" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\75期(2016,17年)\順位戦\B級1組",
        "No74" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\74期(2015,16年)\順位戦\B級1組",
        "No73" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\73期(2014,15年)\順位戦\B級1組",
        "No72" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\72期(2013,14年)\順位戦\B級1組",
        "No71" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\71期(2012,13年)\順位戦\B級1組",
        "No70" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\70期(2011,12年)\順位戦\B級1組",
        "No69" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\69期(2010,11年)\順位戦\B級1組",
        "No68" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\68期(2009,10年)\順位戦\B級1組",
        "No67" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\67期(2008,09年)\順位戦\B級1組",
        "No66" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\66期(2007,08年)\順位戦\B級1組",
        "No65" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\65期(2006,07年)\順位戦\B級1組",
        "No64" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\64期(2005,06年)\順位戦\B級1組",
        "No63" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\63期(2004,05年)\順位戦\B級1組",
        "No62" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(62期～79期)(研究室PCにて70000000ノード)\62期(2003,04年)\順位戦\B級1組",
        "No61" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\61期(2002,03年)\B級1組",
        "No60" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\60期(2001,02年)\B級1組",
        "No59" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\59期(2000,01年)\B級1組",
        "No58" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\58期(1999,2000年)\B級1組",
        "No57" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\57期(1998,99年)\B級1組",
        "No56" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\56期(1997,98年)\B級1組",
        "No55" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\55期(1996,97年)\B級1組",
        "No54" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\54期(1995,96年)\B級1組",
        "No53" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\53期(1994,95年)\B級1組",
        "No52" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\52期(1993,94年)\B級1組",
        "No51" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\51期(1992,93年)\B級1組",
        "No50" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\50期(1991,92年)\B級1組",
        "No49" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\49期(1990,91年)\B級1組",
        "No48" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\48期(1989,90年)\B級1組",
        "No47" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\47期(1988,89年)\B級1組",
        "No46" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\46期(1987,88年)\B級1組",
        "No45" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\45期(1986,87年)\B級1組",
        "No44" : r"C:\Users\msait\Documents\research\shogi\kifu\順位戦B級1組(elmo解析結果(最終手まで))(44期～61期まで)(研究室PCにて70000000ノード)\44期(1985,86年)\B級1組",
    },
    
    "渡辺" : r"C:\Users\msait\Documents\research\shogi\kifu\棋譜解析結果ファイル(渡辺明先生他)(水匠4)\渡辺明先生の棋譜解析結果",
    "藤井" : r"C:\Users\msait\Documents\research\shogi\kifu\棋譜解析結果ファイル(渡辺明先生他)(水匠4)\藤井聡太先生の棋譜解析結果",
    "豊島" : r"C:\Users\msait\Documents\research\shogi\kifu\棋譜解析結果ファイル(渡辺明先生他)(水匠4)\豊島将之先生の棋譜解析結果",
    "永瀬" : r"C:\Users\msait\Documents\research\shogi\kifu\棋譜解析結果ファイル(渡辺明先生他)(水匠4)\永瀬先生の棋譜解析結果"
}

"""
YEAR_HASH
    年度 => datetimeの対応票
"""

YEAR_HASH = {
    "2000" : [datetime.datetime(2000,4,1), datetime.datetime(2001,3,31)],
    "2001" : [datetime.datetime(2001,4,1), datetime.datetime(2002,3,31)],
    "2002" : [datetime.datetime(2002,4,1), datetime.datetime(2003,3,31)],
    "2003" : [datetime.datetime(2003,4,1), datetime.datetime(2004,3,31)],
    "2004" : [datetime.datetime(2004,4,1), datetime.datetime(2005,3,31)],
    "2005" : [datetime.datetime(2005,4,1), datetime.datetime(2006,3,31)],
    "2006" : [datetime.datetime(2006,4,1), datetime.datetime(2007,3,31)],
    "2007" : [datetime.datetime(2007,4,1), datetime.datetime(2008,3,31)],
    "2008" : [datetime.datetime(2008,4,1), datetime.datetime(2009,3,31)],
    "2009" : [datetime.datetime(2009,4,1), datetime.datetime(2010,3,31)],
    "2010" : [datetime.datetime(2010,4,1), datetime.datetime(2011,3,31)],
    "2011" : [datetime.datetime(2011,4,1), datetime.datetime(2012,3,31)],
    "2012" : [datetime.datetime(2012,4,1), datetime.datetime(2013,3,31)],
    "2013" : [datetime.datetime(2013,4,1), datetime.datetime(2014,3,31)],
    "2014" : [datetime.datetime(2014,4,1), datetime.datetime(2015,3,31)],
    "2015" : [datetime.datetime(2015,4,1), datetime.datetime(2016,3,31)],
    "2016" : [datetime.datetime(2016,4,1), datetime.datetime(2017,3,31)],
    "2017" : [datetime.datetime(2017,4,1), datetime.datetime(2018,3,31)],
    "2018" : [datetime.datetime(2018,4,1), datetime.datetime(2019,3,31)],
    "2019" : [datetime.datetime(2019,4,1), datetime.datetime(2020,3,31)],
    "2020" : [datetime.datetime(2020,4,1), datetime.datetime(2021,3,31)],
}

"""
create_new_file 関数
    引数で渡された手数までの棋譜を作成する
"""
def create_new_file(file_name, turn, new_file_name):
    new_lines = []

    with open(file_name, mode="r", encoding="cp932") as file:
        analysis_bool = False
        now_turn = 0
        for line in file.readlines():
            if line.startswith("#"):
                continue
            words = line.split()
            if not words:
                continue
            if words[0].isdigit():
                now_turn = int(words[0])
            elif words[0] != "**解析":
                continue
            if words[0] == "**解析":
                analysis_bool = True
            # ターン数が超過したら、処理を終了
            if turn < now_turn:
                break
            # ターン数が超過していないなら、lineをそのままnew_file_nameに出力する
            elif analysis_bool:
                new_lines.append(line)
    with open(new_file_name, mode="w", encoding="cp932", newline="") as file:
        file.writelines(new_lines)
    return

#=====================================#
#
# AIとの着手一致率に関する関数定義
#
#=====================================#

"""
calculate_move_concordance_rate 関数
    引数で渡された手数の間のAIとの着手一致率を求め、[先手の一致率, 後手の一致率]の2要素からなるリストで返す
    例：kifファイル"tmp.kif"の31手～60手までの先手・後手の一致率を求める：calculate_move_concordance_rate("tmp.kif",31,60)
"""
def calculate_move_concordance_rate(file_name, start_move_num, last_move_num):
    with open(file_name, mode="r", encoding="cp932") as file:
        now_move_num = 0 # 現在注目している手数
        first_match_num = 0 # 現在までの先手のAIとの着手一致回数
        second_match_num = 0 # 現在までの後手のAIとの着手一致回数
        analysis_bool = False
        best_move_str = ""
        first_actual_count = 0 # 先手の実際の着手の回数
        second_actual_count = 0 # 後手の実際の着手の回数
        
        for line in file.readlines():
            if line.startswith("#"):
                continue
            words = line.split()
            if not words:
                continue

            if words[0].isdigit():
                now_move_num = int(words[0])

            if (start_move_num-1) <= now_move_num and now_move_num <= last_move_num: # 「現在の盤面の最善手」⇒「実際の着手」という記載の仕方のため、(start_move_num-1)にしている
                if words[0] == "**解析" and analysis_bool is False:
                    best_move_str = words[words.index("読み筋")+1]
                    if best_move_str[-1] == "同":
                        best_move_str = best_move_str + " " + words[words.index("読み筋")+2]
                    if best_move_str[-1] == ")":
                        best_move_str = best_move_str[:best_move_str.find("(")]
                    best_move_str = best_move_str[1:]
                    analysis_bool = True
                    
                elif words[0].isdigit() and analysis_bool is True:
                    if now_move_num % 2 == 1:
                        first_actual_count += 1
                    else:
                        second_actual_count += 1
                    
                    human_move_str = words[1]
                    if human_move_str[-1] == "同":
                        human_move_str = human_move_str + " " + words[2]
                    if human_move_str[-1] == ")":
                        human_move_str = human_move_str[:human_move_str.find("(")]
                    if human_move_str == "投了":
                        break
                    if best_move_str == human_move_str:
                        if now_move_num % 2 == 1:
                            first_match_num += 1
                        else:
                            second_match_num += 1
                    analysis_bool = False
            elif last_move_num < now_move_num:
                break
    first_match_rate = None
    second_match_rate = None
    if first_actual_count == 0:
        first_match_rate = None
    else:
        first_match_rate = (float(first_match_num)) / first_actual_count
    if second_actual_count == 0:
        second_match_rate = None
    else:
        second_match_rate = (float(second_match_num)) / second_actual_count 
    return [first_match_rate, second_match_rate]

"""
search_kif_file_list 関数
    指定したディレクトリ下(サブディレクトリも検索する)に存在する解析済みの棋譜ファイル( ファイル名の末端が".kif" )を検索してリストで返す
    (存在しなかった場合は [] を返す)
"""
def search_kif_file_list(dir_name):
    return glob.glob(dir_name+r"\**\*.kif", recursive=True)

"""
search_suisho2_analysis_file_list 関数
    指定したディレクトリ下(サブディレクトリも検索する)に存在する解析済みの棋譜ファイル( ファイル名の末端が"_suisho2analysis.kif" )を検索してリストで返す
    (存在しなかった場合は [] を返す)
"""
def search_suisho2_analysis_file_list(dir_name):
    return glob.glob(dir_name+r"\**\*_suisho2analysis.kif", recursive=True)

"""
search_suisho4kaianalysis_file_list 関数
    指定したディレクトリ下(サブディレクトリも検索する)に存在する解析済みの棋譜ファイル( ファイル名の末端が"_suisho4analysis.kif" )を検索してリストで返す
    (存在しなかった場合は [] を返す)
"""
def search_suisho4kaianalysis_file_list(dir_name):
    return glob.glob(dir_name+r"\**\*_suisho4kaianalysis.kif", recursive=True)

"""
search_kishi_name 関数
    ファイル内から先手と後手の棋士名を取り出し、[先手性, 先手名, 後手性, 後手名]のリストで返す
"""
def search_kishi_name(file_name):
    first_family_name = "" # 先手の性
    first_last_name = "" # 先手の名
    second_family_name = "" # 後手の性
    second_last_name = "" # 後手の名
    with open(file_name, mode="r", encoding="cp932") as file_name:
        for line in file_name.readlines():
            if line.find("先手姓：") != -1:
                first_family_name = line[4:].strip()
            elif line.find("先手名：") != -1:
                first_last_name = line[4:].strip()
            elif line.find("後手姓：") != -1:
                second_family_name = line[4:].strip()
            elif line.find("後手名：") != -1:
                second_last_name = line[4:].strip()
    return [first_family_name, first_last_name, second_family_name, second_last_name]

"""
search_date_and_time 関数
    対象の棋譜ファイルの対局が行われた日時をdatetime型で返す
"""
def search_date_and_time(file_name):
    game_datetime = datetime.datetime.now()
    with open(file_name, mode="r", encoding="cp932") as file_name:
        for line in file_name.readlines():
            if line.find("開始日時：") != -1:
                game_datetime = datetime.datetime.strptime(line[5:].strip(), "%Y/%m/%d %H:%M")
    return game_datetime

"""
calculation_move_concordance_rate_average_for_elmo 関数
    引数で渡されたディレクトリ内に存在する解析済みの棋譜ファイル( ファイル名の末端が"_analysis.kif" )について、引数で指定された手数の間のAIとの着手一致率の平均を求めて返す
"""
def calculation_move_concordance_rate_average_for_elmo(number, dir_name, start_move_num , last_move_num):
    file_list = search_kif_file_list(dir_name)
    move_concordance_rates_sum = 0
    move_concordance_rate_list = [] # ここに一致率リストを追加
    count = 0
    file_count = 0
    if len(file_list) == 0: # ディレクトリの中身に解析済みの棋譜ファイルが存在しないとき
        return None
    for file in file_list:
        move_concordance_rates = calculate_move_concordance_rate(file, start_move_num, last_move_num)
        if (move_concordance_rates[0] is not None) and (move_concordance_rates[1] is not None):
            move_concordance_rate_list.append(move_concordance_rates[0])
            move_concordance_rate_list.append(move_concordance_rates[1])
            move_concordance_rates_sum += (move_concordance_rates[0] + move_concordance_rates[1])
            count += 2
        file_count += 1
    move_concordance_rate_average = move_concordance_rates_sum / count
    #print(str(number)+"期順位戦B級1組___"+str(start_move_num)+"～"+str(last_move_num)+"手")
    print("kishi_player_count : "+str(count))
    return [file_count, move_concordance_rate_average]

"""
calculation_move_concordance_rate_average_for_suisho2 関数
    引数で渡されたディレクトリ内に存在する解析済みの棋譜ファイル( ファイル名の末端が"_suisho2analysis.kif" )について、引数で指定された手数の間のAIとの着手一致率の平均を求めて返す
"""
def calculation_move_concordance_rate_average_for_suisho2(number, dir_name, start_move_num , last_move_num):
    file_list = search_suisho2_analysis_file_list(dir_name)
    move_concordance_rates_sum = 0
    move_concordance_rate_list = [] # ここに一致率リストを追加
    count = 0
    file_count = 0
    if len(file_list) == 0: # ディレクトリの中身に解析済みの棋譜ファイルが存在しないとき
        return None
    for file in file_list:
        move_concordance_rates = calculate_move_concordance_rate(file, start_move_num, last_move_num)
        if (move_concordance_rates[0] is not None) and (move_concordance_rates[1] is not None):
            move_concordance_rate_list.append(move_concordance_rates[0])
            move_concordance_rate_list.append(move_concordance_rates[1])
            move_concordance_rates_sum += (move_concordance_rates[0] + move_concordance_rates[1])
            count += 2
        file_count += 1
    move_concordance_rate_average = move_concordance_rates_sum / count
    #print(str(number)+"期順位戦B級1組___"+str(start_move_num)+"～"+str(last_move_num)+"手")
    print("kishi_player_count : "+str(count))
    return [file_count, move_concordance_rate_average]

"""
calculation_move_concordance_rate_average 関数
    引数で渡されたディレクトリ内に存在する解析済みの棋譜ファイル( ファイル名の末端が"_suisho4kaianalysis.kif" )について、引数で指定された手数の間のAIとの着手一致率の平均を求めて返す
"""
def calculation_move_concordance_rate_average(number, dir_name, start_move_num , last_move_num):
    file_list = search_suisho4kaianalysis_file_list(dir_name)
    move_concordance_rates_sum = 0
    move_concordance_rate_list = [] # ここに一致率リストを追加
    count = 0
    file_count = 0
    if len(file_list) == 0: # ディレクトリの中身に解析済みの棋譜ファイルが存在しないとき
        return None
    for file in file_list:
        move_concordance_rates = calculate_move_concordance_rate(file, start_move_num, last_move_num)
        if (move_concordance_rates[0] is not None) and (move_concordance_rates[1] is not None):
            move_concordance_rate_list.append(move_concordance_rates[0])
            move_concordance_rate_list.append(move_concordance_rates[1])
            move_concordance_rates_sum += (move_concordance_rates[0] + move_concordance_rates[1])
            count += 2
        file_count += 1
    move_concordance_rate_average = move_concordance_rates_sum / count
    #print(str(number)+"期順位戦B級1組___"+str(start_move_num)+"～"+str(last_move_num)+"手")
    print("kishi_player_count : "+str(count))
    return [file_count, move_concordance_rate_average]

"""
calculation_move_concordance_rate_average_by_kishi_name 関数
    引数で渡されたディレクトリ内に存在する解析済みの棋譜ファイル( ファイル名の末端が"_suisho4analysis.kif" )について、引数で指定された期間の棋譜と手数の間のAIとの着手一致率の平均を1人の将棋棋士に対して求めて返す
"""
def calculation_move_concordance_rate_average_by_kishi_name(dir_name, start_move_num , last_move_num, kishi_family_name, kishi_last_name, begin_datetime, end_datetime):
    file_list = search_suisho4kaianalysis_file_list(dir_name)
    move_concordance_rates_sum = 0
    move_concordance_rate_list = [] # ここに一致率リストを追加
    count = 0
    if len(file_list) == 0: # ディレクトリの中身に解析済みの棋譜ファイルが存在しないとき
        return None
    for file in file_list:
        # --- 1. 対象の棋士が先手か後手かを調べる --- #
        first_family_name = "" # 先手の性
        second_family_name = "" # 後手の性
        tmp = search_kishi_name(file)
        first_family_name = tmp[0]
        first_last_name = tmp[1]
        second_family_name = tmp[2]
        second_last_name = tmp[3]
        
        # --- 2. 棋譜が対象の期間か調べる --- #
        kif_datetime = search_date_and_time(file)
        if (kif_datetime < begin_datetime) or (end_datetime < kif_datetime):
            continue

        # --- 3. 一致率を算出する --- #
        move_concordance_rates = calculate_move_concordance_rate(file, start_move_num, last_move_num)
        if (move_concordance_rates[0] is not None) and (move_concordance_rates[1] is not None):
            
            move_concordance_rate_list.append(move_concordance_rates[0])
            move_concordance_rate_list.append(move_concordance_rates[1])

            if (first_family_name == kishi_family_name) and (first_last_name == kishi_last_name):
                move_concordance_rates_sum += move_concordance_rates[0]
                count+=1
            elif (second_family_name == kishi_family_name) and (second_last_name == kishi_last_name):
                move_concordance_rates_sum += move_concordance_rates[1]
                count += 1

    print("count = "+str(count))
    if count == 0:
        return [0,None]
    move_concordance_rate_average = move_concordance_rates_sum / count
    
    return [count, move_concordance_rate_average]




#==============================#
#
# 盤面評価値に関する関数定義
#
#==============================#



"""
read_board_evaluation_values 関数
    引数で渡されたkifファイルの評価値を読み込み、リストで返す
"""
def read_board_evaluation_values(file_name):
    values = []
    with open(file_name, mode="r", encoding="cp932") as file:
        read_bool = True
        for line in file.readlines():
            if line.startswith("#"): # 行の最初の文字が"#"ならスキップ
                continue
            words = line.split()
            if not words: # wordsが空ならスキップ
                continue
            if words[0].isdigit():
                read_bool = True
            elif (read_bool is True) and words[0] == "**解析": # 解析の出力行
                value_str = words[words.index("評価値")+1]
                if value_str != "+詰" and value_str != "-詰":
                    while not value_str[-1].isdigit(): # 矢印の削除
                        value_str = value_str[:-1]
                    last_value = int(value_str)
                    values.append(last_value)
                else:
                    values.append(None)
                read_bool = False
    return values

def calculation_board_evaluation_each_average(dir_name, start_move_num , last_move_num):
    file_list = search_suisho2_analysis_file_list(dir_name)
    values_sum = 0
    count_sum = 0
    for file in file_list:
        board_values = read_board_evaluation_values(file)
        diff_ai_list = []
        for i in range(len(board_values)):
            if (i % 2 == 0) and (board_values[i] is not None) and ((i+1) < len(board_values)) and (board_values[i+1] is not None):
                diff_ai_list.append(board_values[i+1] - board_values[i])
            elif (i % 2 == 1) and (board_values[i] is not None) and ((i+1) < len(board_values)) and (board_values[i+1] is not None):
                diff_ai_list.append((-1)*(board_values[i+1] - board_values[i]))
        values_sum += sum(diff_ai_list)
        count_sum += len(diff_ai_list)
    if count_sum == 0:
        return [0,None]
    return  [count_sum, (values_sum / count_sum)]

"""
calculation_board_evaluation_each_average_by_kishi_name 関数
    ディレクトリ内に存在する解析済みの各棋譜ファイル( ファイル名の末端が"_suisho4analysis.kif" )の各番での上下の値の平均を出してリストを返す
"""
def calculation_board_evaluation_each_average_by_kishi_name(dir_name, start_move_num , last_move_num, kishi_family_name, kishi_last_name, begin_datetime, end_datetime):
    file_list = search_suisho4_analysis_file_list(dir_name)
    values_sum = 0
    count_sum = 0
    for file in file_list:
        # --- 1. 対象の棋士が先手か後手かを調べる --- #
        first_family_name = "" # 先手の性
        second_family_name = "" # 後手の性
        tmp = search_kishi_name(file)
        first_family_name = tmp[0]
        first_last_name = tmp[1]
        second_family_name = tmp[2]
        second_last_name = tmp[3]

        # --- 2. 棋譜が対象の期間か調べる --- #
        kif_datetime = search_date_and_time(file)
        if (kif_datetime < begin_datetime) or (end_datetime < kif_datetime):
            continue

        # --- 3. 盤面評価値を算出する --- #
        board_values = read_board_evaluation_values(file)
        diff_ai_list = []
        if (first_family_name == kishi_family_name) and (first_last_name == kishi_last_name):
            for i in range(len(board_values)):
                if (i % 2 == 0) and (board_values[i] is not None) and ((i+1) < len(board_values)) and (board_values[i+1] is not None):
                    diff_ai_list.append(board_values[i+1] - board_values[i])
        elif (second_family_name == kishi_family_name) and (second_last_name == kishi_last_name):
            for i in range(len(board_values)):
                if (i % 2 == 1) and (board_values[i] is not None) and ((i+1) < len(board_values)) and (board_values[i+1] is not None):
                    diff_ai_list.append((-1)*(board_values[i+1] - board_values[i]))
        values_sum += sum(diff_ai_list)
        count_sum += len(diff_ai_list)
    if count_sum == 0:
        return [0,None]
    return  [count_sum, (values_sum / count_sum)]