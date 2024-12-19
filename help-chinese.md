# 大家好，这里是clc99的使用文档

## 接下来，我将详细为您介绍clc99的使用方法:)

首先，clc99是一个可以在python3+版本上运行的命令行美化程序，它可以在您的命令行输出前添加类似这样    "<font color=#0099ff size=4 face="黑体">[+]</font>ok" 下面是效果展示图



![image-20210906170853664 - 副本](https://user-images.githubusercontent.com/77145993/132200550-26a32b8a-c08e-43ba-9a7b-c125303285f2.png)


他们对应的使用代码是这样

```python
import clc99
clc99.initsystem()
clc99.print_status('123')
clc99.print_good('good!')
clc99.print_error('错误!')
clc99.print_warning('警告!')
clc99.print_finish('完成')
clc99.print_os('os ok!')
clc99.print_notrun('这是注释')
clc99.print_e('error!')
clc99.print_fileok('文件 ok!')
clc99.print_filerror('文件 error!')
clc99.print_time()
clc99.print_music('播放123.mp3')
clc99.print_video('播放1234.mp4')
clc99.print_ok('OK!')
clc99.print_over('system over;)')
clc99.print_admin('成功获取到管理员权限！')
#clc99.input_str('input:')
print('input_str参数可以返回用户输入的东西，这里不在演示')
clc99.print_dirok('dirok')
clc99.print_direrror('direrror')
clc99.print_comok('设备正常！')
clc99.print_comerror('设备错误！')
clc99.print_uquestion('你知道python吗？')
clc99.print_cquestion('程序有问题！')
def zidingyicolor(str):
    user_c = clc99.user_color('[b]','YELLOW')
    print(user_c+str)
zidingyicolor('自定义的符号')

```

<font color=#FF0000 size=5 face="黑体">注意！在您使用clc99的时候，请一定要执行initsystem函数！</font>

# 方法介绍

```python
initsystem()
```

这个方法用来初始化符号，必须优先执行！

```python
print_status(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#0099ff size=3 face="黑体">[*]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_good(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#0099ff size=3 face="黑体">[+]</font>,ful可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_error(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#FF0000 size=3 face="黑体">[-]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_warning(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#FF8800 size=3 face="黑体">[!]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_finish(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#00FF00 size=3 face="黑体">[√]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_os(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#0099ff size=3 face="黑体">[$]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_notrun(str,full=False)
```

这个方法可以产生提示状态的符号<font color= #800080 size=3 face="黑体">[#]</font>,full方法可以设置文字颜色是否全部着色 ，end参数可以设置print函数的换行符

```python
print_e(str)
```

这个方法可以产生提示状态的符号<font color=#F00 size=3 face="黑体">[@]</font>全部着色

```python
print_fileok(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#0099ff size=3 face="黑体">[.]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_filerror(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#F00 size=3 face="黑体">[.]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_time(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#0099ff size=3 face="黑体">[TIME]</font>shijiangeshi可以设置时间格式，遵循time模块,title可以设置您要显示的文字（str）的位置，有front (前)    before(后)  middle(两边) ,full可以设置文字颜色是否全部着色

```python
print_music(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#0F0 size=3 face="黑体">[music]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_video(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#0F0 size=3 face="黑体">[video]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_ok(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#00F size=3 face="黑体">[OK]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_over(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#999 size=3 face="黑体">[over]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_music(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#0099ff size=3 face="黑体">[Admin]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
input_str(str,full=False)
```

这个方法可以获取用户的输入<font color=#999 size=3 face="黑体">[input]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_dirok(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#0F0 size=3 face="黑体">[/]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_direrror(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#F00 size=3 face="黑体">[/]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_comok(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#0F0 size=3 face="黑体">[C]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_comerror(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#F00 size=3 face="黑体">[C]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_uquestion(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#FF8800 size=3 face="黑体">[?]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
print_cquestion(str,full=False)
```

这个方法可以产生提示状态的符号<font color=#F00 size=3 face="黑体">[?]</font>,full可以设置文字颜色是否全部着色，end参数可以设置print函数的换行符

```python
user_color(title,color,full=False)
```

这个方法可以产生自定义提示状态的符号,full可以设置文字颜色是否全部着色,如下

```python
def zidingyicolor(str):
    user_c = colors.user_color('[b]','YELLOW')
    print(user_c+str)
zidingyicolor('自定义')
```

# 这就是全部的教程文档啦！

## 谢谢！





















