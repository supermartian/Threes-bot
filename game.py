#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Yuzhong Wen <supermartian@gmail.com>
#
# Distributed under terms of the MIT license.

import random
import copy

class gameBoard:

    def __init__(self, state = None):
        if state != None:
            self.board = copy.deepcopy(state)
        else:
            self.board = [[0 for i in xrange(4)] for i in xrange(4)]
        random.seed()

    def initRandomBoard(self):
        self.board = [[0 for i in xrange(4)] for i in xrange(4)]
        state = 0
        s = [0, 0, 0, 0]
        while not state == 9:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if self.board[x][y] != 0:
                continue
            n = random.randint(0, 3)
            if s[n] < 3 and n > 0:
                s[n] = s[n] + 1
                state += 1
            else:
                n = 0
            self.board[x][y] = n

        return self.board

    "0: Up, 1: Right, 2: Down, 3: Left"
    def getNextState(self, move):
        newboard = copy.deepcopy(self.board)
        tilemerged = False
        if move == 3 or move == 1:
            s = -1
            hrange = range(1, 4)
            if move == 3:
                s = -1
            else:
                s = 1
                hrange = range(2, -1, -1)
            for i in range(4):
                for j in hrange:
                    if ((newboard[i][j] == newboard[i][j + s] and newboard[i][j] >= 3) or
                            (newboard[i][j] == 2 and newboard[i][j + s] == 1) or
                            (newboard[i][j + s] == 2 and newboard[i][j] == 1) or
                            (newboard[i][j + s] == 0 and newboard[i][j] !=0)):
                                newboard[i][j + s] += newboard[i][j]
                                newboard[i][j] = 0
                                tilemerged = True
        elif move == 2 or move == 0:
            s = -1
            vrange = range(1, 4)
            if move == 3:
                s = -1
            else:
                s = 1
                vrange = range(2, -1, -1)
            for i in range(4):
                for j in vrange:
                    if ((newboard[j][i] == newboard[j + s][i] and newboard[j][i] >= 3) or
                            (newboard[j][i] == 2 and newboard[j + s][i] == 1) or
                            (newboard[j + s][i] == 2 and newboard[j][i] == 1) or
                            (newboard[j + s][i] == 0 and newboard[j][i] !=0)):
                                newboard[j + s][i] += newboard[j][i]
                                newboard[j][i] = 0
                                tilemerged = True
        if not tilemerged:
            return None
        else:
            return gameBoard(newboard)

    def addTile(self, x, y, tile):
        if self.board[x][y] != 0:
            return False
        else:
            self.board[x][y] = tile
            return True

    def printBoard(self):
        for i in range(4):
            print self.board[i]
