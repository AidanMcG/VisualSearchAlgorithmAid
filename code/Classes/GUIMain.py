from decimal import Decimal
from EightPuzzle import EightPuzzle
from EPSearch import EPSearch
from EPSearch import *
from EPBoard import EPBoard
import pygame,random, sys, time
from pygame.locals import *
from Tree import Tree
from WGBoard import WGBoard
from WGSearch import WGSearch

#colours
RED = (255, 0, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)
BRIGHT_BLUE = (0,50,255)
D_BROWN = (210, 180, 140)
L_BANNER = (200, 180, 135)
DARK_TURQUOISE = (2,54,73)
GREEN = (0,230,0)
GREY = (119, 136, 153)
L_BROWN = (242, 229, 210)
SILVER = (192,192,192)
GOLD = (255, 215, 0)
SAND = (224, 195, 137)
D_BLUE = (70, 130, 180)
D_SILVER = (213, 213, 213)
OFF_WHITE = (1, 57, 94)
STAT_BOX_COLOUR = (186, 174, 227)
YELLOW = (255, 255, 0)
BLUEBOY = (45, 54, 166)
LILAC = (200, 191, 231)
L_BLUE = (95,132,182)

#SETTING COLOURS AND TEXT SIZES
BGCOLOUR = OFF_WHITE
TEXT_COLOUR = WHITE
PRESSED_COLOUR = OFF_WHITE
BORDERCOLOUR = SILVER
BUTTON_COLOUR = WHITE
BUTTON_TEXT_COLOUR = BLACK
MESSAGE_COLOUR = WHITE
BANNER = D_BLUE
MEDIUM_FONT_SIZE = 40
BASIC_FONT_SIZE = 55
LARGE_FONT_SIZE = 100
SMALL_FONT_SIZE = 25
SMALLER_FONT_SIZE = 22
SMALLEST_FONT_SIZE = 17
WINDOW_WIDTH =1280
WINDOW_HEIGHT = 680
FPS = 30

def main():
    pygame.init()
    
    global BASIC_FONT, SMALL_FONT, LARGE_FONT,SMALLER_FONT, MEDIUM_FONT, D_SURF, START_BUTTON, OFF_WHITE, STATE_BOX1, STATE_BOX2, FPS_CLOCK, YELLOW, SMALLEST_FONT, LILAC
    
    FPS_CLOCK = pygame.time.Clock() #amount of ticks per second
    D_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Visual Search Algorithm Learning Aid")
    BASIC_FONT = pygame.font.Font("freesansbold.ttf", BASIC_FONT_SIZE) 
    LARGE_FONT = pygame.font.Font("freesansbold.ttf", LARGE_FONT_SIZE)
    SMALL_FONT = pygame.font.Font("freesansbold.ttf", SMALL_FONT_SIZE)
    SMALLER_FONT = pygame.font.Font("freesansbold.ttf", SMALLER_FONT_SIZE)
    MEDIUM_FONT = pygame.font.Font("freesansbold.ttf", MEDIUM_FONT_SIZE)
    SMALLEST_FONT = pygame.font.Font("freesansbold.ttf", SMALLEST_FONT_SIZE)
    
    ep_menu()
    
