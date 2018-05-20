# -*- coding: utf-8 -*-
import sys

# �s���̃^�u�����̐��𐔂���
def count_tab(str):
    tab = 0
    for c in line:
        if c == '\t':
            tab += 1
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
def theme_string(theme, tab):
    theme_list1 = ['1', '1', '1','1']
    theme_list2 = ['. ', '. ', ') ',' ']
    t1 = chr(ord(theme_list1[tab]) + theme - 1)
    t2 = theme_list2[tab]
    return t1 + t2

if __name__ == '__main__':
    args = sys.argv
    check_args(args)

    with open(args[1], "r") as file:
        strings = file.readlines()
        theme_stack = []
        enable = True

        for line in strings:
            tab = count_tab(line)
            
            # '#'���܂܂��s�������玟��'#'��������܂Ŗ�������
            if line.count('#') > 0:
                enable = not enable
                print(line, end = "")
                continue

            # ��s�łȂ���΍̔�
            if enable == True and len(line) > tab + 1:
                theme = theme_number(theme_stack, tab) 
                theme_str = theme_string(theme, tab)
                tabs = line[0:tab]
                body = line[tab:len(line)]
                print(tabs + theme_str + body, end = "")
            else:
                print(line, end = "")
