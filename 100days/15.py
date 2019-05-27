from PIL import Image

image = Image.open('test.png')
image.format, image.size, image.mode
('PNG', (500, 750), 'RGB')
image.show()
