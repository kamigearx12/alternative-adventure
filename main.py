import pygame

gamework = True

skin = 0

lvl=1

timegm = pygame.time.Clock()
#висота-довжина
wght = 800
hght = 400
#БГ
bg = pygame.image.load('res/bg.png')
bg2 = pygame.image.load('res/bg2.png')
hmins = pygame.image.load('res/homeinside.png')
hminsa = pygame.image.load('res/homeinsidea.png')
#анімації

walkdown = [
    pygame.image.load('res/pl.png'),
    pygame.image.load('res/pl1.png'),
    pygame.image.load('res/pl.png'),
    pygame.image.load('res/pl2.png')
]



walkup = [
    pygame.image.load('res/up.png'),
    pygame.image.load('res/up1.png'),
    pygame.image.load('res/up.png'),
    pygame.image.load('res/up2.png')
]



walkr = [
    pygame.image.load('res/r.png'),
    pygame.image.load('res/r1.png'),
    pygame.image.load('res/r.png'),
    pygame.image.load('res/r2.png')
]



walkl = [
    pygame.image.load('res/l.png'),
    pygame.image.load('res/l1.png'),
    pygame.image.load('res/l.png'),
    pygame.image.load('res/l2.png')
]

kkts = [
    pygame.image.load('res/kkts.png'),
    pygame.image.load('res/kkts1.png'),
    pygame.image.load('res/kkts2.png'),
    pygame.image.load('res/kkts1.png'),
    pygame.image.load('res/kkts.png')
]
kktsa = [
    pygame.image.load('res/kktsa.png'),
    pygame.image.load('res/kktsa1.png'),
    pygame.image.load('res/kktsa2.png'),
    pygame.image.load('res/kktsa1.png'),
    pygame.image.load('res/kktsa.png')
]
kkts_anim_cnt = 0

idle = pygame.image.load('res/pl.png')

gorob = pygame.image.load('res/gorob.png')

