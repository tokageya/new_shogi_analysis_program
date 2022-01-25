from re import match
from typing import Match
from shogi_analysis_module import *
import csv

if __name__=="__main__":
    ANALYSIS_START_TURN = 81 # 最初のターン
    ANALYSIS_LAST_TURN = 300 # 最後のターン
    JUNNISEN_PREMIER_NUMBER = 44 # 最初の順位戦のタイミング
    JUNNISEN_LATEST_NUMBER = 79 # 最後の順位戦のタイミング
    suisho2_match_rate = []
    suisho2_file_count = []
    elmo_match_rate=[]
    elmo_file_count=[]
    suisho4kai_match_rate = []
    suisho4kai_file_count = []
    for number in list(range(JUNNISEN_LATEST_NUMBER, JUNNISEN_PREMIER_NUMBER-1, -1 )):
        """
        # A級
        print("MASTER_DIR[(\"No\"+str(number))][\"A級\"] : ")
        print(MASTER_DIR[("No"+str(number))]["A級"])
        [a_count, a_rate] = calculation_move_concordance_rate_average(number, MASTER_DIR[("No"+str(number))]["A級"], ANALYSIS_START_TURN, ANALYSIS_LAST_TURN)
        print("No"+str(number)+"__"+str(ANALYSIS_START_TURN)+"~"+str(ANALYSIS_LAST_TURN)+" rate:"+str(a_rate))
        classA_match_rate.insert(0, a_rate)
        classA_file_count.insert(0, a_count)
        """


        # 水匠2の順位戦B級1組
        [suisho2_count, suisho2_rate] = calculation_move_concordance_rate_average_for_suisho2(number, MASTER_DIR["水匠2"][("No"+str(number))], ANALYSIS_START_TURN, ANALYSIS_LAST_TURN)
        print("[水匠2] No"+str(number)+"__"+str(ANALYSIS_START_TURN)+"~"+str(ANALYSIS_LAST_TURN)+" rate:"+str(suisho2_rate))
        suisho2_match_rate.insert(0, suisho2_rate)
        suisho2_file_count.insert(0, suisho2_count)

        # 水匠4改の順位戦B級1組
        [suisho4kai_count, suisho4kai_rate] = calculation_move_concordance_rate_average(number, MASTER_DIR["水匠4改"][("No"+str(number))]["B級1組"], ANALYSIS_START_TURN, ANALYSIS_LAST_TURN)
        print("[水匠4改] No"+str(number)+"__"+str(ANALYSIS_START_TURN)+"~"+str(ANALYSIS_LAST_TURN)+" rate:"+str(suisho4kai_rate))
        suisho4kai_match_rate.insert(0, suisho4kai_rate)
        suisho4kai_file_count.insert(0, suisho4kai_count)

        # elmoの順位戦B級1組
        [elmo_count, elmo_rate] = calculation_move_concordance_rate_average_for_elmo(number, MASTER_DIR["elmo"][("No"+str(number))], ANALYSIS_START_TURN, ANALYSIS_LAST_TURN)
        print("[elmo] No"+str(number)+"__"+str(ANALYSIS_START_TURN)+"~"+str(ANALYSIS_LAST_TURN)+" rate:"+str(elmo_rate))
        elmo_match_rate.insert(0, elmo_rate)
        elmo_file_count.insert(0, elmo_count)

    print("=== suisho2_match_rate ===")
    print(suisho2_match_rate)
    print("=== suisho4kai_match_rate ===")
    print(suisho4kai_match_rate)
    print("=== elmo_match_rate ===")
    print(elmo_match_rate)
    #"""
    """
    watanabe_value_list = []
    watanabe_count_list = []
    fujii_value_list = []
    fujii_count_list = []
    toyoshima_value_list = []
    toyoshima_count_list = []
    nagase_value_list = []
    nagase_count_list = []
    print("--- 渡辺先生 ---")
    for year in range(2000, 2021):
        value_list = calculation_move_concordance_rate_average_by_kishi_name(MASTER_DIR["渡辺"],ANALYSIS_START_TURN, ANALYSIS_LAST_TURN, "渡辺", "明", YEAR_HASH[str(year)][0], YEAR_HASH[str(year)][1])
        print(str(year) + " : "+str(value_list[1]))
        watanabe_value_list.append(value_list[1])
        watanabe_count_list .append(value_list[0])
    print("--- 藤井先生 ---")
    for year in range(2000, 2021):
        value_list = calculation_move_concordance_rate_average_by_kishi_name(MASTER_DIR["藤井"],ANALYSIS_START_TURN, ANALYSIS_LAST_TURN, "藤井","聡太" , YEAR_HASH[str(year)][0], YEAR_HASH[str(year)][1])
        print(str(year) + " : "+str(value_list[1]))
        fujii_value_list.append(value_list[1])
        fujii_count_list.append(value_list[0])
    print("--- 豊島先生 ---")
    for year in range(2000, 2021):
        value_list = calculation_move_concordance_rate_average_by_kishi_name(MASTER_DIR["豊島"],ANALYSIS_START_TURN, ANALYSIS_LAST_TURN, "豊島","将之" , YEAR_HASH[str(year)][0], YEAR_HASH[str(year)][1])
        print(str(year) + " : "+str(value_list[1]))
        toyoshima_value_list.append(value_list[1])
        toyoshima_count_list.append(value_list[0])
    print("--- 永瀬先生 ---")
    for year in range(2000, 2021):
        value_list = calculation_move_concordance_rate_average_by_kishi_name(MASTER_DIR["永瀬"],ANALYSIS_START_TURN, ANALYSIS_LAST_TURN, "永瀬","拓矢" , YEAR_HASH[str(year)][0], YEAR_HASH[str(year)][1])
        print(str(year) + " : "+str(value_list[1]))
        nagase_value_list.append(value_list[1])
        nagase_count_list.append(value_list[0])
    """
    # csv ファイル出力
    
    with open("./result_kifu_analysis_concordance_rate_average.csv", "w", newline="") as f:
        writer = csv.writer(f)

        list_tmp = ["年度"]
        for i in list(range(1985,2021)):
            list_tmp.append(i)
        writer.writerow(list_tmp)

        suisho2_match_rate.insert(0, "水匠2(年平均)")
        writer.writerow(suisho2_match_rate)
        #classA_file_count.insert(0, "A級の棋譜の個数")
        #writer.writerow(classA_file_count)

        suisho4kai_match_rate.insert(0, "水匠4改(年平均)")
        writer.writerow(suisho4kai_match_rate)
        #classB_file_count.insert(0, "B級1組の棋譜の個数")
        #writer.writerow(classB_file_count)

        elmo_match_rate.insert(0, "elmo(年平均)")
        writer.writerow(elmo_match_rate)
        #classB_file_count.insert(0, "B級1組の棋譜の個数")
        #writer.writerow(classB_file_count)
    