def ep_menu(s="", g=""):
    
    EP_SURF, EP_RECT = makeText("The 8-Puzzle", BASIC_FONT_SIZE, TEXT_COLOUR, BGCOLOUR,460 ,25)
    
    S_STATE_SURF, S_STATE_RECT = makeText("Start", SMALL_FONT_SIZE, TEXT_COLOUR, BANNER, 170, 130)
    G_STATE_SURF, G_STATE_RECT = makeText("Goal", SMALL_FONT_SIZE, TEXT_COLOUR, BANNER, 1000, 130)
    
    START_RECT = Rect(445, 325, 360, 140)
    R1_RECT = Rect(100, 170, 200, 57)
    R2_RECT = Rect(937, 170, 200, 57)
    s_input_rect = Rect(100, 250, 250, 29)
    g_input_rect = Rect(937, 250, 250, 29)
    wg_arrow_rect = Rect(1080, 15, 185, 80)
    
    
    S_RANDOM_BUTTON = pygame.image.load("randomise_button.png")
    G_RANDOM_BUTTON = pygame.image.load("randomise_button.png")
    S_RANDOM_BUTTON2 = pygame.image.load("randomise_button2.png")
    S_RANDOM_BUTTON2 = pygame.image.load("randomise_button2.png")
    STATE_BOX1 = pygame.image.load("state_box.png")
    STATE_BOX2 = pygame.image.load("state_box.png")
    START_BUTTON = pygame.image.load("start_button.png")
    ep_arrow = pygame.image.load("ep_arrow.png")
    wg_arrow =pygame.image.load("wg_arrow.png")
        
    start = s
    goal = g
    start_in = ""
    goal_in = ""
    s_active = False
    g_active = False
    random1 = True
    random2 = True
    
    D_SURF.fill(BGCOLOUR)
    pygame.draw.rect(D_SURF, BANNER, (0, 100, WINDOW_WIDTH, 650))
    pygame.draw.rect(D_SURF, WHITE, s_input_rect)
    pygame.draw.rect(D_SURF, WHITE, g_input_rect)
    
    goal_in_surf, goal_in_rect = makeText(goal_in, SMALL_FONT_SIZE, BGCOLOUR, WHITE, 937, 250)
    start_in_surf, start_in_rect = makeText(start_in, SMALL_FONT_SIZE, BGCOLOUR, WHITE, 100, 250)
    err_msg = pygame.image.load("err_msg.png")
    
    if start and goal:
        outputState(start,STATE_BOX1)
        outputState(goal, STATE_BOX2)
        
    while True:
        checkForQuit()
        
        pygame.draw.rect(D_SURF, GOLD, R1_RECT)
        pygame.draw.rect(D_SURF, GOLD, R2_RECT)
        
        pygame.draw.rect(D_SURF, GOLD, START_RECT)
        D_SURF.blit(START_BUTTON, [445, 315])
        D_SURF.blit(S_RANDOM_BUTTON, [100, 170])
        D_SURF.blit(G_RANDOM_BUTTON, [937, 170])
        
        pygame.draw.rect(D_SURF, BORDERCOLOUR, (0, 100, WINDOW_WIDTH, 5))
        D_SURF.blit(EP_SURF, EP_RECT)
        D_SURF.blit(wg_arrow, wg_arrow_rect)
        D_SURF.blit(S_STATE_SURF, S_STATE_RECT)
        D_SURF.blit(G_STATE_SURF, G_STATE_RECT)
        D_SURF.blit(STATE_BOX1, [45, 315])
        D_SURF.blit(STATE_BOX2, [860, 315])
        
        for event in pygame.event.get():
            checkForQuit()
            if event.type == MOUSEBUTTONDOWN:
                #START INPUT
                if s_input_rect.collidepoint(pygame.mouse.get_pos()):
                    s_active = not s_active
                    random1 = False
                else:
                    s_active = False
                    
                #GOAL INPUT
                if g_input_rect.collidepoint(pygame.mouse.get_pos()):
                    g_active = not g_active
                    random2 = False
                else:
                    g_active = False
                    
                if wg_arrow_rect.collidepoint(pygame.mouse.get_pos()):
                    wg_menu()
    
            if event.type == KEYDOWN:
                if s_active:
                    if (event.unicode.isdigit() or event.key == pygame.K_b) and len(start_in) < 9:
                        
                        start_in += event.unicode
                        start_in_surf, start_in_rect = makeText(start_in, SMALL_FONT_SIZE, BGCOLOUR, WHITE, 100, 250)
                    elif event.key == pygame.K_BACKSPACE:
                        
                        start_in = start_in[:-1]
                        start_in_surf, start_in_rect = makeText(start_in, SMALL_FONT_SIZE, BGCOLOUR, WHITE, 100, 250)
                    elif event.key == K_RETURN:
                        
                        if len(start_in) ==9 and is_valid_state(start_in):
                            outputState(start_in, STATE_BOX1)
                        else:
                            D_SURF.blit(err_msg, [0, 636])
                pygame.draw.rect(D_SURF, WHITE, s_input_rect)
                D_SURF.blit(start_in_surf, start_in_rect)
                            
                    #GOAL INPUT        
                if g_active:
                    if (event.unicode.isdigit() or event.key == pygame.K_b) and len(goal_in) < 9:
                        
                        goal_in += event.unicode
                        goal_in_surf, goal_in_rect = makeText(goal_in, SMALL_FONT_SIZE, BGCOLOUR, WHITE, 937, 250)
                    elif event.key == pygame.K_BACKSPACE:
                        
                        goal_in = goal_in[:-1]
                        goal_in_surf, goal_in_rect = makeText(goal_in, SMALL_FONT_SIZE, BGCOLOUR, WHITE, 937, 250)
                    elif event.key == K_RETURN:
                        
                        if len(goal_in) ==9 and is_valid_state(goal_in):
                            outputState(goal_in, STATE_BOX2)
                        else:
                            D_SURF.blit(err_msg, [0, 636])
                pygame.draw.rect(D_SURF, WHITE, g_input_rect)
                D_SURF.blit(goal_in_surf, goal_in_rect)
                
            if START_RECT.collidepoint(pygame.mouse.get_pos()):
                START_BUTTON = pygame.image.load("start_button2.png")
                D_SURF.blit(START_BUTTON, [445, 315])
                pygame.display.flip()
                
                if event.type == MOUSEBUTTONDOWN:
                    START_BUTTON = pygame.image.load("start_button3.png")
                    D_SURF.blit(START_BUTTON, [445, 315])
                    pygame.display.flip()
                    if random1 and random2 and start and goal:
                        ep(start, goal)
                    elif not random1 and not random2:
                        if solvable(start_in, goal_in):
                            ep(start_in, goal_in)
                        else:
                            D_SURF.blit(err_msg, [0, 636])
                    elif random1 and not random2:
                        if solvable(start, goal_in):
                            ep(start, goal_in)
                        else:
                            D_SURF.blit(err_msg, [0, 636])
                    elif not random1 and not random:
                        if solvable(start_in, goal):
                            ep(start_in, goal)
                        else:
                            D_SURF.blit(err_msg, [0, 636])
            else:
                START_BUTTON= pygame.image.load("start_button.png")
                D_SURF.blit(START_BUTTON, [445, 315])
                pygame.display.flip()
                
                #start random button handling
            
            if R1_RECT.collidepoint(pygame.mouse.get_pos()):
                S_RANDOM_BUTTON = pygame.image.load("randomise_button2.png")
                D_SURF.blit(S_RANDOM_BUTTON, [100, 170])
                
                if event.type == MOUSEBUTTONDOWN:
                    random1 = True
                    S_RANDOM_BUTTON = pygame.image.load("randomise_button3.png")
                    start = getRandomState()
                    if goal:
                        while not solvable(start, goal):
                            start = getRandomState()
                    D_SURF.blit(S_RANDOM_BUTTON, [100, 170])
                    outputState(start, STATE_BOX1)
                    
                    pygame.display.flip()
            else:
                S_RANDOM_BUTTON= pygame.image.load("randomise_button.png")
                D_SURF.blit(S_RANDOM_BUTTON, [100, 170])
                pygame.display.flip()
                
                #goal random button handling
            
            if R2_RECT.collidepoint(pygame.mouse.get_pos()):
                G_RANDOM_BUTTON = pygame.image.load("randomise_button2.png")
                D_SURF.blit(G_RANDOM_BUTTON, [937, 170])
                
                if event.type == MOUSEBUTTONDOWN:
                    random2 = True
                    G_RANDOM_BUTTON = pygame.image.load("randomise_button3.png")
                    goal = getRandomState()
                    if start:
                        while not solvable(start, goal):
                            goal = getRandomState()
                    
                    
                    D_SURF.blit(G_RANDOM_BUTTON, [937, 170])
                    outputState(goal, STATE_BOX2)
                    pygame.display.flip()
            else:
                G_RANDOM_BUTTON= pygame.image.load("randomise_button.png")
                D_SURF.blit(G_RANDOM_BUTTON, [937, 170])
                pygame.display.flip()
            
        pygame.display.flip()
        FPS_CLOCK.tick(FPS)
        