#екран
pygame.init()
wind = pygame.display.set_mode((wght, hght))
pygame.display.set_caption('shoska')
icon = pygame.image.load('res/ico.png')
pygame.display.set_icon(icon)
#об'єкти
home = pygame.image.load('res/home.png')
home2 = pygame.image.load('res/home2.png')
kktsdialogfnt = pygame.font.Font('res/DeliciousHandrawn-Regular.ttf', 24)
kktsdialog = kktsdialogfnt.render('Hi Catavis! How are you today?', False, 'white')
kktsdialog2 = kktsdialogfnt.render('oh... you cant talk...', False, 'white')
homeinf = kktsdialogfnt.render('this is not your home', False, 'red')
kktsadialog = kktsdialogfnt.render('This is real bad place', False, 'white')
btn = pygame.image.load('res/button.png')
#настройки гравця
pl_anim_cnt = 0
plspeed = 5
player_x=335
player_y=175
#цикл
while gamework:
    key = pygame.key.get_pressed()
    if key[pygame.K_t] and lvl == 1:
        lvl = 2
    elif key[pygame.K_t] and lvl == 2:
        lvl = 1
    elif key[pygame.K_t] and lvl == 3:
        lvl = 4
    elif key[pygame.K_t] and lvl == 4:
        lvl = 3

    if lvl == 1:
        wind.blit(bg, (0,0))
        key = pygame.key.get_pressed()

        if key[pygame.K_g] and skin == 0:
            skin = 999
        elif key[pygame.K_g] and skin == 999:
            skin = 0
        
        if skin == 999:
            if key[pygame.K_DOWN]:
                wind.blit(gorob, (player_x,player_y))
            elif key[pygame.K_UP]:
                wind.blit(gorob, (player_x,player_y))
            elif key[pygame.K_RIGHT]:
                wind.blit(gorob, (player_x,player_y))
            elif key[pygame.K_LEFT]:
                wind.blit(gorob, (player_x,player_y))
            else:
                wind.blit(gorob, (player_x,player_y))
        elif skin == 0:
            if key[pygame.K_DOWN]:
                wind.blit(walkdown[pl_anim_cnt], (player_x,player_y))
            elif key[pygame.K_UP]:
                wind.blit(walkup[pl_anim_cnt], (player_x,player_y))
            elif key[pygame.K_RIGHT]:
                wind.blit(walkr[pl_anim_cnt], (player_x,player_y))
            elif key[pygame.K_LEFT]:
                wind.blit(walkl[pl_anim_cnt], (player_x,player_y))
            else:
                wind.blit(idle, (player_x,player_y))
        


        #розміщення об'єктів
        btnx = player_x + 35
        btny = player_y + 20
        wind.blit(btn, (btnx, btny))
        wind.blit(kkts[kkts_anim_cnt], (535,220))
        wind.blit(home, (315,50))
        

        if pl_anim_cnt == 3:
            pl_anim_cnt = 0
        else:
            pl_anim_cnt += 1
        if kkts_anim_cnt == 4:
            kkts_anim_cnt = 0
        else:
            kkts_anim_cnt += 1
        #керування гравця
        if key[pygame.K_DOWN] and player_y <= hght:
            player_y += plspeed
        elif key[pygame.K_UP] and player_y >= 0:
            player_y -= plspeed
        elif key[pygame.K_RIGHT] and player_x <= wght:
            player_x += plspeed
        elif key[pygame.K_LEFT] and player_x >= 0:
            player_x -= plspeed

        

        #колізія
        if player_x >= 485 and player_x <= 495 and player_y >= 235 and player_y <= 260:
            player_x -= 10
        if player_x >= 495 and player_x <= 795 and player_y >= 225 and player_y <= 235:
            player_y -= 10
        if player_x >= 510 and player_x <= 790 and player_y >= 250 and player_y <= 260:
            player_y += 10
        if player_x >= 420 and player_x <= 430 and player_y >= 230 and player_y <= 255:
            player_x += 10
        if player_x >= -5 and player_x <= 415 and player_y >= 225 and player_y <= 240:
            player_y -= 10
        if player_x >= -5 and player_x <= 415 and player_y >= 250 and player_y <= 265:
            player_y += 10
        if player_x >= 285 and player_x <= 395 and player_y >= 125 and player_y <= 150:
            wind.blit(homeinf, (315,50))
            player_y += 10
        if player_x >= 290 and player_x <= 390 and player_y >= 90 and player_y <= 105:
            player_y -= 10
    
        if player_x >= 495 and player_x <= 575 and player_y >= 180 and player_y <= 220:
            wind.blit(kktsdialog, (525,205))
            wind.blit(kktsdialog2, (525,220))
       
    #альтернатіва (2 левл)
    if lvl == 2:
        wind.blit(bg2, (0,0))
        key = pygame.key.get_pressed()

        if key[pygame.K_g] and skin == 0:
            skin = 999
        elif key[pygame.K_g] and skin == 999:
            skin = 0
        
        if skin == 999:
            if key[pygame.K_DOWN]:
                wind.blit(gorob, (player_x,player_y))
            elif key[pygame.K_UP]:
                wind.blit(gorob, (player_x,player_y))
            elif key[pygame.K_RIGHT]:
                wind.blit(gorob, (player_x,player_y))
            elif key[pygame.K_LEFT]:
                wind.blit(gorob, (player_x,player_y))
            else:
                wind.blit(gorob, (player_x,player_y))
        elif skin == 0:
            if key[pygame.K_DOWN]:
                wind.blit(walkdown[pl_anim_cnt], (player_x,player_y))
            elif key[pygame.K_UP]:
                wind.blit(walkup[pl_anim_cnt], (player_x,player_y))
            elif key[pygame.K_RIGHT]:
                wind.blit(walkr[pl_anim_cnt], (player_x,player_y))
            elif key[pygame.K_LEFT]:
                wind.blit(walkl[pl_anim_cnt], (player_x,player_y))
            else:
                wind.blit(idle, (player_x,player_y))
        
        #розміщення об'єктів
        btnx = player_x + 35
        btny = player_y + 20
        wind.blit(btn, (btnx, btny))

        wind.blit(kktsa[kkts_anim_cnt], (535,220))
        wind.blit(home2, (315,50))
        

        if pl_anim_cnt == 3:
            pl_anim_cnt = 0
        else:
            pl_anim_cnt += 1
        if kkts_anim_cnt == 4:
            kkts_anim_cnt = 0
        else:
            kkts_anim_cnt += 1
        #керування гравця
        if key[pygame.K_DOWN] and player_y <= hght:
            player_y += plspeed
        elif key[pygame.K_UP] and player_y >= 0:
            player_y -= plspeed
        elif key[pygame.K_RIGHT] and player_x <= wght:
            player_x += plspeed
        elif key[pygame.K_LEFT] and player_x >= 0:
            player_x -= plspeed

        

        #колізія
        if player_x >= 485 and player_x <= 495 and player_y >= 235 and player_y <= 260:
            player_x -= 10
        if player_x >= 495 and player_x <= 795 and player_y >= 225 and player_y <= 235:
            player_y -= 10
        if player_x >= 510 and player_x <= 790 and player_y >= 250 and player_y <= 260:
            player_y += 10
        if player_x >= 420 and player_x <= 430 and player_y >= 230 and player_y <= 255:
            player_x += 10
        if player_x >= -5 and player_x <= 415 and player_y >= 225 and player_y <= 240:
            player_y -= 10
        if player_x >= -5 and player_x <= 415 and player_y >= 250 and player_y <= 265:
            player_y += 10
        if player_x >= 285 and player_x <= 395 and player_y >= 125 and player_y <= 150:
            player_x = 215
            player_y = 335
            lvl = 3
        if player_x >= 290 and player_x <= 390 and player_y >= 90 and player_y <= 105:
            player_y -= 10
        
        if player_x >= 495 and player_x <= 575 and player_y >= 180 and player_y <= 220:
            wind.blit(kktsadialog, (525,205))
    #3a
    if lvl == 3:
        wind.blit(hminsa, (0,0))
        key = pygame.key.get_pressed()
        
        if key[pygame.K_g] and skin == 0:
            skin = 999
        elif key[pygame.K_g] and skin == 999:
            skin = 0
        
        if skin == 999:
            if key[pygame.K_DOWN]:
                wind.blit(gorob, (player_x,player_y))
            elif key[pygame.K_UP]:
                wind.blit(gorob, (player_x,player_y))
            elif key[pygame.K_RIGHT]:
                wind.blit(gorob, (player_x,player_y))
            elif key[pygame.K_LEFT]:
                wind.blit(gorob, (player_x,player_y))
            else:
                wind.blit(gorob, (player_x,player_y))
        elif skin == 0:
            if key[pygame.K_DOWN]:
                wind.blit(walkdown[pl_anim_cnt], (player_x,player_y))
            elif key[pygame.K_UP]:
                wind.blit(walkup[pl_anim_cnt], (player_x,player_y))
            elif key[pygame.K_RIGHT]:
                wind.blit(walkr[pl_anim_cnt], (player_x,player_y))
            elif key[pygame.K_LEFT]:
                wind.blit(walkl[pl_anim_cnt], (player_x,player_y))
            else:
                wind.blit(idle, (player_x,player_y))
        
        #розміщення об'єктів
        btnx = player_x + 35
        btny = player_y + 20
        wind.blit(btn, (btnx, btny))

        if pl_anim_cnt == 3:
            pl_anim_cnt = 0
        else:
            pl_anim_cnt += 1
        #керування гравця
        if key[pygame.K_DOWN] and player_y <= hght:
            player_y += plspeed
        elif key[pygame.K_UP] and player_y >= 0:
            player_y -= plspeed
        elif key[pygame.K_RIGHT] and player_x <= wght:
            player_x += plspeed
        elif key[pygame.K_LEFT] and player_x >= 0:
            player_x -= plspeed

        #колізія
        if player_x >= 170 and player_x <= 305 and player_y >= 380 and player_y <= 395:
            player_x = 340
            player_y = 155
            lvl = 2
        elif player_x >= 5 and player_x <= 25 and player_y >= -5 and player_y <= 405:
            player_x += 10
        elif player_x >= 195 and player_x <= 205 and player_y >= -5 and player_y <= 25:
            player_x -= 10
        elif player_x >= 300 and player_x <= 306 and player_y >= -5 and player_y <= 25:
            player_x += 10
        elif player_x >= 225 and player_x <= 295 and player_y >= -5 and player_y <= 35:
            player_y += 10
        elif player_x >= 560 and player_x <= 566 and player_y >= 100 and player_y <= 205:
            player_x -= 10
        elif player_x >= 585 and player_x <= 735 and player_y >= 100 and player_y <= 115:
            player_y -= 10
        elif player_x >= 740 and player_x <= 745 and player_y >= 100 and player_y <= 205:
            player_x += 10
        elif player_x >= 565 and player_x <= 730 and player_y >= 205 and player_y <= 211:
            player_y += 10
    #3
    if lvl == 4:
        wind.blit(hmins, (0,0))
        key = pygame.key.get_pressed()
        
        if key[pygame.K_g] and skin == 0:
            skin = 999
        elif key[pygame.K_g] and skin == 999:
            skin = 0
        
        if skin == 999:
            if key[pygame.K_DOWN]:
                wind.blit(gorob, (player_x,player_y))
            elif key[pygame.K_UP]:
                wind.blit(gorob, (player_x,player_y))
            elif key[pygame.K_RIGHT]:
                wind.blit(gorob, (player_x,player_y))
            elif key[pygame.K_LEFT]:
                wind.blit(gorob, (player_x,player_y))
            else:
                wind.blit(gorob, (player_x,player_y))
        elif skin == 0:
            if key[pygame.K_DOWN]:
                wind.blit(walkdown[pl_anim_cnt], (player_x,player_y))
            elif key[pygame.K_UP]:
                wind.blit(walkup[pl_anim_cnt], (player_x,player_y))
            elif key[pygame.K_RIGHT]:
                wind.blit(walkr[pl_anim_cnt], (player_x,player_y))
            elif key[pygame.K_LEFT]:
                wind.blit(walkl[pl_anim_cnt], (player_x,player_y))
            else:
                wind.blit(idle, (player_x,player_y))
        
        #розміщення об'єктів
        btnx = player_x + 35
        btny = player_y + 20
        wind.blit(btn, (btnx, btny))

        if pl_anim_cnt == 3:
            pl_anim_cnt = 0
        else:
            pl_anim_cnt += 1
        #керування гравця
        if key[pygame.K_DOWN] and player_y <= hght:
            player_y += plspeed
        elif key[pygame.K_UP] and player_y >= 0:
            player_y -= plspeed
        elif key[pygame.K_RIGHT] and player_x <= wght:
            player_x += plspeed
        elif key[pygame.K_LEFT] and player_x >= 0:
            player_x -= plspeed

        #колізія
        if player_x >= 170 and player_x <= 305 and player_y >= 380 and player_y <= 395:
            player_x = 340
            player_y = 155
            lvl = 1
        elif player_x >= 5 and player_x <= 25 and player_y >= -5 and player_y <= 405:
            player_x += 10
        elif player_x >= 195 and player_x <= 205 and player_y >= -5 and player_y <= 25:
            player_x -= 10
        elif player_x >= 300 and player_x <= 306 and player_y >= -5 and player_y <= 25:
            player_x += 10
        elif player_x >= 560 and player_x <= 566 and player_y >= 100 and player_y <= 205:
            player_x -= 10
        elif player_x >= 585 and player_x <= 735 and player_y >= 100 and player_y <= 115:
            player_y -= 10
        elif player_x >= 740 and player_x <= 745 and player_y >= 100 and player_y <= 205:
            player_x += 10
        elif player_x >= 565 and player_x <= 730 and player_y >= 205 and player_y <= 211:
            player_y += 10
    
    #дебаг
    if key[pygame.K_p]:
        print(f'x:{player_x}, y:{player_y}')
    if key[pygame.K_y]:
        wt = input('add, remove, set:\n')
        if wt =='add':
            add = int(input('number:\n'))
            player_y += add
        elif wt == 'remove':
            remove = int(input('number:\n'))
            player_y -=remove
        elif wt == 'set':
            setup = int(input('nember:\n'))
            player_y = setup
        else:
            print('none')
    if key[pygame.K_x]:
        wt = input('add, remove, set:\n')
        if wt =='add':
            add = int(input('number:\n'))
            player_x += add
        elif wt == 'remove':
            remove = int(input('number:\n'))
            player_x -=remove
        elif wt == 'set':
            setup = int(input('nember:\n'))
            player_x = setup
        else:
            print('none')
    #шось
    pygame.display.update()

    timegm.tick(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamework = False
            pygame.quit()

    
