import os
import glob # ファイル名検索
from statistics import variance # 分散表示

TURN_NUM = 40 # 対象とする序・中盤のターン数

"""
search_kif_file_list 関数
    指定したディレクトリ下に存在する解析済みの棋譜ファイル( ファイル名の末端が".KIF" )を検索してリストで返す
    (存在しなかった場合は [] を返す)
"""
def search_kif_file_list(dir_name):
    #print(glob.glob(dir_name+r"\**\*.KIF", recursive=True))
    return glob.glob(dir_name+r"\**\*.KIF", recursive=True)

"""
rename_file 関数
    ファイル名を受け取って、新しいフォーマットのファイル名に変更する
    ex. 19850614小林健二田丸昇.KIF => 19850614小林 健二－田丸 昇_suisho4analysis.kif
"""
def rename_file(file_name):
    file_pass = file_name[:(file_name.rfind("\\")+1)] # ファイルのパス
    new_file_name = file_name[(file_name.rfind("\\")+1):] # 新しいファイル名
    if ".kif" in file_name:
        print("--- file name \"" + file_name + "\" already changed ---")
        return
    
    is_2 = False
    if "2.KIF" in file_name:
        print("=== 2.KIF FILE ===")
        is_2 = True

    first_family_name = "" # 先手の性
    first_last_name = "" # 先手の名
    second_family_name = "" # 後手の性
    second_last_name = "" # 後手の名
    # 1. ファイルの中身から先手, 後手それぞれの性, 名を読み取る
    with open(file_name, mode="r", encoding="cp932") as file:
        for line in file.readlines():
            if line.find("先手姓：") != -1:
                first_family_name = line[4:].strip()
            elif line.find("先手名：") != -1:
                first_last_name = line[4:].strip()
            elif line.find("後手姓：") != -1:
                second_family_name = line[4:].strip()
            elif line.find("後手名：") != -1:
                second_last_name = line[4:].strip()
    if "?" in first_family_name or "?" in first_last_name or "?" in second_family_name or "?" in second_last_name:
        if ("?" in first_last_name) and (r"けい" in file_name):
            first_last_name = first_last_name.replace("?", r"けい")
            print("first_last_name replaced.")
        elif ("?" in second_last_name) and (r"けい" in file_name):
            second_last_name = second_last_name.replace("?", r"けい")
            print("second_last_name replaced.")
        else:
            print("\n-----------------------")
            print("Error: ")
            print("first_family_name = \""+first_family_name+"\"")
            print("first_last_name = \""+first_last_name+"\"")
            print("second_family_name = \""+second_family_name+"\"")
            print("second_last_name = \""+second_last_name+"\"")
            print("file_name : \""+file_name+"\"")
            print("-----------------------")
            return
    
    # 2. 先手,後手の性と名の間に半角スペースを挿入
    if is_2 is True:
        new_file_name = file_pass + new_file_name[:8] + first_family_name + r" " + first_last_name + r"－" + second_family_name + r" " + second_last_name + r"2_suisho4analysis.kif"
    else:
        new_file_name = file_pass + new_file_name[:8] + first_family_name + r" " + first_last_name + r"－" + second_family_name + r" " + second_last_name + r"_suisho4analysis.kif"
    os.rename(file_name, new_file_name)
