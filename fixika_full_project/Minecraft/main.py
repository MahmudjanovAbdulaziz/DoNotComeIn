from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


class Voxel(Button):
    def __int__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture='white_cube',
            color=color.color(0, 0, 255),
            hightlight_color=color.lime
        )


for z in range(15):
    for x in range(15):
        voxel = Voxel((x, 0, z))

player = FirstPersonController()

app.run()
