# Hello everyone, here is the use document of clc99

## Next, I will introduce you how to use clc 99 in detail:)

First of all, clc99 is a command-line beautification program that can be run on Python 3 +. It can add a similar "<font color = #0099ff size = 4 face ="blod "> [+] </font >OK" before your command-line output. The following is the effect display diagram

![image-20210906174615747](https://user-images.githubusercontent.com/77145993/132200373-fe106698-a109-44c6-b2d5-eb585ec8d66f.png)


Their corresponding call code is like this

```python
import clc99
clc99.initsystem()
clc99.print_status('status')
clc99.print_good('ok!')
clc99.print_error('error!')
clc99.print_warning('warning!')
clc99.print_finish('finish')
clc99.print_os('os ok!')
clc99.print_notrun('This is a comment')
clc99.print_e('error!')
clc99.print_fileok('file ok!')
clc99.print_filerror('file error!')
clc99.print_time()
clc99.print_music('play 123.mp3')
clc99.print_video('play 1234.mp4')
clc99.print_ok('OK!')
clc99.print_over('system over;)')
clc99.print_admin('Successfully obtained administrator privileges!')
#clc99.input_str('input:')
print("'input_str'Parameters can return the user's input, which is not demonstrated here")
clc99.print_dirok('dirok')
clc99.print_direrror('direrror')
clc99.print_comok('The equipment is normal！')
clc99.print_comerror('equipment error！')
clc99.print_uquestion('Do you know Python？')
clc99.print_cquestion('There is a problem with the procedure！')
def zidingyicolor(str):
    user_c = clc99.user_color('[b]','YELLOW')
    print(user_c+str)
zidingyicolor('Custom symbols')
```

# <font color = #ff0000 size = 5 face = "bold" > attention! When you use clc99, be sure to execute the initsystem method</font>

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

This method can generate a prompt status symbol <font color = #0099ff size = 3 face = "bold" > [.]</Font >, full can set whether all text colors are colored

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
print_cquestion(str,full=False)
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





















