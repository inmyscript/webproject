from PIL import Image,ImageDraw,ImageFont


#w = 638
#h = 1063
im = Image.open(r"名片1.jpg")

(w,h) = im.size

bg = Image.new("RGB",(w,h),(255,255,255))

#im = Image.open(r"名片1.jpg")

draw2 = Image.blend(bg,im,1.0)

draw = ImageDraw.Draw(draw2)

name = "梁二哈"
site = "地址:"+"广东省清远市某某区屋某村某巷21号"
work = "游戏开发工程师"
tel  = "手机:"+"138-1536-1734"
phone= "座机:"+"12332311"
email= "邮箱:"+"uehariuhri@168.com"
web  = "网址:"+"www.youcanyouup@168.com"

h = 180
w  = 80
h1= 280
for i in range(len(name)):
    if i == 0:
        draw.text((w,100),name[i], fill=(20,20,20),font=ImageFont.truetype(r"方正黑体简体.ttf",60))
    else:
        
        draw.text((w,h),name[i], fill=(20,20,20),font=ImageFont.truetype(r"方正黑体简体.ttf",60))		# （7）在图像绘制对象中添加文字：
        h += 65

for i in work[::-1]:
        draw.text((160,h1),i, fill=(20,20,20),font=ImageFont.truetype(r"方正黑体简体.ttf",23))
        h1 -= 23
        
draw.text((w,500),tel[0:3], fill=(20,20,20),font=ImageFont.truetype(r"方正黑体简体.ttf",23))      
draw.text((w,530),tel[3:], fill=(20,20,20),font=ImageFont.truetype(r"方正黑体简体.ttf",35))

draw.text((w,700),phone, fill=(20,20,20),font=ImageFont.truetype(r"方正黑体简体.ttf",23))
draw.text((w,750),email, fill=(20,20,20),font=ImageFont.truetype(r"方正黑体简体.ttf",23))
draw.text((w,850),web, fill=(20,20,20),font=ImageFont.truetype(r"方正黑体简体.ttf",23))
draw.text((w,900),site, fill=(20,20,20),font=ImageFont.truetype(r"方正黑体简体.ttf",23))

draw2.show()