def wg_menu(s="", g=""):
    
    
    wg_surf, wg_rect = makeText("The Word Game", BASIC_FONT_SIZE, TEXT_COLOUR, BGCOLOUR,430 ,25)
    ep_arrow = pygame.image.load("ep_arrow.png")
    start_button = pygame.image.load("start_button.png")
    wgmenubox = pygame.image.load("wgmenubox.png")
    
    s_state_surf, s_state_rect = makeText("Starting word", MEDIUM_FONT_SIZE, TEXT_COLOUR, BANNER, 160, 220)
    g_state_surf, g_state_rect = makeText("Finishing word", MEDIUM_FONT_SIZE, TEXT_COLOUR, BANNER, 800, 220)
    
    ep_arrow_rect = Rect(20, 15, 185, 80)
    s_input_rect = Rect(130, 310, 350, 100)
    g_input_rect = Rect(760, 310, 350, 100)
    
    D_SURF.fill(BGCOLOUR)
                          
    start_rect = Rect(445, 500, 360, 140)
    pygame.draw.rect(D_SURF, BANNER, (0, 100, WINDOW_WIDTH, 650))
    pygame.draw.rect(D_SURF, BORDERCOLOUR, (0, 100, WINDOW_WIDTH, 5))
    
    start_in = ""
    goal_in = ""
    s_active = False
    g_active = False
    sinputx = 80
    ginputx = 850
    
    pygame.draw.rect(D_SURF, LILAC, s_input_rect)
    pygame.draw.rect(D_SURF, LILAC, g_input_rect)
    D_SURF.blit(wgmenubox, [110, 300])
    
    while True:
        checkForQuit()
        D_SURF.blit(wgmenubox, [110, 300])
        D_SURF.blit(wg_surf, wg_rect)
        D_SURF.blit(ep_arrow, ep_arrow_rect)
        D_SURF.blit(start_button, start_rect)
        D_SURF.blit(s_state_surf, s_state_rect)
        D_SURF.blit(g_state_surf, g_state_rect)
        
        
        #goal_in_surf, goal_in_rect = makeText(goal_in, SMALL_FONT_SIZE, BGCOLOUR, WHITE, 937, 300)
        #start_in_surf, start_in_rect = makeText(start_in, SMALL_FONT_SIZE, BGCOLOUR, WHITE, 100, 300)
        start_word_final_surf, start_word_final_rect = makeText(start_in, MEDIUM_FONT_SIZE, WHITE, LILAC, 250, 350)
        goal_word_final_surf, goal_word_final_rect = makeText(goal_in, MEDIUM_FONT_SIZE, WHITE, LILAC, 850, 350)
        err_msg_surf, err_msg_rect = makeText("The words must be valid and equal in length", SMALLEST_FONT_SIZE, YELLOW, BANNER, 5, 630)
    
        for event in pygame.event.get():
            checkForQuit()
            if event.type == MOUSEBUTTONDOWN:
                if ep_arrow_rect.collidepoint(pygame.mouse.get_pos()):
                    ep_menu()
                    
                if s_input_rect.collidepoint(pygame.mouse.get_pos()):
                    s_active = True
                    g_active = False
                    
                elif g_input_rect.collidepoint(pygame.mouse.get_pos()):
                    g_active = True
                    s_active = False
                    
                else:
                    s_active = False
                    g_active = False
                    
            if event.type == KEYDOWN:
                if s_active:
                    if event.unicode.isalpha() and len(start_in) < 5:
                        start_in += event.unicode.lower()
                        #start_in_surf, start_in_rect = makeText(start_in, SMALL_FONT_SIZE, BGCOLOUR, WHITE, 100, 300)
                        pygame.draw.rect(D_SURF, LILAC, s_input_rect)
                        #D_SURF.blit(start_in_surf, start_in_rect)
                        
                    elif event.key == pygame.K_BACKSPACE:
                        start_in = start_in[:-1]
                        #start_in_surf, start_in_rect = makeText(start_in, SMALL_FONT_SIZE, BGCOLOUR, WHITE, 100, 300)
                        pygame.draw.rect(D_SURF, LILAC, s_input_rect)
                        #D_SURF.blit(start_in_surf, start_in_rect)
                        
                    elif event.key == pygame.K_RETURN:
                        D_SURF.blit(start_word_final_surf, start_word_final_rect)
                        D_SURF.blit(goal_word_final_surf, goal_word_final_rect)
                        
                elif g_active:
                    if event.unicode.isalpha() and len(goal_in) < 5:
                        goal_in += event.unicode.lower()
                        #goal_in_surf, goal_in_rect = makeText(goal_in, SMALL_FONT_SIZE, BGCOLOUR, WHITE, 937, 300)
                        pygame.draw.rect(D_SURF, LILAC, g_input_rect)
                        #D_SURF.blit(goal_in_surf, goal_in_rect)
                        
                    elif event.key == pygame.K_BACKSPACE:
                        goal_in = goal_in[:-1]
                        #goal_in_surf, goal_in_rect = makeText(goal_in, SMALL_FONT_SIZE, BGCOLOUR, WHITE, 937, 300)
                        pygame.draw.rect(D_SURF, LILAC, g_input_rect)
                        #D_SURF.blit(goal_in_surf, goal_in_rect)
                        
                    elif event.key == pygame.K_RETURN:
                        D_SURF.blit(start_word_final_surf, start_word_final_rect)
                        D_SURF.blit(goal_word_final_surf, goal_word_final_rect)
                        
            if start_rect.collidepoint(pygame.mouse.get_pos()):
                START_BUTTON = pygame.image.load("start_button2.png")
                D_SURF.blit(START_BUTTON, [445, 500])
                
            else:
                START_BUTTON = pygame.image.load("start_button.png")
                D_SURF.blit(START_BUTTON, [445, 500])
               
                        
            if event.type == MOUSEBUTTONDOWN:
                if start_rect.collidepoint(pygame.mouse.get_pos()):
                    wgstart = WGBoard(start_in, 0)
                    if (len(start_in) == len(goal_in)) and start_in in wgstart.d and goal_in in wgstart.d:
                        wg(start_in, goal_in)
                    else:
                        D_SURF.blit(err_msg_surf, err_msg_rect)
                        
            checkForQuit()
            D_SURF.blit(start_word_final_surf, start_word_final_rect)
            D_SURF.blit(goal_word_final_surf, goal_word_final_rect)
            pygame.display.flip()            
            FPS_CLOCK.tick(FPS)

