class Process:
    def __init__(self,priority):
        self.priority = priority
        self.status = 'online'

    def toggle(self):
        if(self.status=='online'):
            self.status = 'offline'
        return self.status  

