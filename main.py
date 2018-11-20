#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Conversor

import win_conversor, wx

app = wx.App()

frame = win_conversor.win_conversor(None)
frame.Show()

app.MainLoop()
