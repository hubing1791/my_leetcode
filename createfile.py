# 根据题目链接自动生成子目录及写入初始文件

import os
import datetime
paths = [
    './cracking_the_code_intreview/',
    './extra_practice/',
    './leetcode_main/',
    './sword/'
]

# 和paths对应，表示某个目录下可能需要添加的前缀名
pre_list = ['', '', '', 'sword_']

levels = [
    'easy',
    'medium',
    'difficult',
]


def create_information(path_num: int, link: str, level_num: int, pro_num: str, name_str=''):
    if name_str == '':
        name_str = link.split('/')[-2].replace('-', '_')
    sub_path_name = pre_list[path_num] + pro_num + '_' + levels[level_num] + '_' + name_str
    full_path = paths[path_num] + sub_path_name + '/'
    is_exists = os.path.exists(full_path)
    if not is_exists:
        os.mkdir(full_path)
    f = open(full_path + 'problem.md', 'w', encoding='utf-8')
    f = open(full_path + 'solution.py', 'w', encoding='utf-8')
    f.write('')
    now_date = datetime.date.today().__str__()
    f.write('# '+link+'\n')
    f.write('# '+ now_date+'\n\n')


if __name__ == '__main__':
    create_information(3, 'https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/',
                       0, "54", 'kth_Largest')

