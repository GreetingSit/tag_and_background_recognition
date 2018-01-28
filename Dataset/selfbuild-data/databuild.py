#build datasets
#code: 0-farm 1-laboratory 2-market 3-port 4-rainforest 5-room
#
#
import os
import random
import numpy as np
from PIL import Image

def gettagdict(background):
    '''
    :param background:background label
    :return tagdict
    '''
    dict={}
    if background==0:
        imgs=os.listdir('..//pictures_set//farm')
        for i in range(len(imgs)):
            if imgs[i]!='farm(176mmx250mm).png':
                dict[imgs[i]]= Image.open('..//pictures_set//farm//' + imgs[i])
    elif background==1:
        imgs = os.listdir('..//pictures_set//laboratory')
        for i in range(len(imgs)):
            if imgs[i] != 'laboratory(176mmx250mm).png':
                dict[imgs[i]] =  Image.open('..//pictures_set//laboratory//' + imgs[i])
    elif background==2:
        imgs = os.listdir('..//pictures_set//market')
        for i in range(len(imgs)):
            if imgs[i] != 'market(176mmx250mm).png':
                dict[imgs[i]] = Image.open('..//pictures_set//market//' + imgs[i])
    elif background==3:
        imgs = os.listdir('..//pictures_set//port')
        for i in range(len(imgs)):
            if imgs[i] != 'port(176mmx250mm).png':
                dict[imgs[i]] = Image.open('..//pictures_set//port//' + imgs[i])
    elif background==4:
        imgs = os.listdir('..//pictures_set//rainforest')
        for i in range(len(imgs)):
            if imgs[i] != 'rainforest(176mmx250mm).png':
                dict[imgs[i]] = Image.open('..//pictures_set//rainforest//' + imgs[i])
    elif background==5:
        imgs = os.listdir('..//pictures_set//room')
        for i in range(len(imgs)):
            if imgs[i] != 'room(176mmx250mm).png':
                dict[imgs[i]] =  Image.open('..//pictures_set//room//' + imgs[i])
    return dict

def getbackground(background):
    '''
    :param background: label of background
    :return: background
    '''
    bgimg=[]
    if background==0:
        bgimg=Image.open('..//pictures_set//farm//farm(176mmx250mm).png')
    elif background==1:
        bgimg = Image.open('..//pictures_set//laboratory//laboratory(176mmx250mm).png')
    elif background==2:
        bgimg = Image.open('..//pictures_set//market//market(176mmx250mm).png')
    elif background==3:
        bgimg = Image.open('..//pictures_set//port//port(176mmx250mm).png')
    elif background==4:
        bgimg = Image.open('..//pictures_set//rainforest//rainforest(176mmx250mm).png')
    elif background==5:
        bgimg = Image.open('..//pictures_set//room//room(176mmx250mm).png')
    return bgimg

def getpath(background):
    '''
    :param background: label of background
    :return: path
    '''
    path=''
    if background==0:
        path='farm//'
    elif background==1:
        path='laboratory//'
    elif background==2:
        path='market//'
    elif background==3:
        path='port//'
    elif background==4:
        path='rainforest//'
    elif background==5:
        path='room//'
    return path

def tagpaste(tag,bg,box):
    '''
    :param tag: tag we use
    :param bg: sorce pic
    :param box: location of tag
    :return: new pic
    '''
    tar=np.array(tag).astype(np.int8)
    src=np.array(bg).astype(np.int8)
    size =src.shape
    tagsize=tar.shape
    for r in range(box[0],min(box[0]+tagsize[0],size[0])):
        for c in range(box[1],min(box[1]+tagsize[1],size[1])):
            if sum(tar[r-box[0],c-box[1],:])!=0:
                src[r,c,:]=tar[r-box[0],c-box[1],:]
    return Image.fromarray(src.astype("uint8"))



def build(background,n):
    '''
    build random data
    :param background:label of background
    :param n: Number of new data:
    '''
    tagdict=gettagdict(background)
    bgimg=getbackground(background)
    savepath=getpath(background)
    pics=list(tagdict.keys())
    for i in range(n):
        temp={}
        k = random.randint(0,len(tagdict))+1
        for j in range(k):
            r=random.randint(0,len(pics)-1)
            temp[pics[r]]=tagdict[pics[r]]
        new = bgimg.copy()
        tempbg=bgimg.copy()
        for key in temp.keys():
            box=(random.randint(0,new.size[0]),random.randint(0,new.size[1]))
            temptag=temp[key].rotate(random.randint(0,360),expand=True,resample=Image.BICUBIC)
            new=tagpaste(temptag,tempbg,box)
            tempbg=new
        new.save(savepath+str(i)+'.png')
        if i % 5 == 0:
            print('finished pic '+ str(i) + '.png')

#test
build(0,10);






