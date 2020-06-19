class tentacle:
    
    def __init__(self, three_points, ten_len):
        if len(three_points) !=3:
            print(three_points)
            raise Exception("3 points required to make tentacle, you submitted "\
                            + str(len(three_points)))
        
        self.phi = 0
        self.leng = ten_len
        self.anchor = three_points[1]
        self.GetAngle(three_points)
        self.GenTen()
    
    def GetAngle(self,three_points):
        tp = three_points
        dx = tp[0][0]-tp[2][0]
        dy = tp[0][1]-tp[2][1]
        h = sqrt(pow(dx,2)+pow(dy,2))
        
        self.cos_theta = dy/h
        self.sin_theta = dx/h
    
    def GenTen(self):
        leng = self.leng
        lin = [[0,0] for i in range(leng)] 
        lin[0] = self.anchor
        n_scale = 2*PI/leng 
        
        for n, pt in enumerate(lin[1:], start = 1):
            attn = 1/(pow(n,3))
            pt[0] = lin[n-1][0] - attn*pow(self.cos_theta, 2) - (1 - attn)*(0.6*cos((2*n*n_scale+self.phi)) + 0.2)
            pt[1] = lin[n-1][1] + attn*pow(self.sin_theta, 2) +1*(1 - attn)
        
        self.lin = lin
        
    def DrawTen(self):
        self.DrawMirrorTen()
        self.RenderTen(self.lin)
    
    def DrawMirrorTen(self):
        Mirror_lin = [[-i[0],i[1]] for i in reversed(self.lin)]
        self.RenderTen(Mirror_lin)        
        
    def RenderTen(self, lin):
        for i in range(len(lin)-1):
            line(lin[i][0], lin[i][1], lin[i+1][0], lin[i+1][1])        
