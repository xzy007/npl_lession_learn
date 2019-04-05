import jieba
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt #D:\ProgramData\Anaconda3\pkgs\matplotlib-3.0.2-py37hc8f65d3_0\Lib\site-packages\matplotlib\mpl-data\matplotlibrc文件中的backend      : Agg需要打开
import math


# 创建停用词list
def stopwordslist(filepath):
    stopwords = set([line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()])
    return stopwords

def get_word_tf():
    stop_word = stopwordslist("jieba_stop_word.txt")
    with open('完美世界.txt', 'r', encoding='utf-8') as f:
        all_lines = 0
        total_lines = 0
        total_words = 0
        word_tf = {}
        for line in f.readlines():
            all_lines += 1
            line = line.strip()
            if len(line) == 0:
                continue
            total_lines += 1
            for word in jieba.cut(line):
                if word in stop_word:
                    continue
                word_tf[word] = word_tf[word] + 1 if word in word_tf else 1
                total_words += 1
            # if len(word_tf) > 10:
            #     break
        print("all lines: %d"%all_lines)
        print("total lines: %d"%total_lines)
        print("total words: %d"%total_words)
        sort_res = sorted(word_tf.items(), key=lambda x:x[1], reverse=True)
        print("top 10 words:")
        print('\n'.join(["%s:%d"%(word, tf) for (word, tf) in sort_res[:10]]))
        return sort_res

def plot_point(res):
    plt.plot([math.log(i + 1) for i in range(len(res))], res, 'ro')
    plt.show()

if __name__ == "__main__":
    sort_res = get_word_tf()
    res = [math.log(tf) for (word, tf) in sort_res]
    plot_point(res)
