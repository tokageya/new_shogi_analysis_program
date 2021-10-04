from file_rename_module import *

MASTER_DIR = {
    "渡辺" : r"C:\Users\msait\Documents\research\shogi\kifu\棋譜解析結果ファイル(渡辺明先生他)(水匠4)\渡辺明先生の棋譜解析結果",
    "藤井" : r"C:\Users\msait\Documents\research\shogi\kifu\棋譜解析結果ファイル(渡辺明先生他)(水匠4)\藤井聡太先生の棋譜解析結果",
    "豊島" : r"C:\Users\msait\Documents\research\shogi\kifu\棋譜解析結果ファイル(渡辺明先生他)(水匠4)\豊島将之先生の棋譜解析結果",
    "永瀬" : r"C:\Users\msait\Documents\research\shogi\kifu\棋譜解析結果ファイル(渡辺明先生他)(水匠4)\永瀬先生の棋譜解析結果"
}

if __name__ == "__main__":
    for i,v in MASTER_DIR.items():
        for file in search_kif_file_list(v):
            print(file)
            rename_file(file)
        print("\n======\n")