def ep(start, goal, algo = 0):
    eightp_surf, eightp_rect = makeText("The 8-Puzzle", SMALL_FONT_SIZE, TEXT_COLOUR, BGCOLOUR, 990, 15)
    time_taken_surf, time_taken_rect = makeText("Time taken: ", SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 25, 550)
    nodes_expanded_surf, nodes_expanded_rect = makeText("Nodes expanded: ", SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 25, 575)
    depth_node_surf, depth_node_rect = makeText("Depth of node: ", SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 25, 600)
    
    rh_side_rect = Rect( 520, 75, 725, 579)
    rh_side_surf = pygame.Surface((725, 579)) 
    
    B_ARROW = pygame.image.load("back_arrow.png")
    NAV_BAR1 = pygame.image.load("nav_bar1.png")
    NAV_BAR2 = pygame.image.load("nav_bar2.png")
    NAV_BAR4 = pygame.image.load("nav_bar4.png")
    BOARD_MAIN = pygame.image.load("state_box.png")
    solved_button = pygame.image.load("solved_button.png")
    working_button = pygame.image.load("working_button.png")
    stat_box = pygame.image.load("stat_box.png")
    rh_side = pygame.image.load("rh_side.png")
    paused_button = pygame.image.load("paused_button.png")
    bfs_button = pygame.image.load("algo_button_0.png")
    iddfs_button = pygame.image.load("algo_button_1.png")
    astar_button = pygame.image.load("algo_button_2.png")
    
    B_ARROW_BUTTON = Rect(0,3, 138, 47)
    reset_rect = Rect(120, 1, 140, 47)
    solve_rect = Rect(270, 1, 140, 47)

    next_rect = Rect(561, 1, 140, 47)
    bfs_rect = Rect(0, 215, 109, 86)
    iddfs_rect = Rect(0, 320, 109, 86)
    astar_rect = Rect(0, 425, 109, 86)
    
    D_SURF.fill(BGCOLOUR)
    pygame.draw.rect(D_SURF, BANNER, (0, 50, WINDOW_WIDTH, 650))
    pygame.draw.rect(D_SURF, BORDERCOLOUR, (0, 50, WINDOW_WIDTH, 5))
    D_SURF.blit(rh_side, [520, 75])
    
    outputState(start,BOARD_MAIN)
    
    
    solved = False
    search = EPSearch(start, goal)
    maxDepth = 0
    
    time_stat_surf, time_stat_rect = makeText(str(search.timeTaken), SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 165, 550 )
    ne_stat_surf, ne_stat_rect = makeText(str(search.nodesExpanded), SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 220, 575 )
    depth_stat_surf, depth_stat_rect = makeText("0", SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 192, 600 )
    
    startBoard = EPBoard(start,0)
    rootNode = startBoard
    tree = Tree(rootNode, rh_side_rect, D_SURF)
    
    stringboard = strconvert(search.startBoard.state)
    time_taken = 0
    
    while True:
        checkForQuit()
        
        D_SURF.blit(eightp_surf, eightp_rect)
        D_SURF.blit(B_ARROW, B_ARROW_BUTTON)
        D_SURF.blit(B_ARROW, [0,3])
        D_SURF.blit(NAV_BAR1, [120, 1])
        D_SURF.blit(NAV_BAR1,reset_rect)
        D_SURF.blit(NAV_BAR2,solve_rect)
        D_SURF.blit(NAV_BAR4,next_rect)
        D_SURF.blit(BOARD_MAIN, [120, 210])
        D_SURF.blit(stat_box, [9, 530])
        D_SURF.blit(time_taken_surf, time_taken_rect)
        D_SURF.blit(nodes_expanded_surf, nodes_expanded_rect)
        D_SURF.blit(depth_node_surf, depth_node_rect)
        D_SURF.blit(bfs_button, bfs_rect)
        D_SURF.blit(iddfs_button, iddfs_rect)
        D_SURF.blit(astar_button, astar_rect)
        
        if algo == 0:
            bfs_button = pygame.image.load("algo_button_0h.png")
        else:
            bfs_button = pygame.image.load("algo_button_0.png")
        
        if algo == 1:
            iddfs_button = pygame.image.load("algo_button_1h.png")
        else:
            iddfs_button = pygame.image.load("algo_button_1.png")
            
        if algo == 2:
            astar_button = pygame.image.load("algo_button_2h.png")
        else:
            astar_button = pygame.image.load("algo_button_2.png")
        
        
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if B_ARROW_BUTTON.collidepoint(pygame.mouse.get_pos()):
                    ep_menu(start, goal)
                    
                if bfs_rect.collidepoint(pygame.mouse.get_pos()):
                    ep(start, goal)
                    print(search.bfsSolve())
                    first_thing = search.openQueue.first()
                elif iddfs_rect.collidepoint(pygame.mouse.get_pos()):
                    ep(start, goal, 1)
                    
                    print(search.dfsSolve(maxDepth))
                    
                elif astar_rect.collidepoint(pygame.mouse.get_pos()):
                    ep(start, goal, 2)
                    print(search.astarSolve())
                    first_thing = search.openList[0]
                    
                if next_rect.collidepoint(pygame.mouse.get_pos()):
                    start_time = time.time()
                    
                    #bfs
                    if algo == 0:
                        stringboard = strconvert(search.bfsSolve())
                        first_thing = search.openQueue.first()
                        
                    #iddfs
                    elif algo == 1:
                        result = search.dfsSolve(maxDepth)
                        if result != None:
                            stringboard = strconvert(result)
                        if search.openList == []:
                            maxDepth +=1
                            search = EPSearch(start, goal)
                            
                            
                                
                    #astar
                    elif algo == 2: 
                        stringboard = strconvert(search.astarSolve())
                        
                        
                    time_stat_surf, time_stat_rect = makeText(str("{0:.2f}".format(time_taken)), SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 165, 550 )
                    ne_stat_surf, ne_stat_rect = makeText(str(search.nodesExpanded), SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 220, 575 )
                    if algo == 0:
                        depth = getDepth(search.startBoard, search.openQueue.first())
                    else:
                        if not search.openList:
                            depth = 0
                        else:
                            depth = getDepth(search.startBoard, search.openList[0])
                    depth_stat_surf, depth_stat_rect = makeText(str(depth), SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 192, 600 )
                        
                        
                        
                    if search.openList and algo != 0:
                        tree.update(search.openList[0])
                    elif algo == 0:
                        tree.update(search.openQueue.first())
                    else:
                        tree.update(search.openList[0])
                            
                    if stringboard:
                        outputState(stringboard, BOARD_MAIN)
                    D_SURF.blit(stat_box, [9, 530])
                    D_SURF.blit(time_taken_surf, time_taken_rect)
                    D_SURF.blit(nodes_expanded_surf, nodes_expanded_rect)
                    D_SURF.blit(depth_node_surf, depth_node_rect)
                    D_SURF.blit(BOARD_MAIN, [120, 210])
                    D_SURF.blit(time_stat_surf, time_stat_rect)
                    D_SURF.blit(ne_stat_surf, ne_stat_rect)
                    D_SURF.blit(depth_stat_surf, depth_stat_rect)
                    pygame.display.flip()
                        
                    if algo == 0:
                        first_thing = search.openQueue.first()
                    else:
                        if search.openList:
                            first_thing = search.openList[0]
                        
                    #if search.openList[0].state == search.goalBoard.state:
                        #solved = True
                    print (time_taken)
                    
                    time_taken = time_taken + (time.time() - start_time)
                    
                    
                if solve_rect.collidepoint(pygame.mouse.get_pos()):
                    
                    
                    
                    if algo == 0:
                        print(search.bfsSolve())
                        first_thing = search.openQueue.first()
                    
                    
                    while not solved:
                        start_time = time.time()
                        checkForQuit()
                        D_SURF.blit(working_button, [114, 120])
                        
                        if pygame.event.peek(MOUSEBUTTONDOWN) and reset_rect.collidepoint(pygame.mouse.get_pos()): #pauses search
                            break
                        if algo == 0:    
                            stringboard = strconvert(search.bfsSolve())
                        elif algo == 1:
                            result = search.dfsSolve(maxDepth)
                            if result != None:
                                stringboard = strconvert(result)
                            if search.openList == []:
                                maxDepth +=1
                                search = EPSearch(start, goal)
                    
                        elif algo == 2: 
                            stringboard = strconvert(search.astarSolve())
                        
                        
                        time_stat_surf, time_stat_rect = makeText(str("{0:.2f}".format(time_taken)), SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 165, 550 )
                        ne_stat_surf, ne_stat_rect = makeText(str(search.nodesExpanded), SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 220, 575 )
                        if algo == 0:
                            depth = getDepth(search.startBoard, search.openQueue.first())
                        else:
                            if search.openList:
                                depth = getDepth(search.startBoard, search.openList[0])
                            else:
                                depth = 0
                        depth_stat_surf, depth_stat_rect = makeText(str(depth), SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 192, 600 )
                                   
                        if search.openList and algo != 0:
                            tree.update(search.openList[0])
                        elif algo == 0:
                            tree.update(search.openQueue.first())
                        
                        outputState(stringboard, BOARD_MAIN)
                        D_SURF.blit(stat_box, [9, 530])
                        D_SURF.blit(time_taken_surf, time_taken_rect)
                        D_SURF.blit(nodes_expanded_surf, nodes_expanded_rect)
                        D_SURF.blit(depth_node_surf, depth_node_rect)
                        D_SURF.blit(BOARD_MAIN, [120, 210])
                        D_SURF.blit(time_stat_surf, time_stat_rect)
                        D_SURF.blit(ne_stat_surf, ne_stat_rect)
                        D_SURF.blit(depth_stat_surf, depth_stat_rect)
                        pygame.display.flip()
                        
                        if algo == 0:
                            first_thing = search.openQueue.first()
                        else:
                            if search.openList:
                                first_thing = search.openList[0]
                            else:
                                first_thing = search.startBoard
                            
                                
                        
                        if first_thing.state == search.goalBoard.state:
                            solved = True
                        
                        
                        time_taken = time_taken + (time.time() - start_time)
                    
        if time_taken != 0:
            
            D_SURF.blit(paused_button,[114, 120])
            D_SURF.blit(time_stat_surf, time_stat_rect)
            D_SURF.blit(ne_stat_surf, ne_stat_rect)
            D_SURF.blit(depth_stat_surf, depth_stat_rect)
            
            
        if solved:
            D_SURF.blit(solved_button, [114, 120])
            D_SURF.blit(time_stat_surf, time_stat_rect)
            D_SURF.blit(ne_stat_surf, ne_stat_rect)
            D_SURF.blit(depth_stat_surf, depth_stat_rect)
            
            
        pygame.display.flip()

        
