# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    zgwh = pd.read_csv('策划.mycsv')
    rw = pd.read_csv('管理.mycsv')
    rwzj = pd.read_csv('经济学.mycsv')
    zj = pd.read_csv('股票.mycsv')
    ez = pd.read_csv('营销.mycsv')
    fj = pd.read_csv('金融.mycsv')
    zgwh_nums = zgwh['nums']
    zgwh_peoples = zgwh['peoples']
    ez_nums = ez['nums']
    ez_peoples = ez['peoples']
    rw_nums = rw['nums']
    rw_peoples = rw['peoples']
    rwzj_nums = rwzj['nums']
    rwzj_peoples = rwzj['peoples']
    zj_nums = zj['nums']
    zj_peoples = zj['peoples']
    fj_nums = fj['nums']
    fj_peoples = fj['peoples']
    flg = plt.figure(figsize=(12,6))
    ax1 = flg.add_subplot(2,3,1)
    ax2 = flg.add_subplot(2,3,2)
    ax3 = flg.add_subplot(2,3,3)
    ax4 = flg.add_subplot(2,3,4)
    ax5 = flg.add_subplot(2,3,5)
    ax6 = flg.add_subplot(2,3,6)
    ax1.scatter(zgwh_nums,zgwh_peoples,12)
    ax1.set_xlabel('score')
    ax1.set_ylabel('evaluation')
    ax2.scatter(ez_nums,ez_peoples,12)
    ax2.set_xlabel('score')
    ax2.set_ylabel('evaluation')
    ax3.scatter(rw_nums,rw_peoples,12)
    ax3.set_xlabel('score')
    ax3.set_ylabel('evaluation')
    ax4.scatter(rwzj_nums,rwzj_peoples,12)
    ax4.set_xlabel('score')
    ax4.set_ylabel('evaluation')
    ax5.scatter(zj_nums,zj_peoples,12)
    ax5.set_xlabel('score')
    ax5.set_ylabel('evaluation')
    ax6.scatter(fj_nums,fj_peoples,12)
    ax6.set_xlabel('score')
    ax6.set_ylabel('evaluation')
    plt.show()