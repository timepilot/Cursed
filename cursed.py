#Cursed is a wrapper for Python's Curses module
#By default, Python for Windows doesn't support
#Curses. However, it can be downloaded here:
#http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses
#
#Cursed was created by Luke Martin (flags)
#This program is free software. It comes without any warranty, to
#the extent permitted by applicable law. You can redistribute it
#and/or modify it under the terms of the Do What The Fuck You Want
#To Public License, Version 2, as published by Sam Hocevar. See
#http://sam.zoy.org/wtfpl/COPYING for more details.
import sys

try:
	import curses
except:
	print 'This terminal/version of Python doesn\'t support curses.'
	print 'If you are on Windows, download curses-2.2 from'
	print 'http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses'
	sys.exit()

class cursed:
	def __init__(self):
		self.screen = [{'name':'main','win':curses.initscr()}]

		curses.noecho()
		curses.cbreak()
		self.screen[0]['win'].keypad(1)
		curses.curs_set(0)
	
	def new_window(self,name,spos,epos):
		win = curses.newwin(epos[1]-spos[1], epos[0]-spos[0], spos[0], spos[1])
		self.screen.append({'name':name,'win':win})
	
	def get_char(self):
		return self.screen[0]['win'].getch()
	
	def get_str(self):
		curses.nocbreak();
		curses.echo();
		self.screen[0]['win'].addstr(24,0, '> ')
		curses.curs_set(1)
		s = self.screen[0]['win'].getstr();
		curses.curs_set(0)
		self.clear_line(24)
		curses.noecho();
		curses.cbreak();
		
		return s
	
	def clear_line(self,line,char=' '):
		for i in range(0,79):
			self.screen[0]['win'].addstr(line,i, char)
	
	def write(self,name,text,pos):
		for screen in self.screen:
			if screen['name'] == name:
				screen['win'].addstr(pos[1],pos[0], text)
				screen['win'].refresh()
				return True
	
	def end(self):
		curses.nocbreak();
		self.screen[0]['win'].keypad(0);
		curses.echo()
		curses.endwin()

_c = cursed()

while 1:
	c = _c.get_char()
	if c == ord('p'): _c.write('main','derp',(0,0))
	elif c == ord('w'): s = _c.get_str(); _c.write('main',s,(0,0))
	elif c == ord('q'): break  # Exit the while()
	elif c == curses.KEY_HOME: x = y = 0

_c.end()