# 图像和办公文档处理

from random import randint
from PIL import Image , ImageFilter

image = Image.open('res/dog.webp')

# print(image.format, image.size, image.mode)
# image.show()

# 裁剪
# rect = 80, 20, 310, 360
# image.crop(rect).show()

# 缩略图
# size = 128, 128
# image.thumbnail(size)
# image.show()

# 缩放和黏贴
# image2 = Image.open('res/dog.webp')
# width, height = image2.size
# image.paste(image2.resize((int(width/1.5), int(height/1.5))), (172, 40))
# image.show()

# 旋转与翻转
# image.rotate(180).show()
# image.transpose(Image.FLIP_LEFT_RIGHT).show()

# 修改像素
# for x in range(200, 400):
#     for y in range(200, 400):
#         image.putpixel(
#             (x, y), (randint(0, 255), randint(0, 255), randint(0, 255)))
# image.show()

# 滤镜
image.filter(ImageFilter.CONTOUR).show()