from wordcloud import WordCloud
import matplotlib.pyplot as plt


if __name__ == '__main__':
    f = open(u'data.txt','r').read()
    word = WordCloud(background_color='white',width=1000,height=860,margin=2).generate(f)
    plt.imshow(word)
    plt.axis('off')
    plt.show()
    word.to_file('test.png')
