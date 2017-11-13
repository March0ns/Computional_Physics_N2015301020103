import sys
import pygame
import math
import random

    
def run_game():
    
       pygame.init()
       
       v=5
       width,height=1020,574
       screen=pygame.display.set_mode((width,height))
       pygame.display.set_caption("Shell game")
       player=pygame.image.load("resources/images/player22.png")
       grass=pygame.image.load("resources/images/bg.jpg")
       arrow = pygame.image.load("resources/images/bullet1.png")
       badguyimg1=pygame.image.load("resources/images/nudle.png")
       badguyimg=badguyimg1
       badtimer=100
       badtimer1=0
       badguys=[[640,500]]
       keys = [False,False]

       playerpos=[10,430]
       arrows=[]
      
       
       
       while True:
           badtimer-=1
           for event in pygame.event.get():
               if event.type==pygame.QUIT:
                   pygame.quit()
                   sys.exit()
               if event.type==pygame.MOUSEBUTTONDOWN:
                        position=pygame.mouse.get_pos()
                        bullet=[math.atan2(position[1]-(playerpos[1]+5),position[0]-(playerpos[0]+5)),playerpos[0]+60,playerpos[1]+55]
                        vx=v*math.cos(bullet[0])
                        vy=math.sin(bullet[0])*v
                        bullet.append(vx)
                        bullet.append(vy)
                        arrows.append(bullet)
                        

               if event.type == pygame.KEYDOWN:
                  if event.key==pygame.K_a:
                     keys[0]=True
                  if event.key==pygame.K_d:
                     keys[1]=True
               if event.type == pygame.KEYUP:
                  if event.key==pygame.K_a:
                     keys[0]=False
                  if event.key==pygame.K_d:
                      keys[1]=False
           screen.fill(0) 
           screen.blit(grass,(0,0))
           screen.blit(player,playerpos)
           if badtimer==0:
               badguys.append([640,random.randint(200,400)])
               badtimer=100-(badtimer1*2)
               if badtimer1>=20:
                   badtimer1=20
               else:
                   badtimer1+=5
           index=0
           for badguy in badguys:
               if badguy[0]<-64:
                   badguys.pop(index)
               badguy[0]-=2
               badrect=pygame.Rect(badguyimg.get_rect())
               badrect.left=badguy[0]
               badrect.top=badguy[1]
               if badrect.left<64:
                   badguys.pop(index)
               index+=1
               
               for bullet in arrows:
                   index1=0
                   bullrect=pygame.Rect(arrow.get_rect())
                   bullrect.left=bullet[1]
                   bullrect.top=bullet[2]
                   if badrect.colliderect(bullrect):
                       badguys.pop(index1)
                       arrows.pop(index1)
                   index1+=1
                   
             
           for badguy in badguys:
               screen.blit(badguyimg1,badguy)
           
               
           
           for bullet in arrows:
                         index=0

                         velx=bullet[3]
                         bullet[4] = bullet[4] + 0.02;
                         vely=bullet[4]
                         bullet[1]+=velx
                         bullet[2]+=vely
                         if bullet[1]<-64 or bullet[1]>1020 or bullet[2]<-64 or bullet[2]>574:
                             arrows.pop(index)
                         else:
               
                          index+=1
                         for projectile in arrows:
                            arrow1=pygame.transform.rotate(arrow,360-projectile[0]*57.29)
                            screen.blit(arrow1,(projectile[1],projectile[2]))
              

           
           
           
           pygame.display.flip()
           if keys[0]:
              playerpos[0]-=2
           if keys[1]:
              playerpos[0]+=2

              

run_game()