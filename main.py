from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

print(kivymd.__version__)

class Mainapp(MDApp):
    def build(self):
        return MDLabel(text="Hello I am Sandeep", halign = "center")


if __name__ == '__main__':
    Mainapp().run()
