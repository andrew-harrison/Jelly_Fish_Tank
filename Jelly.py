from Tentacle import tentacle

class jelly:
    
    def __init__(self, r, phi, x_pos, y_pos, scale_val, speed):
    
        self.r = width/10
        self.phi = phi
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.scale_val = scale_val
        self.speed = speed # value between 0.5 and 1
        self.dir = 0
        
    def DrawCustomShape(self, pts):
        for i in range(len(pts)):
            if i == len(pts)-1:
                line(pts[i][0], pts[i][1], pts[0][0], pts[0][1])
            else:
                line(pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1])
    
    def AddReflection(self, points):
        
        points_mirror = [[-i[0],i[1]] for i in reversed(points)]
        all_points = points + points_mirror
        return all_points

    def DrawCroissant(self):
        
        r = self.r
        phi = self.phi*self.speed
        
        self.x_pos += sin(self.dir)*self.speed*5*(0.8+sin(phi - PI/8))
        self.y_pos -= cos(self.dir)*self.speed*3*(0.8+sin(phi - PI/8))
        
        translate(self.x_pos,self.y_pos)
        rotate(self.dir)
        
        x_scale = 0.5*self.scale_val*(1+0.2*cos(phi))
        y_scale = 1*self.scale_val*(1+0.1*sin(phi))        
        scale(x_scale, y_scale)
        stroke(0)
        fill(100,100,100)
        
        segs = 80
        pts = [[0]*2 for i in range(segs)] # x stored at pts[i][0]
        theta = -PI/2
        y_smooth = 0.4 #Smoothing in y-direction as %
        theta_smooth = PI/2*(y_smooth) 
        depth = 0.4 #Difference  in radius between two arcs
        seg_count = 0 #Counter to find length of lower arc
        
        for pt in pts:
            wobble = r*0.01*cos((theta+phi/20)*15)
            
            #Upper Surface
            if(theta <= - theta_smooth):
                pt[0] = (r+wobble)*cos(theta)
                pt[1] = (r+wobble)*sin(theta)
                
            #Lower Surface
            elif(theta >= (theta_smooth)):
                seg_count += 1 
                wobble *=4
                pt[0] = (r+wobble)*cos(theta)
                pt[1] = - depth*(r+wobble)*(sin(theta))
                wobble *=0.25
            else:
                pt[0] = (r+wobble)*cos(theta)
                
                b_ftr = map(theta, -theta_smooth, theta_smooth, 0,1)
                pt[1] = (r+wobble)*(sin(theta)*(1 - b_ftr*(1 + depth)) - 0.22*sin(PI*b_ftr))
                
            theta += (PI)/(segs-1)
    
        tentacle_spacing = 8    
        if tentacle_spacing %2 == 1:
            raise Exception("Tentacle spacing must be even")
            
        tentacle_start = len(pts) - seg_count
        tentacle_stop = len(pts)-tentacle_spacing/2
        tentacle_range = range(tentacle_start, tentacle_stop, tentacle_spacing) 
        tentacle_length = r/3
            
        all_tentacles = [tentacle(pts[i-1:i+2], r)  for i in tentacle_range]
        
        pts = self.AddReflection(pts)
        self.DrawCustomShape(pts)
        
        for t in all_tentacles:
            t.phi = phi
            t.GenTen()
            t.DrawTen()
    
