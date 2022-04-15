from cmath import exp
from sqlite3 import Row
import tkinter as tk
from turtle import color

LIGHT_GRAY = "#f5f5f5"
SMALL_FONT_STYLE = ("Arial",20)
LARGE_FONT_STYLE = ("Arial",40)
LABEL_COLOR = "#25265E"
FONT_BUTTON_STYLE = ("Arial",20,"bold")
WHITE = "#FFFFFF"

count = 0
class Calculator():
    def __init__(self):
        self.current_expression = ""
        self.total_expression = ""
        self.digits = {
        7 : (1,1), 8 : (1,2) , 9 : (1,3),
        4 : (2,1), 5 : (2,2) , 6 : (2,3),
        1 : (3,1), 2 : (3,2) , 3 : (3,3),
        '.' : (4,1), 0 : (4,2)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}


        #creating a GUI window using tkinter
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.title("Calculator")

        #calling functions
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.create_display_labels()
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_clear_button()
        self.create_equal_button()
        self.create_square_button()
        self.create_braces_button()
        #self.create_sqrt_button()


        #expanding rows in to the full-screen
        self.buttons_frame.rowconfigure(0,weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)


      ## class ended ##


    # create functions

    def add_braces(self,x):
        global count
        print(count)
        if x == '()':
            count += 1 
            if count%2 != 0:
                self.current_expression += '('
                self.update_label()
            else:
                self.total_expression += self.current_expression
                self.total_expression += ')'
                self.current_expression = ""
                self.update_total_label()
                self.update_label() 


    def add_to_expression(self,x):
        self.current_expression += str(x) #(9
        self.update_label()

    def add_operator(self,operator):
        self.current_expression += operator # total expression = (9+
        self.total_expression += self.current_expression #9x
        self.current_expression = "" # empty current expression
        self.update_total_label()
        self.update_label()
        print(self.total_expression)

    def square(self):
        self.current_expression = str(eval(f'{self.current_expression}')**2)
        self.update_label()

    #def sqrt(self):
       # self.current_expression = str(eval(f'{self.current_expression}')**0.5)
       # self.update_label()

    def create_display_frame(self):
        frame = tk.Frame(self.window,height=221,bg=LIGHT_GRAY)
        frame.pack(expand=True,fill="both")
        return frame
    
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True,fill="both")
        return frame

    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame,text=str(digit),bg=WHITE,font=LABEL_COLOR,borderwidth=0,command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)

    def create_braces_button(self):
        button = tk.Button(self.buttons_frame,text="()",bg=WHITE,font=LABEL_COLOR,borderwidth=0,command = lambda x = "()": self.add_braces(x))
        button.grid(row=0,column=2,sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator,symbol in self.operations.items():
            button = tk.Button(self.buttons_frame,text=symbol,bg=WHITE,font=LABEL_COLOR,borderwidth=0,command=lambda x=operator: self.add_operator(x))
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i += 1

    def create_square_button(self):
        button = tk.Button(self.buttons_frame,text='x\u00b2',bg=WHITE,font=LABEL_COLOR,borderwidth=0,command= self.square)
        button.grid(row=0,column=1,sticky=tk.NSEW)

    #def create_sqrt_button(self):
        #button = tk.Button(self.buttons_frame,text='\u221ax',bg=WHITE,font=LABEL_COLOR,borderwidth=0,command= self.sqrt)
        #button.grid(row=0,column=2,sticky=tk.NSEW)
    
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame,text="C",bg=WHITE,font=LABEL_COLOR,borderwidth=0,command=self.clear)
        button.grid(row=0,column=3,sticky=tk.NSEW)

    def create_equal_button(self):
        button = tk.Button(self.buttons_frame,text="=",bg=WHITE,font=LABEL_COLOR,borderwidth=0,command=self.evaluate)
        button.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW)
    
    def create_display_labels(self):
        self.total_label = tk.Label(self.display_frame,text=self.total_expression,bg=LABEL_COLOR,font=SMALL_FONT_STYLE,anchor=tk.E)
        self.total_label.pack(expand=True,fill="both")

        self.label = tk.Label(self.display_frame,text=self.current_expression,bg=LABEL_COLOR,font=LARGE_FONT_STYLE,anchor=tk.E)
        self.label.pack(expand=True,fill="both")

        return self.total_label,self.label

    def evaluate(self):
        self.total_expression += self.current_expression
        try:
            self.current_expression = str(eval(f'{self.total_expression}'))
            self.update_total_label()
        except Exception as e:
            self.current_expression = "Error!"
        finally:
            self.update_label()
            self.current_expression= ""

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()
        
    def update_label(self):
        self.label.config(text=self.current_expression[:11])


    def update_total_label(self):
        expression = self.total_expression
        for operator,symbol in self.operations.items():
            expression = expression.replace(operator,f'{symbol}')
        self.total_label.config(text=expression)


    def run(self):
        self.window.mainloop()



if __name__ == "__main__":
    calc = Calculator()
    calc.run()
