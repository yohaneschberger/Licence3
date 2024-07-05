import cng

###############################################################

#Exercice 1
def Segment(id_p1, id_p2, pas):
    '''
    Affichage des points avec un pas
    id_p1, id_p2 : identifiant des 2 points
    '''
    pt_cox1, pt_coy1= cng.obj_get_coord(id_p1)[0], cng.obj_get_coord(id_p1)[1] #Recupere les coordonnées des points avec les id
    pt_cox2, pt_coy2= cng.obj_get_coord(id_p2)[0], cng.obj_get_coord(id_p2)[1]
    a= (pt_coy2-pt_coy1)/(pt_cox2-pt_cox1) # a : Calcul de la pente du segment de la droite
    b= pt_coy1 - a*pt_cox1  # b : Calcul de l'ordonnée à l'origine
    x = pt_cox1+pas # x : initialisation de l'abscisse d'un nouveau point du segment avec le pas
    while x < pt_cox2:
        cng.point(x, a*x+b)
        x += pas


#Exercice 2
def Bresenham(x1,y1,x2,y2):
    '''
    Fonction Bresenham pour tout les octants avec 2 points quelconque
    '''
    dx, dy = x2-x1, y2-y1   # Calcul des deltas
    if dx > 0:  # On est sur la partie droite du repère
        if dy > 0:  # On est sur la partie supérieur du repère
            # 1er cadran
            dec = dx - 2*dy # Calcul de la décision
            if abs(dx) >= abs(dy):
                # 1er octant
                x, y = x1, y1
                while x <= x2:
                    cng.point(x,y)
                    if dec < 0: # Si la décision est négative
                        dec += 2*dx
                        y += 1
                    dec -= 2*dy
                    x += 1
            else:
                # 2nd octant
                x1, x2, y1, y2 = y1, y2, x1, x2 # On echange le role de x et y
                dx, dy = dy, dx
                x, y = x1, y1
                while y <= y2:
                    cng.point(y,x)
                    if dec < 0:
                        dec += 2*dx
                        y += 1
                    dec -= 2*dy
                    x += 1
        else:   # dy < 0
            # 4eme cadran
            if abs(dx) >= abs(dy):  
                # 8eme octant
                dx, dy = abs(dx), abs(dy)   # On prend la valeur absolue des deltas
                dec = dx - 2*dy 
                x, y = x1, -y1  # On prend l'opposé de y
                while x <= x2:
                    cng.point(x,-y)
                    if dec < 0:
                        dec += 2*dx
                        y += 1
                    dec -= 2*dy
                    x += 1
            else:
                # 7eme octant
                dx, dy = abs(dx), abs(dy)
                dec = dy - 2*dx
                x, y = y1, -x1  # On prend l'opposé de x
                while y <= -y2:
                    cng.point(x,-y)
                    if dec < 0:
                        dec += 2*dy
                        x += 1
                    dec -= 2*dx
                    y += 1
    else:       # dx < 0
        if dy > 0:  # On est sur la partie supérieur du repère
            # 2nd cadran
            if abs(dx) >= abs(dy):
                # 4eme octant
                dx, dy = abs(dx), abs(dy)
                dec = dx - 2*dy
                x, y = -x1, y1  # On prend l'opposé de x
                while x <= -x2:
                    cng.point(-x,y)
                    if dec < 0:
                        dec += 2*dx
                        y += 1
                    dec -= 2*dy
                    x += 1

            else:
                # 3eme octant
                dx, dy = abs(dx), abs(dy)
                dec = dy - 2*dx
                x, y = -y1, x1  # On prend l'opposé de y
                while y <= y2:
                    cng.point(-x,y)
                    if dec < 0:
                        dec += 2*dy
                        x += 1
                    dec -= 2*dx
                    y += 1
        else:   # dy < 0
            # 3eme cadran
            if dx <= dy:
                # 5eme octant
                dx, dy = abs(dx), abs(dy)
                dec = dx - 2*dy
                x, y = -x1, -y1
                while x <= -x2:
                    cng.point(-x,-y)
                    if dec < 0:
                        dec += 2*dx
                        y += 1
                    dec -= 2*dy
                    x += 1
            else:
                # 6eme octant
                dx, dy = abs(dx), abs(dy)
                dec = dy - 2*dx
                x, y = -y1, -x1
                while y <= -y2:
                    cng.point(-x,-y)
                    if dec < 0:
                        dec += 2*dy
                        x += 1
                    dec -= 2*dx
                    y += 1



###############################################################

'''
Travail sur un repere avec origine (400,400) sur une fenetre de 800,800
'''

cng.init_window('TP2', 800, 800)    # Initialisation de la fenêtre
windows_list= [-10,-10,40,40]
pt_list= [0,0]
viewport_stat= [100,100,200,200]

p_id= cng.point(0,0)
p_id2= cng.point(800,800)
Segment(p_id, p_id2, 5)     #Affichage des points avec un pas

p_id3= cng.point(0,800)
p_id4= cng.point(800,0)
Segment(p_id3, p_id4, 5)    #Affichage des points avec un pas

cng.line(400,0,400,800)     #Affichage des axes
cng.line(0,400,800,400)     #Affichage des axes


Bresenham(0+400,0+400,200+400,300+400)  #Octant 2
Bresenham(0+400,0+400,300+400,200+400)  #Octant 1

Bresenham(0+400,0+400,-200+400,300+400) #Octant 3
Bresenham(0+400,0+400,-300+400,200+400) #Octant 4

Bresenham(0+400,0+400,-300+400,-200+400) #Octant 5
Bresenham(0+400,0+400,-200+400,-300+400) #Octant 6

Bresenham(0+400,0+400,200+400,-300+400) #Octant 7
Bresenham(0+400,0+400,300+400,-200+400) #Octant 8

cng.main_loop() # Boucle principale
