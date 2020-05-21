# -*- coding: utf-8 -*-
import os
import re
'''
使用前请保持待修改的字幕集数与对应的视频数量一致
'''
def endsWith(s,*endstring):
    array = map(s.endswith,endstring)
    if True in array:
        return True
    else:
        return False

def getFileName(path,Type):
    namelist = []
    i = 0
    videoNum = 0
    subtitleNum = 0
    for filename in os.listdir(path):
        if endsWith(filename,'.mkv','.rmvb','.avi','.rm','.asf','.divx','.mpg','.mpeg','.mpe','.wmv','.mp4','.vob'):
            videoNum += 1
            shortname = os.path.splitext(filename)[0]
            namelist.append(shortname)
    #print (namelist)
    for filename in os.listdir(path):
        if endsWith(filename,'.ass','.ssa','.srt'):
            subtitleNum += 1
    if (videoNum == subtitleNum) and (Type == 'n'):
        sublist = []
        for filename in os.listdir(path):
            if endsWith(filename,'.ass','.ssa','.srt'):
                sublist.append(filename)
        namelist.sort()
        sublist.sort()
        for i in range(len(sublist)):
            print('视频名：  ',namelist[i])
            print('原字幕名：',sublist[i])
            print('更改后名：',namelist[i] + os.path.splitext(sublist[i])[1])
            print('='*20)
        flag = input('是否更改(Y/n)')
        if flag == 'Y' or flag =='y':
            for i in range(len(sublist)):
                print('视频名：  ',namelist[i])
                print('原字幕名：',sublist[i])
                print('更改后名：',namelist[i] + os.path.splitext(sublist[i])[1])
                os.rename(sublist[i], namelist[i] + os.path.splitext(sublist[i])[1])
                print('='*20)
        else:
            print('exiting...')
            exit()

        print('修改成功！')
    elif (subtitleNum == videoNum*2) and (Type == 'y'):
        scSubList = []
        tcSubList = []
        for filename in os.listdir(path):
            subtitleType = re.findall(".*[.](.*)[.].*",filename)
            if subtitleType:
                print (subtitleType[0])
                if ('sc' in subtitleType[0]) or ('chs' in subtitleType[0]):
                    if endsWith(filename,'.ass','.ssa','.srt'):
                        scSubList.append(filename)
                        #print (namelist[i] + '.' + subtitleType[0] + os.path.splitext(filename)[1])
                        #os.rename(filename, namelist[i] + '.' + subtitleType[0] + os.path.splitext(filename)[1])
                elif ('tc' in subtitleType[0]) or ('cht' in subtitleType[0]):
                    if endsWith(filename,'.ass','.ssa','.srt'):
                        tcSubList.append(filename)
                        #print (namelist[i] + '.' + subtitleType[0] + os.path.splitext(filename)[1])
                        #os.rename(filename, namelist[i] + '.' + subtitleType[0] + os.path.splitext(filename)[1])
        namelist.sort()
        scSubList.sort()
        tcSubList.sort()
        for i in range(len(namelist)):
            print('匹配视频名称：',namelist[i])
            print('-'*10)
            print('原简体字幕名：',scSubList[i])
            print('新简体字幕名：',namelist[i] + '.' + 'chs' + os.path.splitext(scSubList[i])[1])
            print('-'*10)
            print('原繁体字幕名：',tcSubList[i])
            print('新繁体字幕名：',namelist[i] + '.' + 'cht' + os.path.splitext(scSubList[i])[1])
            print('='*20)
        flag = input('是否修改(Y/n)')
        if flag == 'Y' or flag == 'y':
            for i in range(len(namelist)):
                print('匹配视频名称：',namelist[i])
                print('-'*10)
                print('原简体字幕名：',scSubList[i])
                print('新简体字幕名：',namelist[i] + '.' + 'chs' + os.path.splitext(scSubList[i])[1])
                os.rename(scSubList[i], namelist[i] + '.' + 'chs' + os.path.splitext(scSubList[i])[1])
                print('-'*10)
                print('原繁体字幕名：',tcSubList[i])
                print('新繁体字幕名：',namelist[i] + '.' + 'cht' + os.path.splitext(scSubList[i])[1])
                os.rename(tcSubList[i], namelist[i] + '.' + 'cht' + os.path.splitext(scSubList[i])[1])
                print('='*20)
        else:
            exit()
        print('修改成功！')
    else:
        if Type == 'n':
            print('[ERROR]字幕文件数量与视频文件数量不匹配！')
        elif Type == 'y':
            print('[ERROR]字幕文件数量与视频文件数量不匹配！')
        else:
            print('[ERROR]参数错误，请修改！')

if __name__ == '__main__':
    path = './'
#       设置文件路径     
    Type = input("是否同时含有简体字幕与繁体字幕（y/n）")
    getFileName(path,Type)
