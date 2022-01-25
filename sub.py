from file_rename_module import *



if __name__ == "__main__":
    #print(search_kif_file_list(MASTER_DIR["tmp"]))

    for file in search_kif_file_list(MASTER_DIR["tmp"]):
        print(file)
        rename_file_tmp(file)
    
    """
    for i,v in MASTER_DIR.items():
        for file in search_kif_file_list(v):
            print(file)
            rename_file(file)
        print("\n======\n")
    """