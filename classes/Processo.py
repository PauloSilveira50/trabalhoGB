class Processo:
    def _init_(self,pid):
        self.pid=int(pid)

    def getPid(self):
        return self.pid

    def execute(self):
        return  