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
                for filename in os.listdir(path):
                        if endsWith(filename,'.ass','.ssa','.srt'):
                                print (namelist[i] + os.path.splitext(filename)[1])
                                os.rename(filename, namelist[i] + os.path.splitext(filename)[1])
                                i += 1
                print('修改成功！')
        elif (subtitleNum == videoNum*2) and (Type == 'y'):
                for filename in os.listdir(path):
                        subtitleType = re.findall(".*[.](.*)[.].*",filename)
                        if subtitleType:
                                print (subtitleType[0])
                                if ('sc' in subtitleType[0]) or ('chs' in subtitleType[0]):
                                        if endsWith(filename,'.ass','.ssa','.srt'):
                                                print (namelist[i] + '.' + subtitleType[0] + os.path.splitext(filename)[1])
                                                os.rename(filename, namelist[i] + '.' + subtitleType[0] + os.path.splitext(filename)[1])
                                elif ('tc' in subtitleType[0]) or ('cht' in subtitleType[0]):
                                        if endsWith(filename,'.ass','.ssa','.srt'):
                                                i -= 1
                                                print (namelist[i] + '.' + subtitleType[0] + os.path.splitext(filename)[1])
                                                os.rename(filename, namelist[i] + '.' + subtitleType[0] + os.path.splitext(filename)[1])
                                i += 1
                print('修改成功！')
        else:
                print('参数错误，请修改！')

if __name__ == '__main__':
        path = './'
#       设置文件路径     
        Type = input("是否同时含有简体字幕与繁体字幕（y/n）")
        getFileName(path,Type)