def wg(start,goal, algo=0):
    
    wordg_surf, wordg_rect = makeText("The Word Game", SMALL_FONT_SIZE, TEXT_COLOUR, BGCOLOUR, 990, 15)
    time_taken_surf, time_taken_rect = makeText("Time taken: ", SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 25, 550)
    nodes_expanded_surf, nodes_expanded_rect = makeText("Nodes expanded: ", SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 25, 575)
    depth_node_surf, depth_node_rect = makeText("Depth of node: ", SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 25, 600)
    
    rh_side_rect = Rect( 520, 75, 725, 579)
    rh_side_surf = pygame.Surface((725, 579)) 
    
    B_ARROW = pygame.image.load("back_arrow.png")
    NAV_BAR1 = pygame.image.load("nav_bar1.png")
    NAV_BAR2 = pygame.image.load("nav_bar2.png")
    NAV_BAR4 = pygame.image.load("nav_bar4.png")
    solved_button = pygame.image.load("solved_button.png")
    working_button = pygame.image.load("working_button.png")
    stat_box = pygame.image.load("stat_box.png")
    rh_side = pygame.image.load("rh_side2.png")
    paused_button = pygame.image.load("paused_button.png")
    bfs_button = pygame.image.load("algo_button_0.png")
    iddfs_button = pygame.image.load("algo_button_1.png")
    astar_button = pygame.image.load("algo_button_2.png")
    wg_box = pygame.image.load("WGBox.png")
    
    B_ARROW_BUTTON = Rect(0,3, 138, 47)
    reset_rect = Rect(120, 1, 140, 47)
    solve_rect = Rect(270, 1, 140, 47)
    back_rect = Rect(419, 1, 140, 47)
    next_rect = Rect(561, 1, 140, 47)
    bfs_rect = Rect(0, 215, 109, 86)
    iddfs_rect = Rect(0, 320, 109, 86)
    astar_rect = Rect(0, 425, 109, 86)
    
    D_SURF.fill(BGCOLOUR)
    pygame.draw.rect(D_SURF, BANNER, (0, 50, WINDOW_WIDTH, 650))
    pygame.draw.rect(D_SURF, BORDERCOLOUR, (0, 50, WINDOW_WIDTH, 5))
    D_SURF.blit(rh_side, [520, 75])
    

    solved = False
    
    time_taken = 0
    
    search = WGSearch(start, goal)
    D_SURF.fill(BGCOLOUR)
    pygame.draw.rect(D_SURF, BANNER, (0, 50, WINDOW_WIDTH, 650))
    D_SURF.blit(wg_box, [123, 293])
    current_word_surf, current_word_rect = makeText(str(search.startState), LARGE_FONT_SIZE, TEXT_COLOUR, BLUEBOY, 150, 302 )
    D_SURF.blit(current_word_surf, current_word_rect)
    maxDepth = 0
    
    while True:
        
        checkForQuit()
        
        pygame.draw.rect(D_SURF, BORDERCOLOUR, (0, 50, WINDOW_WIDTH, 5))
        D_SURF.blit(rh_side, [520, 75])
        D_SURF.blit(wordg_surf, wordg_rect)
        
        D_SURF.blit(B_ARROW, B_ARROW_BUTTON)
        D_SURF.blit(B_ARROW, [0,3])
        D_SURF.blit(NAV_BAR1, [120, 1])
        D_SURF.blit(NAV_BAR1,reset_rect)
        D_SURF.blit(NAV_BAR2,solve_rect)
        D_SURF.blit(NAV_BAR4,next_rect)
        D_SURF.blit(stat_box, [9, 530])
        D_SURF.blit(time_taken_surf, time_taken_rect)
        D_SURF.blit(nodes_expanded_surf, nodes_expanded_rect)
        D_SURF.blit(depth_node_surf, depth_node_rect)
        D_SURF.blit(bfs_button, bfs_rect)
        D_SURF.blit(iddfs_button, iddfs_rect)
        D_SURF.blit(astar_button, astar_rect)
        
        if algo == 0:
            bfs_button = pygame.image.load("algo_button_0h.png")
        else:
            bfs_button = pygame.image.load("algo_button_0.png")
        
        if algo == 1:
            iddfs_button = pygame.image.load("algo_button_1h.png")
        else:
            iddfs_button = pygame.image.load("algo_button_1.png")
            
        if algo == 2:
            astar_button = pygame.image.load("algo_button_2h.png")
        else:
            astar_button = pygame.image.load("algo_button_2.png")
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                checkForQuit()
                if B_ARROW_BUTTON.collidepoint(pygame.mouse.get_pos()):
                    
                    wordpath = []
                    wg_menu()
                
                if bfs_rect.collidepoint(pygame.mouse.get_pos()):
                    wg(start, goal)
                    
                elif iddfs_rect.collidepoint(pygame.mouse.get_pos()):
                    wg(start, goal, 1)
                    
                elif astar_rect.collidepoint(pygame.mouse.get_pos()):
                    wg(start, goal, 2)
                    
                
                elif next_rect.collidepoint(pygame.mouse.get_pos()):
                    
                    if algo == 0:
                        stringboard = search.bfsSolve()
                        print (stringboard)
                        first_thing = search.openQueue.first()
                        
                    #iddfs
                    elif algo == 1:
                        result = search.dfsSolve(maxDepth)
                        if result != None:
                            stringboard = "".join(result)
                        if search.openList == []:
                            maxDepth +=1
                            search = EPSearch(start, goal)
                                
                    #astar
                    elif algo == 2: 
                        stringboard = "".join(search.astarSolve())
                    
                    if not solved:
                        
                        start_time = time.time()
                        
                        checkForQuit()
                        D_SURF.blit(working_button, [114, 120])
                        
                        if pygame.event.peek(MOUSEBUTTONDOWN) and reset_rect.collidepoint(pygame.mouse.get_pos()): #pauses search
                            break
                        if algo == 0:    
                            stringboard = "".join(search.bfsSolve())
                        elif algo == 1:
                            result = search.dfsSolve(maxDepth)
                            if result != None:
                                stringboard = "".join(result)
                            if search.openList == []:
                                maxDepth +=1
                                search = WGSearch(start, goal)
                        elif algo == 2: 
                            stringboard = "".join(search.astarSolve())
                            
                        current_word_surf, current_word_rect = makeText(stringboard, LARGE_FONT_SIZE, TEXT_COLOUR, BLUEBOY, 150, 302 )
                        
                        print (stringboard)
                        time_stat_surf, time_stat_rect = makeText(str("{0:.2f}".format(time_taken)), SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 165, 550 )
                        ne_stat_surf, ne_stat_rect = makeText(str(search.nodesExpanded), SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 220, 575 )
                        if algo == 0:
                            depth = getDepth(search.startBoard, search.openQueue.first())
                        else:
                            if search.openList:
                                depth = getDepth(search.startBoard, search.openList[0])
                            else:
                                depth = 0
                            
                        depth_stat_surf, depth_stat_rect = makeText(str(depth), SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 192, 600 )
                                   
                        D_SURF.blit(wg_box, [123, 293])
                        D_SURF.blit(current_word_surf,current_word_rect)
                        D_SURF.blit(rh_side, [520, 75])
                        D_SURF.blit(stat_box, [9, 530])
                        D_SURF.blit(time_taken_surf, time_taken_rect)
                        D_SURF.blit(nodes_expanded_surf, nodes_expanded_rect)
                        D_SURF.blit(depth_node_surf, depth_node_rect)
                        D_SURF.blit(time_stat_surf, time_stat_rect)
                        D_SURF.blit(ne_stat_surf, ne_stat_rect)
                        D_SURF.blit(depth_stat_surf, depth_stat_rect)
                        pygame.display.flip()
                        
                        if algo == 0:
                            first_thing = search.openQueue.first()
                        else:
                            first_thing = search.openList[0]
                        
                        if first_thing.state == search.goalBoard.state:
                            solved = True
                            wordpath = path(search.startBoard, first_thing)
                            print (search.timeTaken)
                            print ("path is ", wordpath)
                    
                        time_taken = time_taken + (time.time() - start_time)
                
                #solve
                elif solve_rect.collidepoint(pygame.mouse.get_pos()):
                    if algo == 0:
                        print(search.bfsSolve())
                        first_thing = search.openQueue.first()
                    elif algo == 1:
                        print (search.dfsSolve(maxDepth))
                        first_thing = search.openList[0]
                    elif algo == 2:
                        print (search.astarSolve())
                        first_thing = search.openList[0]
                    
                    
                    while not solved:
                        
                        checkForQuit()
                        start_time = time.time()
                        D_SURF.blit(working_button, [114, 120])
                        
                        if pygame.event.peek(MOUSEBUTTONDOWN) and reset_rect.collidepoint(pygame.mouse.get_pos()): #pauses search
                            break
                        if algo == 0:    
                            stringboard = "".join(search.bfsSolve())
                        elif algo == 1:
                            result = search.dfsSolve(maxDepth)
                            if search.openList:
                                stringboard = "".join(result)
                            else:
                                maxDepth+=1
                                search = WGSearch(start, goal)
                        elif algo == 2: 
                            stringboard = "".join(search.astarSolve())
                            
                        current_word_surf, current_word_rect = makeText(stringboard, LARGE_FONT_SIZE, TEXT_COLOUR, BLUEBOY, 150, 306 )
                        
                        print (stringboard)
                        time_stat_surf, time_stat_rect = makeText(str("{0:.2f}".format(time_taken)), SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 165, 550 )
                        ne_stat_surf, ne_stat_rect = makeText(str(search.nodesExpanded), SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 220, 575 )
                        if algo == 0:
                            depth = getDepth(search.startBoard, search.openQueue.first())
                        else:
                            if search.openList:
                                depth = getDepth(search.startBoard, search.openList[0])
                            else:
                                depth = 0
                            
                        depth_stat_surf, depth_stat_rect = makeText(str(depth), SMALLER_FONT_SIZE, TEXT_COLOUR, STAT_BOX_COLOUR, 192, 600 )
                                   
                        D_SURF.blit(wg_box, [123, 293])
                        D_SURF.blit(current_word_surf,current_word_rect)
                        D_SURF.blit(rh_side, [520, 75])
                        D_SURF.blit(stat_box, [9, 530])
                        D_SURF.blit(time_taken_surf, time_taken_rect)
                        D_SURF.blit(nodes_expanded_surf, nodes_expanded_rect)
                        D_SURF.blit(depth_node_surf, depth_node_rect)
                        D_SURF.blit(time_stat_surf, time_stat_rect)
                        D_SURF.blit(ne_stat_surf, ne_stat_rect)
                        D_SURF.blit(depth_stat_surf, depth_stat_rect)
                        pygame.display.flip()
                        
                        if algo == 0:
                            first_thing = search.openQueue.first()
                        else:
                            if search.openList:
                                first_thing = search.openList[0]
                            else:
                                first_thing = search.startBoard
                        
                        if first_thing.state == search.goalBoard.state:
                            solved = True
                            wordpath = path(search.startBoard, first_thing, [])
                            print (search.timeTaken)
                            print ("path is ", wordpath)
                        time_taken = time_taken + (time.time() - start_time)

        if search.timeTaken:
            
            D_SURF.blit(wg_box, [123, 293])
            D_SURF.blit(current_word_surf,current_word_rect)
            D_SURF.blit(paused_button,[114, 120])
            D_SURF.blit(time_stat_surf, time_stat_rect)
            D_SURF.blit(ne_stat_surf, ne_stat_rect)
            D_SURF.blit(depth_stat_surf, depth_stat_rect)
            
        if solved:
            D_SURF.blit(solved_button, [114, 120])
            D_SURF.blit(wg_box, [123,293])
            D_SURF.blit(current_word_surf,current_word_rect)
            D_SURF.blit(time_stat_surf, time_stat_rect)
            D_SURF.blit(ne_stat_surf, ne_stat_rect)
            D_SURF.blit(depth_stat_surf, depth_stat_rect)
    
            outputPath(wordpath)
    
        pygame.display.flip()
        FPS_CLOCK.tick(FPS)

