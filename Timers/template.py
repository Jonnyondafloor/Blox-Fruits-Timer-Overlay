from PIL import Image, ImageTk
from typing import Callable

class Timer:
    def __init__(self):
        self.image_path = 'image_path'
        self.title = ''
        self.description = ''
        self.auto_reset_enabled = True
        self.auto_reset_delay = 0
        self.delay_method: Callable[[], float] = None
        self.reset_method: Callable[[], float] = None

    def load_image(self) -> ImageTk.PhotoImage | None:
        try:
            img = Image.open(self.image_path).resize((50, 60))
            return ImageTk.PhotoImage(img)
        except FileNotFoundError:
            print(f'Error: Image file not found at {self.image_path}')
            return None
