#coding:utf-8
#作者:99
from colorama import  init,Fore,Back,Style
import platform
import time


initsystem = False

#创建错误类
class Colorconsole99error(Exception):
    def __init__(self, value):
            self.value = value
    def __str__(self):
        return repr(self.value)



#创建主类
class Colors():
    def initsystem(self):
        v_system = platform.system()
        if v_system != 'Windows':
            #print('other')
            initsystem=True
        else:
            init(wrap=True)
            #print('Windows')
            initsystem = True
    def print_status(self,str,full=False):
        if full:
            print(Fore.BLUE+'[*]',end='')
            print(str)
        else:
            print(Fore.BLUE+'[*]'+Fore.RESET,end='')
            print(str)
    def print_good(self,str,full=False):
        if full:
            print(Fore.BLUE+'[+]',end='')
            print(str)
        else:
            print(Fore.BLUE+'[+]'+Fore.RESET,end='')
            print(str)
    def print_error(self,str,full=False):
        if full:
            print(Fore.RED+'[-]',end='')
            print(str)
        else:
            print(Fore.RED+'[-]'+Fore.RESET,end='')
            print(str)
    def print_warning(self,str,full=False):
        if full:
            print(Fore.YELLOW+'[!]',end='')
            print(str)
        else:
            print(Fore.YELLOW+'[!]'+Fore.RESET,end='')
            print(str)
    def print_finish(self,str,full=False):
        if full:
            print(Fore.GREEN+'[√]',end='')
            print(str)
        else:
            print(Fore.GREEN+'[√]'+Fore.RESET,end='')
            print(str)
    def print_os(self,str,full=False):
        if full:
            print(Fore.CYAN+'[$]',end='')
            print(str)
        else:
            print(Fore.CYAN+'[$]'+Fore.RESET,end='')
            print(str)
    def print_notrun(self,str,full=False):
        if full:
            print(Fore.MAGENTA+'[#]',end='')
            print(str)
        else:
            print(Fore.MAGENTA+'[#]'+Fore.RESET,end='')
            print(str)
    def print_e(self,str):
        print(Fore.RED+'[@]'+str+Fore.RESET)
    def print_fileok(self,str,full=False):
        if full:
            print(Fore.BLUE+'[.]',end='')
            print(str)
        else:
            print(Fore.BLUE+'[.]'+Fore.RESET,end='')
            print(str)
    def print_filerror(self,str,full=False):
        if full:
            print(Fore.RED+'[.]',end='')
            print(str)
        else:
            print(Fore.RED+'[.]'+Fore.RESET,end='')
            print(str)
    def print_time(self,str='',shijiangeshi="%Y-%m-%d %H:%M:%S",title='front',full=False):
        if full:
            if title == 'front':
                print(Fore.CYAN+'[TIME]',end='')
                print(str+time.strftime(shijiangeshi, time.localtime()))
            if title == 'before':
                print(Fore.CYAN+'[TIME]',end='')
                print(time.strftime(shijiangeshi, time.localtime())+str)
            if title == 'middle':
                print(Fore.CYAN+'[TIME]',end='')
                print(str+time.strftime(shijiangeshi, time.localtime())+str)
        else:
            if title == 'front':
                print(Fore.CYAN+'[TIME]'+Fore.RESET,end='')
                print(str+time.strftime(shijiangeshi, time.localtime()))
            if title == 'before':
                print(Fore.CYAN+'[TIME]'+Fore.RESET,end='')
                print(time.strftime(shijiangeshi, time.localtime())+str)
            if title == 'middle':
                print(Fore.CYAN+'[TIME]'+Fore.RESET,end='')
                print(str+time.strftime(shijiangeshi, time.localtime())+str)
    def print_music(self,str,full=False):
        if full:
            print(Fore.GREEN+'[playmusic]',end='')
            print(str)
        else:
            print(Fore.GREEN+'[playmusic]'+Fore.RESET,end='')
            print(str)
    def print_video(self,str,full=False):
        if full:
            print(Fore.GREEN+'[playvideo]',end='')
            print(str)
        else:
            print(Fore.GREEN+'[playvideo]'+Fore.RESET,end='')
            print(str)
    def print_ok(self,str,full=False):
        if full:
            print(Fore.BLUE+'[OK]',end='')
            print(str)
        else:
            print(Fore.BLUE+'[OK]'+Fore.RESET,end='')
            print(str)
    def print_over(self,str,full=False):
        if full:
            print(Fore.WHITE+'[OVER]',end='')
            print(str)
        else:
            print(Fore.WHITE+'[OVER]'+Fore.RESET,end='')
            print(str)
    def print_admin(self,str,full=False):
        if full:
            print(Fore.CYAN+'[Admin]',end='')
            print(str)
        else:
            print(Fore.CYAN+'[Admin]'+Fore.RESET,end='')
            print(str)
    def input_str(self,str,full=False):
        if full:
            inp = input('[input]'+str)
            return inp
        else:
            inp = input('[input]'+str)
            return inp
    def print_dirok(self,str,full=False):
        if full:
            print(Fore.GREEN+'[/]',end='')
            print(str)
        else:
            print(Fore.GREEN+'[/]'+Fore.RESET,end='')
            print(str)
    def print_direrror(self,str,full=False):
        if full:
            print(Fore.RED+'[/]',end='')
            print(str)
        else:
            print(Fore.RED+'[/]'+Fore.RESET,end='')
            print(str)
    def print_comok(self,str,full=False):
        if full:
            print(Fore.GREEN+'[C]',end='')
            print(str)
        else:
            print(Fore.GREEN+'[C]'+Fore.RESET,end='')
            print(str)
    def print_comerror(self,str,full=False):
        if full:
            print(Fore.RED+'[C]',end='')
            print(str)
        else:
            print(Fore.RED+'[C]'+Fore.RESET,end='')
            print(str)
    def print_uquestion(self,str,full=False):
        if full:
            print(Fore.YELLOW+'[?]',end='')
            print(str)
        else:
            print(Fore.YELLOW+'[?]'+Fore.RESET,end='')
            print(str)
    def print_cquestion(self,str,full=False):
        if full:
            print(Fore.RED+'[?]',end='')
            print(str)
        else:
            print(Fore.RED+'[?]'+Fore.RESET,end='')
            print(str)
    def print_syscom(self):
        if full:
            print(Fore.CYAN+'[sys_command]',end='')
            print(str)
        else:
            print(Fore.CYAN+'[sys_command]'+Fore.RESET,end='')
            print(str)
    def user_color(self,title,color,full=False):
        #BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
        if color=='RED':
            colorinfo=Fore.RED
        elif color=='BLACK':
            colorinfo=Fore.BLACK
        elif color=='GREEN':
            colorinfo=Fore.GREEN
        elif color=='YELLOW':
            colorinfo=Fore.YELLOW
        elif color=='BLUE':
            colorinfo=Fore.BLUE
        elif color=='MAGENTA':
            colorinfo=Fore.MAGENTA
        elif color=='CYAN':
            colorinfo=Fore.CYAN
        elif color=='WHITE':
            colorinfo=Fore.WHITE
        else:
            raise Colorconsole99error('Unknown color')
        
        if full:
            return colorinfo+title
        else:
            return colorinfo+title+Fore.RESET
            
colors = Colors()