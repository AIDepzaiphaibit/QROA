import pygame as pg
import ctypes
import time
from ctypes.wintypes import HWND, LPWSTR, UINT

pg.init()

_user32 = ctypes.WinDLL('user32', use_last_error=True)

_MessageBoxW = _user32.MessageBoxW
_MessageBoxW.restype = UINT
_MessageBoxW.argtypes = (HWND, LPWSTR, LPWSTR, UINT)

MB_OK = 0
MB_OKCANCEL = 1
MB_YESNOCANCEL = 3
MB_YESNO = 4

IDOK = 1
IDCANCEL = 2
IDABORT = 3
IDYES = 6
IDNO = 7

def MessageBoxW(hwnd, text, caption, utype):
	result = _MessageBoxW(hwnd, text, caption, utype)
	if not result:
		raise ctypes.WinError(ctypes.get_last_error())
	return result

screen = pg.display.set_mode((1024, 640))
pg.display.set_caption("QROA - test")


load = pg.image.load
zoom = pg.transform.scale

background = zoom(load('storage/background.png'), (1024, 640))
center = False
center_icon = load('storage/QROA-icon32x32.png')
taskbar = True

font = pg.font.SysFont('san', 32)

shutdown_icon = load('storage/shutdown-icon64x64.png')
shutdown = False

firefox = zoom(load('storage/firefoxlogo.png'), (32,32))
browser = firefox
browser_stat = 'not installed'

i_color = (132,170,186)
j_color = (92,129,145)
k_color = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
k_color[0]=j_color
k_color[1]=j_color

def MessageBoxW(hwnd, text, caption, utype):
	result = _MessageBoxW(hwnd, text, caption, utype)
	if not result:
		raise ctypes.WinError(ctypes.get_last_error())
	return result

def showCenter(val):
	if val == True:
		pg.draw.rect(screen, k_color[0], (0, 224, 288, 384))

run = True

while run:

	screen.fill('black')

	mouse = pg.mouse.get_pos()

	screen.blit(shutdown_icon, (0, 224))

	if taskbar == True:
		screen.blit(background, (0, 0))
		pg.draw.rect(screen, j_color, (0, 608, 1024, 32))

		def launchBrowser(val):
			if val == True:
				if browser_stat == 'not installed':
					try:
						result = MessageBoxW(None, "Bạn chưa tải Firefox mà :)", "Chịu", MB_OKCANCEL)
						if result == IDOK:
							pass
						if result == IDCANCEL:
							pass
					except WindowsError as win_err:
						print("An error occurred:\n{}".format(win_err))
					# print('f')
				if browser_stat == 'opening':
					try:
						result = MessageBoxW(None, "Firefox không hỗ trợ đâu :)", "Chịu", MB_OKCANCEL)
						if result == IDOK:
							pass
						if result == IDCANCEL:
							pass
					except WindowsError as win_err:
						print("An error occurred:\n{}".format(win_err))
					# print('k')

		#check row0
		if (0<mouse[0]<32) and (608<mouse[1]<640):
			k_color[0] = i_color
		else:
			k_color[0] = j_color
		pg.draw.rect(screen, k_color[0], (0, 608, 32, 32))

		#check row1
		if (32<mouse[0]<64) and (608<mouse[1]<640):
			k_color[1] = i_color
		else:
			k_color[1] = j_color
		pg.draw.rect(screen, k_color[1], (32, 608, 32, 32))

		screen.blit(center_icon, (0, 608))

	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
			shutdown = True
		if event.type == pg.MOUSEBUTTONDOWN:
			if (0<mouse[0]<32) and (608<mouse[1]<640) and center == False:
				center = True
			else:
				center = False

			if (32<mouse[0]<64) and (608<mouse[1]<640) and center == False:
				launchBrowser(True)
			else:
				launchBrowser(False)

	# print(f'0/{mouse[0]}/64 | 224/{mouse[1]}/288')

	if center == True:
		showCenter(True)
	else:
		showCenter(False)

	screen.blit(browser, (32, 608))

	pg.display.update()

while shutdown:
	screen.fill(i_color)
	text = font.render('Shutting down...', True, 'white')
	screen.blit(text, (64, 64))
	pg.display.flip()
	time.sleep(2)
	shutdown = False

pg.quit()