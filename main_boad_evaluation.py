from typing import Match
from shogi_analysis_module import *
import csv

MASTER_DIR = {
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
    "渡辺" : r"C:\Users\msait\Documents\research\shogi\kifu\棋譜解析結果ファイル(渡辺明先生他)(水匠4)\渡辺明先生の棋譜解析結果",
    "藤井" : r"C:\Users\msait\Documents\research\shogi\kifu\棋譜解析結果ファイル(渡辺明先生他)(水匠4)\藤井聡太先生の棋譜解析結果",
    "豊島" : r"C:\Users\msait\Documents\research\shogi\kifu\棋譜解析結果ファイル(渡辺明先生他)(水匠4)\豊島将之先生の棋譜解析結果",
    "永瀬" : r"C:\Users\msait\Documents\research\shogi\kifu\棋譜解析結果ファイル(渡辺明先生他)(水匠4)\永瀬先生の棋譜解析結果"
}

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

if __name__=="__main__":
    #print(read_board_evaluation_values(MASTER_DIR["No78"] + r"\20190613阿久津 主税－千田 翔太_suisho2analysis.kif"))
    #print(calculate_move_concordance_rate(MASTER_DIR["No78"] + r"\20190613阿久津 主税－千田 翔太_suisho2analysis.kif", ANALYSIS_START_TURN, ANALYSIS_LAST_TURN))
    #print(calculation_move_concordance_rate_average(MASTER_DIR["渡辺"],ANALYSIS_START_TURN, ANALYSIS_LAST_TURN))
    
    #print(len(search_suisho4_analysis_file_list(MASTER_DIR["渡辺"])))
    #print(len(search_suisho4_analysis_file_list(MASTER_DIR["藤井"])))
    #print(len(search_suisho4_analysis_file_list(MASTER_DIR["豊島"])))
    #print(len(search_suisho4_analysis_file_list(MASTER_DIR["永瀬"])))
    #print(len(search_suisho4_analysis_file_list(r"C:\Users\msait\Documents\research\shogi\kifu\棋譜解析結果ファイル(渡辺明先生他)(水匠4)")))
    ANALYSIS_START_TURN = 1 # 最初のターン
    ANALYSIS_LAST_TURN = 600
    #print(search_kishi_name(MASTER_DIR["渡辺"] + r"\20000417佐藤 紳哉－渡辺 明_suisho4analysis.kif"))
    #print(search_date_and_time(MASTER_DIR["渡辺"] + r"\20000417佐藤 紳哉－渡辺 明_suisho4analysis.kif"))
    
    watanabe_value_list = []
    watanabe_count_list = []
    fujii_value_list = []
    fujii_count_list = []
    toyoshima_value_list = []
    toyoshima_count_list = []
    nagase_value_list = []
    nagase_count_list = []

    #print(read_board_evaluation_values(MASTER_DIR["渡辺"] + r"\20000417佐藤 紳哉－渡辺 明_suisho4analysis.kif"))
    print(calculation_board_evaluation_each_average_by_kishi_name(MASTER_DIR["渡辺"], ANALYSIS_START_TURN, ANALYSIS_LAST_TURN, "渡辺", "明", YEAR_HASH["2019"][0], YEAR_HASH["2019"][1]))
    
    # csv ファイル出力
    """
    with open("./result_kifu_analysis_concordance_rate_average.csv", "w", newline="") as f:
        writer = csv.writer(f)

        list_tmp = ["年度"]
        for i in list(range(2000,2021)):
            list_tmp.append(i)
        writer.writerow(list_tmp)

        watanabe_value_list.insert(0, "渡辺　明先生(評価値の年平均)")
        writer.writerow(watanabe_value_list)
        watanabe_count_list.insert(0, "渡辺　明先生(棋譜の個数)")
        writer.writerow(watanabe_count_list)

        fujii_value_list.insert(0, "藤井　聡太先生(評価値の年平均)")
        writer.writerow(fujii_value_list)
        fujii_count_list.insert(0, "藤井　聡太先生(棋譜の個数)")
        writer.writerow(fujii_count_list)

        toyoshima_value_list.insert(0, "豊島　将之先生(評価値の年平均)")
        writer.writerow(toyoshima_value_list)
        toyoshima_count_list.insert(0, "豊島　将之先生(棋譜の個数)")
        writer.writerow(toyoshima_count_list)

        nagase_value_list.insert(0, "永瀬　拓矢先生(評価値の年平均)")
        writer.writerow(nagase_value_list)
        nagase_count_list.insert(0, "永瀬　拓矢先生(棋譜の個数)")
        writer.writerow(nagase_count_list)
    """