import time
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
import random
root=Tk()
root.title('Tic Tac Toe')
root.config(bg='black')

class Tic_Tac(object):                        
    
    def about(self):
        messagebox.showinfo('About','This super funny and interesting game\nis developed by Razz Sawhoney...\nFor more info please do contact us:rajsahani1819@gmail.com')
        
    def currentScore(self,event=None):
        messagebox.showinfo('LiveScore',f'Your score={self.playerScore}\n{self.player2_Id}={self.adminScore}')
        
    def displayPlayerScore(self):
        messagebox.showinfo('Your Score',f'Your score={self.playerScore}')
        
    def displayAdminScore(self):
        messagebox.showinfo('Your Score',f"{self.player2_Id}'s score={self.adminScore}")
        
    def draw(self):
        messagebox.showinfo('Draw','Its a draw guys...!')
                
    def fullBoard(self):
        return  self.B1["text"]!='' and self.B2["text"]!='' and self.B3["text"]!='' and self.B4["text"]!='' and self.B5["text"]!='' and self.B6["text"]!='' and self.B7["text"]!='' and self.B8["text"]!='' and self.B9["text"]!=''
                
    def winCheck(self,marker):        
        return (self.B1["text"]==self.B2["text"]==self.B3["text"]==marker) or    (self.B4["text"]==self.B5["text"]==self.B6["text"]==marker ) or (self.B7["text"]==self.B8["text"]==self.B9["text"]==marker ) or (self.B1["text"]==self.B5["text"]==self.B9["text"]==marker ) or (self.B3["text"]==self.B5["text"]==self.B7["text"]==marker ) or (self.B1["text"]==self.B4["text"]==self.B7["text"]==marker ) or (self.B2["text"]==self.B5["text"]==self.B8["text"]==marker ) or (self.B3["text"]==self.B6["text"]==self.B9["text"]==marker )
        
    def result(self,who_won,marker,score):
        messagebox.showinfo('Result',f'{who_won}:{marker} won this game...!')
        messagebox.showinfo('Info.','Clear the board to play more')
        
    def restart(self,event=None):
        self.clearBoard()
        self.adminScore=0
        self.playerScore=0
        self.click=True
        self.newWindow.forget(self.newWindow)
        self.updateLiveAction(">>>>New game started...<<<<")
        
    def clearBoard(self,event=None):        
        self.click=True
        self.wigets()
        self.newWindow.forget(self.newWindow)
        self.updateLiveAction(">>>>Board cleared!!!<<<<")
                
    def changeBBG(self):        
        color=colorchooser.askcolor(self.B1['bg'])
        if color:
            self.color=color[1]
            self.B1["bg"]=self.B2["bg"]=self.B3["bg"]=self.B4["bg"]=self.B5["bg"]=self.B6["bg"]=self.B7["bg"]=self.B8["bg"]=self.B9["bg"]=self.color
            
    def changeMarker(self,event=None):
        if self.playerMarker=='X':
            self.playerMarker='O'
            self.adminMarker='X'
            self.wigets()
            messagebox.showinfo('Marker Change:','Marker changed to O..')
        else:
            self.playerMarker='X'
            self.adminMarker='O'
            messagebox.showinfo('Marker Change:','Marker changed to X..')
            
    def quit_app(self,event=None):
        if messagebox.askquestion('Confirmation!!','Do you really wanna quit the game??'):
            self.currentScore()            
            if self.adminScore > self.playerScore:
                messagebox.showinfo('Final Result:','Sorry but you lose the game\nBetter luck next time..')
                quit()
            elif self.adminScore < self.playerScore:
                messagebox.showinfo('Final Result:','Congratulations!!!\nYou are winner..')
                quit()
            else:
                messagebox.showinfo('Final Result:','Both of you share equal points...')
                quit()
        else:
            pass
            
    def playwithFriend(self):
        self.flag='F'
        self.player2_Id='Player 2'
        self.restart()
        
    def playwithAdmin(self):
        self.flag='A'
        self.player2_Id='Admin'
        self.restart()        
        
    def SetPosition(self,Bs,marker):        
        Bs["text"]=marker
        
    def control(self,btns):
        #For Both Player Case        
        if self.click and btns['text']=='':
            self.newWindow.forget(self.newWindow)
            self.updateLiveAction(f">>>>Its {self.player2_Id}'s turn<<<<")
            self.SetPosition(btns,self.playerMarker)
            self.click=False
            if self.winCheck(self.playerMarker):
                self.newWindow.forget(self.newWindow)
                self.updateLiveAction('>>>>You won<<<<' )
                self.playerScore+=1
                self.updateScore()
                self.result('You',self.playerMarker,self.playerScore)                
                self.click=None
            elif self.fullBoard():
                self.newWindow.forget(self.newWindow)
                self.updateLiveAction('>>>>Its a draw<<<<')
                self.draw()
                self.click=None
                
                #For Player 2 case                        
                
        elif self.click==False:
            self.newWindow.forget(self.newWindow)
            self.updateLiveAction('>>>>Its Yours turn<<<<')
            #For playing with Friend
            if self.flag=='F' and btns['text']=='':
                self.SetPosition(btns,self.adminMarker)
                self.click=True
            
            #For playing with Admin
            if self.flag=='A':                
                while self.click==False:
                    bt=random.randint(1,9)
                    if (self.B2["text"]==self.adminMarker and self.B3["text"]==self.adminMarker and self.B1["text"]=='') or (self.B4["text"]==self.adminMarker and self.B7["text"]==self.adminMarker and self.B1["text"]=='') or (self.B5["text"]==self.adminMarker and self.B9["text"]==self.adminMarker and self.B1["text"]==''):
                        self.SetPosition(self.B1,self.adminMarker)
                        self.click=True
                    elif (self.B1["text"]==self.adminMarker and self.B3["text"]==self.adminMarker and self.B2["text"]=='') or (self.B5["text"]==self.adminMarker and self.B8["text"]==self.adminMarker and self.B2["text"]==''):
                        self.SetPosition(self.B2,self.adminMarker)
                        self.click=True
                    elif (self.B1["text"]==self.adminMarker and self.B2["text"]==self.adminMarker and self.B3["text"]=='') or (self.B5["text"]==self.adminMarker and self.B7["text"]==self.adminMarker and self.B3["text"]=='') or (self.B6["text"]==self.adminMarker and self.B9["text"]==self.adminMarker and self.B3["text"]==''):
                        self.SetPosition(self.B3,self.adminMarker)
                        self.click=True
                    elif (self.B1["text"]==self.adminMarker and self.B7["text"]==self.adminMarker and self.B4["text"]=='') or (self.B5["text"]==self.adminMarker and self.B6["text"]==self.adminMarker and self.B4["text"]==''):
                        self.SetPosition(self.B4,self.adminMarker)
                        self.click=True
                    elif (self.B1["text"]==self.adminMarker and self.B9["text"]==self.adminMarker and self.B5["text"]=='') or (self.B3["text"]==self.adminMarker and self.B7["text"]==self.adminMarker and self.B5["text"]=='') or (self.B4["text"]==self.adminMarker and self.B6["text"]==self.adminMarker and self.B5["text"]=='') or (self.B2["text"]==self.adminMarker and self.B8["text"]==self.adminMarker and self.B5["text"]==''):
                        self.SetPosition(self.B5,self.adminMarker)
                        self.click=True
                    elif (self.B4["text"]==self.adminMarker and self.B5["text"]==self.adminMarker and self.B6["text"]=='') or (self.B3["text"]==self.adminMarker and self.B9["text"]==self.adminMarker and self.B6["text"]==''):
                        self.SetPosition(self.B6,self.adminMarker)
                        self.click=True
                    elif (self.B1["text"]==self.adminMarker and self.B4["text"]==self.adminMarker and self.B7["text"]=='') or (self.B5["text"]==self.adminMarker and self.B3["text"]==self.adminMarker and self.B7["text"]=='') or (self.B8["text"]==self.adminMarker and self.B9["text"]==self.adminMarker and self.B7["text"]==''):
                        self.SetPosition(self.B7,self.adminMarker)
                        self.click=True
                    elif (self.B7["text"]==self.adminMarker and self.B9["text"]==self.adminMarker and self.B8["text"]=='') or (self.B2["text"]==self.adminMarker and self.B5["text"]==self.adminMarker and self.B8["text"]==''):
                        self.SetPosition(self.B8,self.adminMarker)
                        self.click=True
                    elif (self.B7["text"]==self.adminMarker and self.B8["text"]==self.adminMarker and self.B9["text"]=='') or (self.B1["text"]==self.adminMarker and self.B5["text"]==self.adminMarker and self.B9["text"]=='') or (self.B3["text"]==self.adminMarker and self.B6["text"]==self.adminMarker and self.B9["text"]==''):
                        self.SetPosition(self.B9,self.adminMarker)            
                        self.click=True            
            
            #Defensive algorithms here
                    elif (self.B2["text"]==self.playerMarker and self.B3["text"]==self.playerMarker and self.B1["text"]=='') or (self.B4["text"]==self.playerMarker and self.B7["text"]==self.playerMarker and self.B1["text"]=='') or (self.B5["text"]==self.playerMarker and self.B9["text"]==self.playerMarker and self.B1["text"]==''):
                        self.SetPosition(self.B1,self.adminMarker)
                        self.click=True
                    elif (self.B1["text"]==self.playerMarker and self.B3["text"]==self.playerMarker and self.B2["text"]=='') or (self.B5["text"]==self.playerMarker and self.B8["text"]==self.playerMarker and self.B2["text"]==''):
                        self.SetPosition(self.B2,self.adminMarker)
                        self.click=True
                    elif (self.B1["text"]==self.playerMarker and self.B2["text"]==self.playerMarker and self.B3["text"]=='') or (self.B5["text"]==self.playerMarker and self.B7["text"]==self.playerMarker and self.B3["text"]=='') or (self.B6["text"]==self.playerMarker and self.B9["text"]==self.playerMarker and self.B3["text"]==''):
                        self.SetPosition(self.B3,self.adminMarker)
                        self.click=True
                    elif (self.B1["text"]==self.playerMarker and self.B7["text"]==self.playerMarker and self.B4["text"]=='') or (self.B5["text"]==self.playerMarker and self.B6["text"]==self.playerMarker and self.B4["text"]==''):
                        self.SetPosition(self.B4,self.adminMarker)
                        self.click=True
                    elif (self.B1["text"]==self.playerMarker and self.B9["text"]==self.playerMarker and self.B5["text"]=='') or (self.B3["text"]==self.playerMarker and self.B7["text"]==self.playerMarker and self.B5["text"]=='') or (self.B4["text"]==self.playerMarker and self.B6["text"]==self.playerMarker and self.B5["text"]=='') or (self.B2["text"]==self.playerMarker and self.B8["text"]==self.playerMarker and self.B5["text"]==''):
                        self.SetPosition(self.B5,self.adminMarker)
                        self.click=True
                    elif (self.B4["text"]==self.playerMarker and self.B5["text"]==self.playerMarker and self.B6["text"]=='') or (self.B3["text"]==self.playerMarker and self.B9["text"]==self.playerMarker and self.B6["text"]==''):
                        self.SetPosition(self.B6,self.adminMarker)
                        self.click=True
                    elif (self.B1["text"]==self.playerMarker and self.B4["text"]==self.playerMarker and self.B7["text"]=='') or (self.B5["text"]==self.playerMarker and self.B3["text"]==self.playerMarker and self.B7["text"]=='') or (self.B8["text"]==self.playerMarker and self.B9["text"]==self.playerMarker and self.B7["text"]==''):
                        self.SetPosition(self.B7,self.adminMarker)
                        self.click=True
                    elif (self.B7["text"]==self.playerMarker and self.B9["text"]==self.playerMarker and self.B8["text"]=='') or (self.B2["text"]==self.playerMarker and self.B5["text"]==self.playerMarker and self.B8["text"]==''):
                        self.SetPosition(self.B8,self.adminMarker)
                        self.click=True
                    elif (self.B7["text"]==self.playerMarker and self.B8["text"]==self.playerMarker and self.B9["text"]=='') or (self.B1["text"]==self.playerMarker and self.B5["text"]==self.playerMarker and self.B9["text"]=='') or (self.B3["text"]==self.playerMarker and self.B6["text"]==self.playerMarker and self.B9["text"]==''):
                        self.SetPosition(self.B9,self.adminMarker)
                        self.click=True

    #Anti-SuperTricks algorithms
    
            #Protectin for 1
                    elif (self.B1["text"]==self.playerMarker and self.B5["text"]==''):
                        self.SetPosition(self.B5,self.adminMarker)
                        self.click=True
            #Protectin for 7
                    elif (self.B7["text"]==self.playerMarker and self.B5["text"]==''):
                        self.SetPosition(self.B5,self.adminMarker)
                        self.click=True
                
            #Protectin for 3                                                
                    elif (self.B3["text"]==self.playerMarker and self.B7["text"]==''):
                        self.SetPosition(self.B7,self.adminMarker)
                        self.click=True
                
         #Protectin for 9                
                    elif (self.B9["text"]==self.playerMarker and self.B5["text"]==''):
                        self.SetPosition(self.B5,self.adminMarker)
                        self.click=True            
                                    
          #Random selection algorithm here                
                    elif bt==1 and self.B1["text"]=='':
                        self.SetPosition(self.B1,self.adminMarker)
                        self.click=True
                    elif bt==2 and self.B2["text"]=='':
                        self.SetPosition(self.B2,self.adminMarker)
                        self.click=True 
                    elif bt==3 and self.B3["text"]=='':
                        self.SetPosition(self.B3,self.adminMarker)
                        self.click=True
                    elif bt==4 and self.B4["text"]=='':
                        self.SetPosition(self.B4,self.adminMarker)
                        self.click=True                
                    elif bt==5 and self.B5["text"]=='':
                        self.SetPosition(self.B5,self.adminMarker)
                        self.click=True
                    elif bt==6 and self.B6["text"]=='':
                        self.SetPosition(self.B6,self.adminMarker)
                        self.click=True
                    elif bt==7 and self.B7["text"]=='':
                        self.SetPosition(self.B7,self.adminMarker)
                        self.click=True
                    elif bt==8 and self.B8["text"]=='':
                        self.SetPosition(self.B8,self.adminMarker)
                        self.click=True
                    elif bt==9 and self.B9["text"]=='':
                        self.SetPosition(self.B9,self.adminMarker)
                        self.click=True            
                        
            if self.winCheck(self.adminMarker):
                self.newWindow.forget(self.newWindow)
                self.updateLiveAction(f'>>>>{self.player2_Id} won<<<<' )
                self.adminScore+=1
                self.updateScore()
                self.result(self.player2_Id,self.adminMarker,self.adminScore)
                self.click=None
            elif self.fullBoard():
                self.newWindow.forget(self.newWindow)
                updateLiveAction('>>>>Its a draw<<<<')
                self.draw()
                self.click=None                 
        
    def board_buttons(self):
        self.B1=Button(self.master,text='',height=5,width=11,bg=self.color,fg='#21f608',padx=3,pady=3,command=lambda:self.control(self.B1))
        self.B1.grid(row=0,column=0,sticky=N+S+E+W)
        self.B2=Button(self.master,text='',height=5,width=11,bg=self.color,fg='#21f608',padx=3,pady=3,command=lambda:self.control(self.B2))
        self.B2.grid(row=0,column=1,sticky=N+S+E+W)
        self.B3=Button(self.master,text='',height=5,width=11,bg=self.color,fg='#21f608',padx=3,pady=3,command=lambda:self.control(self.B3))
        self.B3.grid(row=0,column=2,sticky=N+S+E+W)
        self.B4=Button(self.master,text='',height=5,width=11,bg=self.color,fg='#21f608',padx=3,pady=3,command=lambda:self.control(self.B4))
        self.B4.grid(row=1,column=0,sticky=N+S+E+W)
        self.B5=Button(self.master,text='',height=5,width=11,bg=self.color,fg='#21f608',padx=3,pady=3,command=lambda:self.control(self.B5))
        self.B5.grid(row=1,column=1,sticky=N+S+E+W)
        self.B6=Button(self.master,text='',height=5,width=11,bg=self.color,fg='#21f608',padx=3,pady=3,command=lambda:self.control(self.B6))
        self.B6.grid(row=1,column=2,sticky=N+S+E+W)
        self.B7=Button(self.master,text='',height=5,width=11,bg=self.color,fg='#21f608',padx=3,pady=3,command=lambda:self.control(self.B7))
        self.B7.grid(row=2,column=0,sticky=N+S+E+W)
        self.B8=Button(self.master,text='',height=5,width=11,bg=self.color,fg='#21f608',padx=3,pady=3,command=lambda:self.control(self.B8))
        self.B8.grid(row=2,column=1,sticky=N+S+E+W)
        self.B9=Button(self.master,text='',height=5,width=11,bg=self.color,fg='#21f608',padx=3,pady=3,command=lambda:self.control(self.B9))
        self.B9.grid(row=2,column=2,sticky=N+S+E+W)
    
    def wigets(self):       
        
        #Menubar
        
        self.updateScore()
        self.menu=Menu(self.master,bg='#ac00fe',fg='#21f608',bd=8,font=('Roboto Black','8','bold'))
        submenu=Menu(self.menu,bg='#a91e9c',fg='#21f608',bd=9,font=('Dancing Script','10','bold'))
        self.menu.add_cascade(label='Home',menu=submenu)
        submenu.add_command(label='New',command=self.restart,accelerator='Ctrl N')
        submenu.add_command(label='Refresh',command=self.clearBoard,accelerator='Ctrl F')        
        submenu.add_command(label='Current scores',command=self.currentScore,accelerator='Ctrl S')
        submenu.add_command(label='Change Marker',command=self.changeMarker,accelerator='Ctrl M')
        submenu.add_command(label='Change Board Background',command=self.changeBBG)
        submenu.add_separator()
        supersub=Menu(submenu,bg='#ac00fe',fg='#21f608',bd=10)
        submenu.add_cascade(label='Game mode',menu=supersub)
        supersub.add_command(label='Play with friend',command=self.playwithFriend)
        supersub.add_command(label='Play with admin',command=self.playwithAdmin)
        submenu.add_command(label='Exit',command=self.quit_app,accelerator='Ctrl E')        
        helpmenu=Menu(self.menu,bg='#a91e9c',fg='#21f608',font=('Dancing Script','10','bold'))
        self.menu.add_cascade(label='Help',menu=helpmenu)
        helpmenu.add_command(label='About',command=self.about)        
        self.master.config(menu=self.menu)
        self.board_buttons()
        B_quit=Button(self.master,text='Quit',height=2,bd=8,width=11,font=('Roboto Black','7','bold'),bg='#a91e9c',fg='#21f608',padx=3,pady=3,command=self.quit_app)
        B_quit.grid(row=4,column=0,sticky=N+S+E+W)
        
        B_clear=Button(self.master,text='Clear Board',height=2,width=11,bd=8,font=('Roboto Black','7','bold'),bg='#a91e9c',fg='#21f608',padx=3,pady=3,command=self.clearBoard)
        B_clear.grid(row=4,column=2,sticky=N+S+E+W)        
                               
        Button(self.master,text='TIC_TAC\nBy',height=2,font=('Dancing Script','8','bold'),width=7,bg='#ac00fe',fg='#21f608').grid(row=3,column=1,sticky=N+S+E+W)
        Button(self.master,text='-Razz Sawhoney',height=2,font=('Dancing Script','8','bold'),width=7,bg='#ac00fe',fg='#21f608').grid(row=4,column=1,sticky=N+S+E+W)
        
        #KeyBoard ShortCuts Control
        self.master.bind('<Control-n>',self.restart)
        self.master.bind('<Control-m>',self.changeMarker)
        self.master.bind('<Control-s>',self.currentScore)
        self.master.bind('<Control-e>',self.quit_app)
        self.master.bind('<Control-f>',self.clearBoard)
        
    def updateLiveAction(self,action):
        self.newWindow=Toplevel(self.master,bg='#3b0046')
        self.newWindow.title('Live Commentry')
        self.newWindow.geometry('+290+0')
        Label(self.newWindow,text=action,fg='#21f608',bg='#3b0046',font=('Dancing Script','10','bold')).pack(side=BOTTOM)        
        
        
    def updateScore(self):       
       B_playerScr=Button(self.master,text=f'Your={self.playerScore} point',height=2,width=11,font=('Roboto Black','7','bold'),bd=8,bg='#a91e9c',fg='#21f608',padx=3,pady=3,command=self.displayPlayerScore)
       B_playerScr.grid(row=3,column=0,sticky=N+S+E+W)
       B_adminScr=Button(self.master,text=f'{self.player2_Id}={self.adminScore} point',height=2,width=11,bd=8,bg='#a91e9c',font=('Roboto Black','7','bold'),fg='#21f608',padx=3,pady=3,command=self.displayAdminScore) 
       B_adminScr.grid(row=3,column=2,sticky=N+S+E+W)
       
    def __init__(self,master):
        self.master=master
        self.master.protocol('WM_DELETE_WINDOW',self.quit_app)
        self.adminScore=0
        self.playerScore=0
        self.playerMarker='X'
        self.adminMarker='O'
        self.player2_Id='Player 2'
        self.color='#3b0046'
        self.updateLiveAction(">>>Welcome To Tic Tac Toe...!!!<<<")
        self.newWindow.lift(self.master)
        self.wigets()
        self.flag='F'
        self.click=True

time.sleep(0.09)
Tic_Tac(root)
root.mainloop()