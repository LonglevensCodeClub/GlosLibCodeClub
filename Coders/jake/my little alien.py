import pgzrun
  
alien = Actor('alien')
alien.topright = 0, 10



START = 0
WIDTH = 300
HEIGHT = 300
  
def draw():
      screen.fill((0, 0, 100))
      screen.clear()
      alien.draw()
      
      
def update():
    alien.left -= 2
    if alien.left < START:
        alien.right = 300


def on_mouse_down(pos, button):
    if button == mouse.LEFT and alien.collidepoint(pos):
        print("bbbbblllaaaa!")
        alien.left = 300
    else:
        print("bla you missed")



pgzrun.go()