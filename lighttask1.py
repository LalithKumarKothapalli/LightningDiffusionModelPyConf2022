import lightning as L

class TaskOne(L.LightningWork):
    def __init__(self):
        super().__init__()
        self.demo = "Hello World"

    def run(self):
        print(self.demo)

component = TaskOne()
app = L.LightningApp(component)