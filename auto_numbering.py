# -*- coding: utf-8 -*-
import sys

# 行頭のタブ文字の数を数える
def count_tab(line):
    tab = 0
    for c in line:
        if c == '\t':
            tab += 1
        else:
            break
    return tab

# 引数チェック。引数がない場合は使い方を表示して終了。
def check_args(args):
    if len(args) <= 1:
        print("usage: python auto_numbering.py <file>")
        sys.exit()

# テーマ数を求める。テーマ数はスタック構造なので、スタックもこの関数で更新する。
def theme_number(theme_stack, tab):
    while (len(theme_stack) > tab + 1):
        theme_stack.pop()
    while (len(theme_stack) <= tab):
        theme_stack.append(0)
    theme_stack[tab] += 1
    return theme_stack[tab];

# タブ数に応じたテーマを考慮してをテーマ文字列を返す。
def theme_string(list, theme, tab):
    t1 = list[tab][theme - 1]
    return t1

if __name__ == '__main__':
    args = sys.argv
    check_args(args)
    theme_list = []

    # テーマ文字列の初期化
    with open("moji.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            theme_list.append(line.split(" "))

    # ファイルを読み込んで採番
    with open(args[1], "r") as file:
        strings = file.readlines()
        theme_stack = []
        enable = True
        i = 0
        for line in strings:
            tab = count_tab(line)

            # 子テーマが1行しかない場合は採番しない
            if i > 0 and i < len(strings):
                tab_before = count_tab(strings[i-1])
                tab_after = count_tab(strings[i+1])
                # print("b:" + str(tab_before) +  "a:" + str(tab_after) , end = "")
                if tab > tab_before and tab > tab_after:
                    print(line, end = "")
                    i += 1
                    continue

            i += 1
            # '#'が含まれる行が来たら次に'#'が見つかるまで無視する
            if line.count('#') > 0:
                enable = not enable
                print(line, end = "")
                continue

            # 空行でなければ採番
            if enable == True and len(line) > tab + 1:
                theme = theme_number(theme_stack, tab) 
                theme_str = theme_string(theme_list, theme, tab)
                tabs = line[0:tab]
                body = line[tab:len(line)]
                print(tabs + theme_str + body, end = "")
            else:
                print(line, end = "")

