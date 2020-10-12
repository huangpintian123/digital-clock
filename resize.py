from PIL import Image
for _ in range(13):
	img=Image.open('{}.png'.format(_))
	img=img.resize((90,140),Image.ANTIALIAS)
	img.save('{}.png'.format(_))