def makeText(text, size, color, BGCOLOUR, top, left):
    #create the Surface and Rect objects for some text
    if size == BASIC_FONT_SIZE:
        textSurf = BASIC_FONT.render(text, True, color, BGCOLOUR)
    elif size == LARGE_FONT_SIZE:
        textSurf = LARGE_FONT.render(text, True, color, BGCOLOUR)
    elif size == SMALL_FONT_SIZE:
        textSurf = SMALL_FONT.render(text, True, color,BGCOLOUR)
    elif size == SMALLER_FONT_SIZE:
        textSurf = SMALLER_FONT.render(text, True, color, BGCOLOUR)
    elif size == MEDIUM_FONT_SIZE:
        textSurf = MEDIUM_FONT.render(text, True, color, BGCOLOUR)
    elif size == SMALLEST_FONT_SIZE:
        textSurf = SMALLEST_FONT.render(text, True, color, BGCOLOUR)
    
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)   

def checkForQuit():
    for event in pygame.event.get(QUIT): #get all the quit events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the keyup events
        if event.key == K_ESCAPE:
            terminate() # terminate if esc key pressed
        pygame.event.post(event) # put the other keyup event objects back


def outputState(state, box):
    x, y = 45, 25
    blank = pygame.image.load("blank.png")
    
    num1_surf, num1_rect = makeText(state[0], BASIC_FONT_SIZE, OFF_WHITE, BORDERCOLOUR, x, y)
    num2_surf, num2_rect = makeText(state[1], BASIC_FONT_SIZE, OFF_WHITE, BORDERCOLOUR, x+120, y)
    num3_surf, num3_rect = makeText(state[2], BASIC_FONT_SIZE, OFF_WHITE, BORDERCOLOUR, x+240, y)
    
    num4_surf, num4_rect = makeText(state[3], BASIC_FONT_SIZE, OFF_WHITE, BORDERCOLOUR, x, y+103)
    num5_surf, num5_rect = makeText(state[4], BASIC_FONT_SIZE, OFF_WHITE, BORDERCOLOUR, x+120, y+103)
    num6_surf, num6_rect = makeText(state[5], BASIC_FONT_SIZE, OFF_WHITE, BORDERCOLOUR, x+240, y+103)
    
    num7_surf, num7_rect = makeText(state[6], BASIC_FONT_SIZE, OFF_WHITE, BORDERCOLOUR, x, y+103+103)
    num8_surf, num8_rect = makeText(state[7], BASIC_FONT_SIZE, OFF_WHITE, BORDERCOLOUR, x+120, y+103+103)
    num9_surf, num9_rect = makeText(state[8], BASIC_FONT_SIZE, OFF_WHITE, BORDERCOLOUR, x+240, y+103+103)
    
    box.blit(num1_surf, num1_rect)
    box.blit(num2_surf, num2_rect)
    box.blit(num3_surf, num3_rect)
    box.blit(num4_surf, num4_rect)
    box.blit(num5_surf, num5_rect)
    box.blit(num6_surf, num6_rect)
    box.blit(num7_surf, num7_rect)
    box.blit(num8_surf, num8_rect)
    box.blit(num9_surf, num9_rect)
    
    for x in range(len(state)):
        if state[x] == "b" and x == 0:
            box.blit(blank, num1_rect)
        elif state[x] == "b" and x == 1:
            box.blit(blank, num2_rect)
        elif state[x] == "b" and x == 2:
            box.blit(blank, num3_rect)
        elif state[x] == "b" and x == 3:
            box.blit(blank, num4_rect)
        elif state[x] == "b" and x == 4:
            box.blit(blank, num5_rect)
        elif state[x] == "b" and x == 5:
            box.blit(blank, num6_rect)
        elif state[x] == "b" and x == 6:
            box.blit(blank, num7_rect)
        elif state[x] == "b" and x == 7:
            box.blit(blank, num8_rect)
        elif state[x] == "b" and x == 8:
            box.blit(blank, num9_rect)
    
