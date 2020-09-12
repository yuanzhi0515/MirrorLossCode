import tensorflow as tf
import numpy as np


def mirror_modify(mirror_original, game = None):
    if game =='Pong':
        return mirror_modify
    elif game =='Breakout':
        position = {0:[0,2],1:[3,4],2:[2,3]}
    elif game == 'Qbert':
        position = {0:[0,3],1:[4,5],2:[3,4],3:[5,6]}
    elif game == 'BeamRider':
        position = {0:[0,3],1:[4,5],2:[3,4],3:[6,7],4:[5,6],5:[8,9],6:[7,8]}
    elif game == 'Enduro':
        position = {0:[0,2],1:[3,4],2:[2,3],3:[4,5],4:[6,7],5:[5,6],6:[8,9],7:[7,8]}
    elif game == 'Seaquest':
        position = {0:[0,3],1:[4,5],2:[3,4],3:[5,6],4:[7,8],5:[6,7],6:[9,10],7:[8,9],8:[10,11],9:[12,13],10:[11,12],11:[13,14],12:[15,16],13:[14,15],14:[17,18],15:[16,17]}
    elif game == None:
        print('Sorry, the mirror mapping infomation is not in the mirror_modify function. No change will be done')
        return mirror_original
    lenp=len(position)
    part = []
    for i in range(lenp):
        left = position[i][0]
        right = position[i][1]
        part.append(mirror_original[:,left:right])
    mirror_final = tf.concat(part,axis=1)
    return mirror_final


def test_action(actions, game=None):
    if game == 'Pong':
        return actions
    elif game == 'Breakout':
        actionmap = {0:0,1:1,2:3,3:2}
    elif game == 'Qbert':
        actionmap = {0:0,1:1,2:2,3:4,4:3,5:5}
    elif game =='BeamRider':        
        actionmap = {0:0,1:1,2:2,3:4,4:3,5:6,6:5,7:8,8:7}
    elif game == 'Euduro':
        actionmap = {0:0,1:1,2:3,3:2,4:4,5:6,6:5,7:8,8:7}
    elif game == 'Seaquest':
        actionmap = {0:0,1:1,2:2,3:4,4:3,5:5,6:7,7:6,8:9,9:8,10:10,11:12,12:11,13:13,14:15,15:14,16:17,17:16}
    elif game == None:
        print('Sorry, the mirror mapping infomation is not in the test_action function. No change will be done')
        return actions
    for i in range(len(actions)):
        actions[i] = actionmap[actions[i]]
    return actions