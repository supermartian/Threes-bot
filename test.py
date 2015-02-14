#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 Yuzhong Wen <supermartian@gmail.com>
#
# Distributed under terms of the MIT license.

import game
import random

g = game.gameBoard()
g.initRandomBoard()
while g != None:
    m = random.randint(0, 4)
    print ''
    g.printBoard()
    g = g.getNextState(m)
