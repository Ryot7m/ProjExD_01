import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    img=pg.image.load("ex01/fig/3.png")
    img=pg.transform.flip(img,True,False)
    imgs=[img,pg.transform.rotozoom(img,2,1.0),pg.transform.rotozoom(img,4,1.0),
          pg.transform.rotozoom(img,6,1.0),pg.transform.rotozoom(img,8,1.0),
          pg.transform.rotozoom(img,10,1.0),pg.transform.rotozoom(img,8,1.0),
          pg.transform.rotozoom(img,6,1.0),pg.transform.rotozoom(img,4,1.0)
          ,pg.transform.rotozoom(img,2,1.0)]
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x=tmr%3200
        screen.blit(bg_img, [-x,0])
        screen.blit(pg.transform.flip(bg_img,True,False), [1600-x,0])
        screen.blit(bg_img, [3200-x,0])
        screen.blit(imgs[tmr%10],[300,200])
        # screen.blit(bg_img,[1600-x,0])
        # screen.blit(imgs[tmr%2],[0,y])
        pg.display.update()
        tmr += 1        
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()