# Hello everyone, here is the use document of colorconsole99

## Next, I will introduce you how to use colorconsole 99 in detail:)

First of all, colorconsole99 is a command-line beautification program that can be run on Python 3 +. It can add a similar "<font color = #0099ff size = 4 face ="blod "> [+] </font >OK" before your command-line output. The following is the effect display diagram

![image-20210906174615747](E:\99自制库\colorconsole99\1.0.0\images-md\image-20210906174615747.png)

Their corresponding call code is like this

```python
from colorconsole99 import *
colors.initsystem()
colors.print_status('status')
colors.print_good('ok!')
colors.print_error('error!')
colors.print_warning('warning!')
colors.print_finish('finish')
colors.print_os('os ok!')
colors.print_notrun('This is a comment')
colors.print_e('error!')
colors.print_fileok('file ok!')
colors.print_filerror('file error!')
colors.print_time()
colors.print_music('play 123.mp3')
colors.print_video('play 1234.mp4')
colors.print_ok('OK!')
colors.print_over('system over;)')
colors.print_admin('Successfully obtained administrator privileges!')
#colors.input_str('input:')
print("'input_str'Parameters can return the user's input, which is not demonstrated here")
colors.print_dirok('dirok')
colors.print_direrror('direrror')
colors.print_comok('The equipment is normal！')
colors.print_comerror('equipment error！')
colors.print_uquestion('Do you know Python？')
colors.print_cquestion('There is a problem with the procedure！')
def zidingyicolor(str):
    user_c = colors.user_color('[b]','YELLOW')
    print(user_c+str)
zidingyicolor('Custom symbols')
```

# <font color = #ff0000 size = 5 face = "bold" > attention! When you use colorconsole 99, be sure to execute the initsystem method</font>

# Method introduction



```python
initsystem()
```

This method is used to initialize symbols and must be executed first!

```python
print_status(str,full=False)
```

This method can generate a prompt status symbol <font color = #0099ff size = 3 face = "bold" > [*] </font >, and full can set whether all text colors are colored

```python
print_good(str,full=False)
```

This method can generate a prompt status symbol <font color = #0099ff size = 3 face = "bold" > [+] </font >, and ful can set whether all text colors are colored

```python
print_error(str,full=False)
```

This method can generate prompt status symbols <font color = #ff0000 size = 3 face = "bold" > [-] </font >, and full can set whether all text colors are colored

```python
print_warning(str,full=False)
```

This method can generate a prompt status symbol <font color = #ff8800 size = 3 face = "bold" > [!]</Font >, full can set whether all text colors are colored

```python
print_finish(str,full=False)
```

This method can generate a prompt status symbol <font color = #00ff00 size = 3 face = "bold" > [√] </font >, and full can set whether all text colors are colored

```python
print_os(str,full=False)
```

This method can generate prompt status symbols <font color = #0099ff size = 3 face = "bold" > [$] </font >, and full can set whether all text colors are colored

```python
print_notrun(str,full=False)
```

This method can generate a prompt status symbol <font color = #800080 size = 3 face = "bold" > [#] </font >, and the full method can set whether all text colors are colored

```python
print_e(str)
```

This method can generate the prompt status symbols <font color = #f00 size = 3 face = "bold" > [@] </font > all coloring

```python
print_fileok(str,full=False)
```

This method can generate a prompt status symbol <font color = #0099ff size = 3 face = "bold" > [。]</Font >, full can set whether all text colors are colored

```python
print_filerror(str,full=False)
```

This method can generate prompt status symbols <font color = #f00 size = 3 face = "bold" > [.] </font >, and full can set whether all text colors are colored

```python
print_time(str,full=False)
```

This method can generate prompt status symbols <font color = #0099ff size = 3 face = "bold" > [time] </font > shijiangeshi can set the time format, follow the time module, title can set the position of the text (str) to be displayed, with front (front) before (back) middle (both sides), and full can set whether all text colors are colored

```python
print_music(str,full=False)
```

This method can generate prompt symbols <font color = #0f0 size = 3 face = "bold" > [music] </font >, and full can set whether all text colors are colored

```python
print_video(str,full=False)
```

This method can generate prompt symbols <font color = #0f0 size = 3 face = "bold" > [Video] </font >, and full can set whether all text colors are colored

```python
print_ok(str,full=False)
```

This method can generate a prompt status symbol <font color = #00f size = 3 face = "bold" > [OK] </font >, and full can set whether all text colors are colored

```python
print_over(str,full=False)
```

This method can generate prompt status symbols <font color = #999 size = 3 face = "bold" > [over] </font >, and full can set whether all text colors are colored

```python
print_music(str,full=False)
```

This method can generate prompt status symbols <font color = #0099ff size = 3 face = "bold" > [Admin] </font >, and full can set whether all text colors are colored

```python
input_str(str,full=False)
```

This method can get the user's input <font color = #999 size = 3 face = "bold" > [input] </font >, and full can set whether all text colors are colored

```python
print_dirok(str,full=False)
```

This method can generate a prompt status symbol <font color = #0f0 size = 3 face = "bold" > [/] </font >, and full can set whether all text colors are colored

```python
print_direrror(str,full=False)
```

This method can generate a prompt status symbol <font color = #f00 size = 3 face = "bold" > [/] </font >, and full can set whether all text colors are colored

```python
print_comok(str,full=False)
```

This method can generate a prompt status symbol <font color = #0f0 size = 3 face = "bold" > [C] </font >, and full can set whether all text colors are colored

```python
print_comerror(str,full=False)
```

This method can generate a prompt status symbol <font color = #f00 size = 3 face = "bold" > [C] </font >, and full can set whether all text colors are colored

```python
print_uquestion(str,full=False)
```

This method can generate a prompt status symbol <font color = #ff8800 size = 3 face = "bold" > [?]</Font >, full can set whether all text colors are colored

```python
print_music(str,full=False)
```

This method can generate a prompt status symbol <font color = #f00 size = 3 face = "bold" > [?]</Font >, full can set whether all text colors are colored

```python
user_color(title,color,full=False)
```

This method can generate custom prompt status symbols. Full can set whether all text colors are colored, as shown below

```python
def zidingyicolor(str):
    user_c = colors.user_color('[b]','YELLOW')
    print(user_c+str)
zidingyicolor('Custom symbols')
```

# This is all the tutorial documentation!

## thank you!





















