# -*- coding: utf-8 -*-
import os
'''
使用前请保持待修改的字幕数量与对应的视频数量一致
'''
def endsWith(s,*endstring):
        array = map(s.endswith,endstring)
        if True in array:
                return True
        else:
                return False

def getFileName(path):
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
        if videoNum == subtitleNum:
                for filename in os.listdir('.'):
                        if endsWith(filename,'.ass','.ssa','.srt'):
                                print (namelist[i] + os.path.splitext(filename)[1])
                                os.rename(filename, namelist[i] + os.path.splitext(filename)[1])
                                i += 1
                print('修改成功！')
        else:
                print('字幕数量与视频数量不匹配，请修改！')
        

if __name__ == '__main__':
        path = './'
        getFileName(path)
