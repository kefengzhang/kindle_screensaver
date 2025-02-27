# kindle_screensaver
自动构建kindle锁屏壁纸

你自已要知道你kindle壁纸需要的尺寸,可以在这个地方查:https://bookfere.com/gallery/pictures/kindle-screensaver
我的是kpw2024 比例是:1272*1696

1.你先要越狱
2.请安装好usbnet或usbnet lite(https://github.com/notmarek/kindle-usbnetlite/tree/master)
3.将你准备的图片放在build.py一起
4.python build.py 或 python build.py 1272 1696 我会先建一个目录,然后将当前目当的图片切好变黑白转成png,随机命名好bg_ss00.png
5.用ssh登录到你的kindle
6.mount -o remount,rw /  这个是让系统可以写入
7.将生成的图片上传到kindle的/usr/share/blanket/screensaver/目录下,这个目录之前是有图片的,你可以先备份出来
8.mount -o remount,ro / 关闭写的权限

最后附上我整理的几十张图片
