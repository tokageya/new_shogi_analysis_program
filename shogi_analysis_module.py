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

    first_match_rate = (float(first_match_num)) / first_actual_count
    second_match_rate = (float(second_match_num)) / second_actual_count 
    return [first_match_rate, second_match_rate]


"""
search_suisho4_analysis_file_list 関数
    指定したディレクトリ下(サブディレクトリも検索する)に存在する解析済みの棋譜ファイル( ファイル名の末端が"_suisho4analysis.kif" )を検索してリストで返す
    (存在しなかった場合は [] を返す)
"""
def search_suisho4_analysis_file_list(dir_name):
    return glob.glob(dir_name+r"\**\*_suisho4analysis.kif", recursive=True)

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
calculation_move_concordance_rate_average_by_kishi_name 関数
    引数で渡されたディレクトリ内に存在する解析済みの棋譜ファイル( ファイル名の末端が"_suisho4analysis.kif" )について、引数で指定された手数の間のAIとの着手一致率の平均を1人の将棋棋士に対して求めて返す
"""
def calculation_move_concordance_rate_average_by_kishi_name(dir_name, start_move_num , last_move_num, kishi_family_name, kishi_last_name, begin_datetime, end_datetime):
    file_list = search_suisho4_analysis_file_list(dir_name)
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
        #print(kif_datetime)

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
            elif read_bool is True and words[0] == "**解析": # 解析の出力行
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
        boad_values = read_board_evaluation_values(file)
        diff_ai_list = []
        if (first_family_name == kishi_family_name) and (first_last_name == kishi_last_name):
            for i in range(len(boad_values)):
                if (i % 2 == 0) and (boad_values[i] is not None) and ((i+1) < len(boad_values)) and (boad_values[i+1] is not None):
                    diff_ai_list.append(boad_values[i] - boad_values[i+1])
        elif (second_family_name == kishi_family_name) and (second_last_name == kishi_last_name):
            for i in range(len(boad_values)):
                if (i % 2 == 1) and (boad_values[i] is not None) and ((i+1) < len(boad_values)) and (boad_values[i+1] is not None):
                    diff_ai_list.append(boad_values[i] - boad_values[i+1])
        values_sum += sum(diff_ai_list)
        count_sum += len(diff_ai_list)
    
    return values_sum / count_sum