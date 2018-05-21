# -*- coding: utf-8 -*-
import sys

# �s���̃^�u�����̐��𐔂���
def count_tab(line):
    tab = 0
    for c in line:
        if c == '\t':
            tab += 1
        else:
            break
    return tab

# �����`�F�b�N�B�������Ȃ��ꍇ�͎g������\�����ďI���B
def check_args(args):
    if len(args) <= 1:
        print("usage: python auto_numbering.py <file>")
        sys.exit()

# �e�[�}�������߂�B�e�[�}���̓X�^�b�N�\���Ȃ̂ŁA�X�^�b�N�����̊֐��ōX�V����B
def theme_number(theme_stack, tab):
    while (len(theme_stack) > tab + 1):
        theme_stack.pop()
    while (len(theme_stack) <= tab):
        theme_stack.append(0)
    theme_stack[tab] += 1
    return theme_stack[tab];

# �^�u���ɉ������e�[�}���l�����Ă��e�[�}�������Ԃ��B
def theme_string(list, theme, tab):
    t1 = list[tab][theme - 1]
    return t1

if __name__ == '__main__':
    args = sys.argv
    check_args(args)
    theme_list = []

    # �e�[�}������̏�����
    with open("moji.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            theme_list.append(line.split(" "))

    # �t�@�C����ǂݍ���ō̔�
    with open(args[1], "r") as file:
        strings = file.readlines()
        theme_stack = []
        enable = True
        i = 0
        for line in strings:
            tab = count_tab(line)

            # �q�e�[�}��1�s�����Ȃ��ꍇ�͍̔Ԃ��Ȃ�
            if i > 0 and i < len(strings):
                tab_before = count_tab(strings[i-1])
                tab_after = count_tab(strings[i+1])
                # print("b:" + str(tab_before) +  "a:" + str(tab_after) , end = "")
                if tab > tab_before and tab > tab_after:
                    print(line, end = "")
                    i += 1
                    continue

            i += 1
            # '#'���܂܂��s�������玟��'#'��������܂Ŗ�������
            if line.count('#') > 0:
                enable = not enable
                print(line, end = "")
                continue

            # ��s�łȂ���΍̔�
            if enable == True and len(line) > tab + 1:
                theme = theme_number(theme_stack, tab) 
                theme_str = theme_string(theme_list, theme, tab)
                tabs = line[0:tab]
                body = line[tab:len(line)]
                print(tabs + theme_str + body, end = "")
            else:
                print(line, end = "")

