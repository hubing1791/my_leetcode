from collections import defaultdict
from typing import List


# 简化了下输入
def hot_words(n: int, str_list: List[str]):
    # 映射次数到单词集合的字典,和根据单词查次数的
    top_dict = defaultdict(set)
    word_times = defaultdict(int)
    # 记录标题中出现顺序的字典
    title_dict = defaultdict(int)
    title_count = 1
    # 记录文章中出现顺序的字典
    article_dict = defaultdict(int)
    article_count = 1
    # 开始数数
    length = len(str_list)
    for i in range(length):
        word_list = str_list[i].split()
        # 对于标题和文章分别处理
        if i % 2 == 0:
            for word in word_list:
                word_times[word] += 1
                if word not in title_dict:
                    title_dict[word] = title_count
                    title_count += 1
        else:
            # 正文的词一定会有很多重复，因此直接全部遍历处理时间代价过大
            # 后来想了下看文章结构，越长的文章我这样写越赚
            for word in word_list:
                word_times[word] += 1
                if word not in article_dict:
                    article_dict[word] = article_count
                    article_count += 1
    # print(word_times,"\n",title_dict,"\n",article_dict)
    # 记录下最高频率以方便倒遍历
    max_fr = 0
    for key, value in word_times.items():
        top_dict[value].add(key)
        max_fr = max(max_fr, value)
    result = []
    for fr in range(max_fr, 0, -1):
        # 还需要补充的元素个数
        num_left = n - len(result)
        if num_left == 0:
            return result
        if fr in top_dict and len(top_dict[fr]) <= num_left:
            result.extend(top_dict[fr])
        else:
            # 先按标题里排序
            tmp_sort_title = []
            tmp_sort_article = []
            for word in top_dict[fr]:
                if word in title_dict:
                    tmp_sort_title.append([word, title_dict[word]])
                else:
                    tmp_sort_article.append([word, article_dict[word]])
            # print(tmp_sort_title,"\n",tmp_sort_article)
            if len(tmp_sort_title) >= num_left:
                tmp_sort_title.sort(key=lambda x: x[1])
                for i in range(num_left):
                    result.append(tmp_sort_title[i][0])
                return result
            else:
                tmp_sort_title.sort(key=lambda x: x[1])
                tmp_sort_article.sort(key=lambda x: x[1])
                tmp_sort = tmp_sort_title + tmp_sort_article
                for i in range(num_left):
                    result.append(tmp_sort[i][0])
                return result


if __name__ == '__main__':
    test_set = [
        # 这里list，is，no都出现了3次，按排序规则应该返回list和is
        [2,["list","list is best","tuple","no tuple is best no list no is"]]
    ]
    for top_n,t_a_list in test_set:
        print(hot_words(top_n,t_a_list))
