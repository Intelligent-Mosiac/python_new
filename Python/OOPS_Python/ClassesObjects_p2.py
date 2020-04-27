class Youtube:
    def __init__(self,n,t,r):
        self.Name=n
        self.Type=t
        self.Rating=r
    def reveal_name(self):
        print("The name is "+ self.Name)
y1=Youtube("Mensutra","Self-Help",9)
y2=Youtube("Lucid","Entertainment",8)
y3=Youtube("Eminem","Rap","7")
y1.reveal_name()
y2.reveal_name()
y3.reveal_name()   
