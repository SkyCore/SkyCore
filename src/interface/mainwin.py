# Copyright (C) 2010 SkyCore <http://github.com/imetallica/SkyCore>

import sys
sys.path.append('../lang')

from intb import *
from langlinker import *

# Main window builder

win = Tk()
App = c_WinBuild(win)
lang = DoSelectLanguageImport()

menuName  = lang.menuName()
menu0Name = lang.menu0Name()
menu1Name = lang.menu1Name()

# Build Menu 0
App.f_CreateMenu

win.mainloop()