def strconvert(ll):
    s = ""
    for x in range(3):
        for y in range(3):
            s += ll[x][y]
    return s
   
def getRandomState():
    options = ["1", "2", "3", "4", "5", "6", "7", "8", "b"]
    state = ""
    while len(state) < 9:
        c = random.choice(options)
        if c not in state:
            state += c
    return (state)
    
def solvable(start, goal):
    if len(start) != 9 or len(goal) != 9:
        return False
    
    s_inv = getInv(start)
    g_inv = getInv(goal)
    if s_inv %2==0 and g_inv%2==0:
        return True
    elif s_inv%2==1 and g_inv%2==1:
        return True
    else:
        return False
    
def getInv(state):
    inv = 0
    j =-1
    for c in state:
        j+=1
        for c2 in range(j, 9):
            if c != "b" and state[c2] != "b":
                if int(c) > int(state[c2]):
                    
                    inv += 1
    return inv

def is_valid_state(s):
    options = ["1", "2", "3", "4", "5", "6", "7", "8", "b"]
    st = "".join(set(s))
    if len(st) == 9:
        for x in st:
            if x in options:
                return True
    
def getDepth(sboard, cboard, depth =0):
    if sboard == None :
        
        return "No"
    if cboard.state == sboard.state:
        return depth
    return getDepth(sboard, cboard.parent, depth+1)
    
def path(sboard, cboard, p = []):
    while cboard.state != sboard.state:
        print(cboard.state)
        p.append("".join(cboard.state))
        cboard = cboard.parent
    p.append("".join(sboard.state))
    print (p)
    return p
    
def outputPath(path):
    y=0
    z=0
    p = path[::-1]
    
    for x in p:
        out_surf, out_rect = makeText(str(x), BASIC_FONT_SIZE, TEXT_COLOUR, L_BLUE, 580+z, 140+y)
        y+=50
        if y >= 500:
            y = 0
            z += 200
        D_SURF.blit(out_surf, out_rect)
        
def terminate():
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    