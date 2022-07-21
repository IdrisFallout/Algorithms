import pygame
from dokusan import generators
import numpy as np

arr = np.array(list(str(generators.random_sudoku(avg_rank=150))))
#print(arr.reshape(9,9))
#print(arr[0])

WIDTH = 550
background_color = (251, 247, 245)
original_grid_element_color = (52, 31, 151)
buffer = 5

#initialise empty 9 by 9 grid
grid = []
grid.append([int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3]), int(arr[4]), int(arr[5]), int(arr[6]), int(arr[7]), int(arr[8])])
grid.append([int(arr[9]), int(arr[10]), int(arr[11]), int(arr[12]), int(arr[13]), int(arr[14]), int(arr[15]), int(arr[16]), int(arr[17])])
grid.append([int(arr[18]), int(arr[19]), int(arr[20]), int(arr[21]), int(arr[22]), int(arr[23]), int(arr[24]), int(arr[25]), int(arr[26])])
grid.append([int(arr[27]), int(arr[28]), int(arr[29]), int(arr[30]), int(arr[31]), int(arr[32]), int(arr[33]), int(arr[34]), int(arr[35])])
grid.append([int(arr[36]), int(arr[37]), int(arr[38]), int(arr[39]), int(arr[40]), int(arr[41]), int(arr[42]), int(arr[43]), int(arr[44])])
grid.append([int(arr[45]), int(arr[46]), int(arr[47]), int(arr[48]), int(arr[49]), int(arr[50]), int(arr[51]), int(arr[52]), int(arr[53])])
grid.append([int(arr[54]), int(arr[55]), int(arr[56]), int(arr[57]), int(arr[58]), int(arr[59]), int(arr[60]), int(arr[61]), int(arr[62])])
grid.append([int(arr[63]), int(arr[64]), int(arr[65]), int(arr[66]), int(arr[67]), int(arr[68]), int(arr[69]), int(arr[70]), int(arr[71])])
grid.append([int(arr[72]), int(arr[73]), int(arr[74]), int(arr[75]), int(arr[76]), int(arr[77]), int(arr[78]), int(arr[79]), int(arr[80])])

grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

def insert(win, position):
	i, j = position[1], position[0]
	myfont = pygame.font.SysFont('Maiandra GD', 35)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			if event.type == pygame.KEYDOWN:
				if (grid_original[i-1][j-1] != 0):
					return
				if (event.key == 48): #48 represents 0 on a keyboard
					grid[i-1][j-1] = event.key - 48
					pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
					pygame.display.update()
				if (0 < event.key - 48 < 10): #check if the input is valid
					pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
					value = myfont.render(str(event.key-48), True, (0,0,0))
					win.blit(value, (position[0]*50 + 15, position[1]*50 +5))
					grid[i-1][j-1] = event.key - 48
					pygame.display.update()
				return


def main():
	pygame.init()
	win = pygame.display.set_mode((WIDTH, WIDTH))
	pygame.display.set_caption("SUDOKU")
	win.fill(background_color)
	myfont = pygame.font.SysFont('Maiandra GD', 35)

	for i in range(0, 10):
		if(i%3 == 0):
			pygame.draw.line(win, (0,0,0), (50 + 50 * i, 50), (50 + 50*i,500), 4)
			pygame.draw.line(win, (0,0,0), (50, 50 + 50 * i), (500,50 + 50 * i), 4)

		pygame.draw.line(win, (0,0,0), (50 + 50 * i, 50), (50 + 50*i,500), 2)
		pygame.draw.line(win, (0,0,0), (50, 50 + 50 * i), (500,50 + 50 * i), 2)
		pygame.display.update()

	for i in range(0, len(grid[0])):
		for j in range(0, len(grid[0])):
			if (0<grid[i][j]<10):
				value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
				win.blit(value, ((j+1)*50+15, (i+1)*50 +5))
	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
				pos = pygame.mouse.get_pos()
				insert(win, (pos[0]//50, pos[1]//50))
			if event.type == pygame.QUIT:
				pygame.quit()
				return

main()