#%%
import matplotlib.pyplot as plt

class Circle(object): 
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color
    def add_radius(self, radius):
        self.radius += radius
        return self.radius
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0,0), radius=self.radius,fc=self.color))
        plt.axis('scaled')
        plt.show()

circle = Circle(10, 'red')
# circle.drawCircle()

class Rectangle(object):
    def __init__(self, width=2, height=2, color='r'):
        self.height = height
        self.width = width
        self.color = color
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0), self.width, self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()

rect = Rectangle(10, 2, 'purple')
rect.drawRectangle()