#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 martian <supermartian@gmail.com>
#
# Distributed under terms of the MIT license.

import game

class boardEvaluator:
    def __init__(self, gameBoard):
        self.board = gameBoard.board
        self.maxtile = gameBoard.maxtile
        print "max ", self.maxtile

    def cornerEvaluate(self):
        if ((self.board[0][0] == self.maxtile) or
        (self.board[3][0] == self.maxtile) or
        (self.board[0][3] == self.maxtile) or
        (self.board[3][3] == self.maxtile)):
            return 5
        else:
            return 0

    def blankEvaluate(self):
        ret = 0
        for i in range(4):
            for j in range(4):
                ret += 1 if self.board[i][j] == 0 else 0
        return ret

    def smoothnessEvaluate(self):
        ret = 0

        "Horizontal lines"
        for i in range(4):
            intr = []
            for j in range(1, 4):
                intr.append(self.board[i][j] - self.board[i][j - 1])
            ret += 1 if min(intr) * max(intr) >= 0 else 0

        "Vertical lines"
        for i in range(4):
            intr = []
            for j in range(1, 4):
                intr.append(self.board[j][i] - self.board[j - 1][i])
            ret += 1 if min(intr) * max(intr) >= 0 else 0

        return ret

    def boardHeuristic(self):
        ret = 0
        ret += self.cornerEvaluate()
        ret += self.blankEvaluate()
        ret += self.smoothnessEvaluate()
        return ret

class boardSolver:
    def __init__(self, gameBoard):
        self.evaluator = boardEvaluator(gameBoard)
        self.game = gameBoard
