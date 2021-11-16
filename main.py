from shogi_analysis_module import *

if __name__=="__main__":

    # 手順1. search_suisho4_analysis_file_list関数で、棋譜ファイル名のリストを取得

    # 手順2. それぞれの棋譜ファイルに対して、条件に合う手数でのcreate_new_fileを一つ一つ行う
    kif_file_name = r"C:\Users\msait\Downloads\tmp\19850614小林健二田丸昇_analysis.KIF"
    
    values_list = read_board_evaluation_values(kif_file_name)
    print(values_list)
    values_list = [i for i in values_list if i != None]
    print("=== after remove None ===")
    print(values_list)

    diff_list = [] # 評価値の変動した値の差のリスト
    for i in range(len(values_list) - 1):
        diff_list.append(abs(values_list[i+1] - values_list[i]))

    #print(sum(diff_list)/len(diff_list))
    for i in range(len(diff_list) - 1):
        if diff_list[i] > (sum(diff_list)/len(diff_list)):
            create_new_file( kif_file_name, i+1, kif_file_name.replace(".KIF", "_turn"+str(i+1)+".KIF") )

