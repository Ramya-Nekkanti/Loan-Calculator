from tkinter import *
import math

window = Tk()
window.title('Loan Calculator System')
window.geometry('400x250')
window.config(background='orange')
#Create a frame
frame = Frame(window)
frame.config(bg='light blue')
frame.pack(side="top", expand=True, fill="both")

class loanCal():

    def __init__(self):
        # creating the labels
    
        Label(frame, text='Annual Interest Rate %',fg="brown",bg='light blue',font=('Times', 18), borderwidth=8).place(x = 50,y = 50) 

        Label(frame, text='Numbers of Years', fg="brown",bg='light blue', font=('Times', 18),borderwidth=8).place(x = 50, y = 90) 

        Label(frame, text='Loan Amount', fg="brown",bg='light blue',font=('Times', 18),borderwidth=8).place(x = 50, y = 130) 

        Label(frame, text='Monthly Payment',fg="brown",bg='light blue',font=('Times', 18), borderwidth=8).place(x = 50, y = 250) 

        Label(frame, text='Total Payment', fg="brown",bg='light blue',font=('Times', 18), borderwidth=8).place(x = 50, y = 300) 

        # Create the Entry Widgets
        self.Int_for_Annual = StringVar()
        Entry(frame, textvariable=self.Int_for_Annual, justify=RIGHT).place(x = 300, y = 65) 

        self.yrs = StringVar()
        Entry(frame, textvariable=self.yrs, justify=RIGHT).place(x = 300, y = 105) 

        self.amt = StringVar()
        Entry(frame, textvariable=self.amt, justify=RIGHT).place(x = 300, y = 145) 

        self.mon_payment = StringVar()
        Entry(frame, textvariable=self.mon_payment,justify=RIGHT).place(x = 300, y = 270) 

        self.tot_payment = StringVar()
        Entry(frame, textvariable=self.tot_payment,justify=RIGHT).place(x = 300, y = 310) 

        # CREATING BUTTONS
        computation = Button(frame, text='Calculate',fg="white",bg='green', width=12, command=self.Payment_Computation).place(x = 150, y = 200)
        Clear = Button(frame, text='Clear',fg="white",bg='green', width=12, command=self.delete_all).place(x = 270, y = 200) 
        clear = Button(frame, text="ClearAll", fg="white",bg='green', width=12, command=self.clear_frame).place(x = 150, y = 370)

    # compute the total payment.
    def Payment_Computation(self):
        month = self.Getting_Payment_in_Monthly(
        float(self.amt.get()),
        float(self.Int_for_Annual.get()) / 1200,
        int(self.yrs.get()))

        self.mon_payment.set(format(month, '10.2f'))

        tot = float(self.mon_payment.get()) * 12 * int(self.yrs.get())

        self.tot_payment.set(format(tot, '10.2f'))

    def Getting_Payment_in_Monthly(self, Amount_Loan, mon_rate_interest, no_of_yrs):
    # compute the monthly payment.
        month = Amount_Loan * mon_rate_interest / (1
        - 1 / (1 + mon_rate_interest) ** (no_of_yrs * 12))
    
        return month;
    def delete_all(self) :
        self.Int_for_Annual.set("")
        self.yrs.set("")
        self.amt.set("")
        self.mon_payment.set("")
        self.tot_payment.set("")
    def clear_frame(self):
        for widgets in frame.winfo_children():
            widgets.destroy()
def display_selected(options):
    options = var1.get()
    if options == "Find the monthly payment":
        loanCal()
    if options == "Find the loan amount":
        loanAmount()
    if options == "Find the number of months":
        Period()
values = ["Find the loan amount", "Find the monthly payment", "Find the number of months"]
var1 = StringVar()
var1.set(values[1])
Label(window, text='Select a calculation',fg="brown",font=('Times', 16), borderwidth=5).place(x = 580,y = 0)
dropdown = OptionMenu(
    window,
    var1,
    *values,
    command=display_selected
)
dropdown.place(x=580,y=30)
class loanAmount():
    def __init__(self):
        # creating the labels
    
        Label(frame, text='Annual Interest Rate %',fg="brown",bg='light blue',font=('Times', 18), borderwidth=8).place(x = 50,y = 50) 

        Label(frame, text='Numbers of months', fg="brown", bg='light blue',font=('Times', 18),borderwidth=8).place(x = 50, y = 90) 

        Label(frame, text='Monthly Payment', fg="brown",bg='light blue',font=('Times', 18),borderwidth=8).place(x = 50, y = 130) 

        Label(frame, text='Principal Amount',fg="brown",bg='light blue',font=('Times', 18), borderwidth=8).place(x = 50, y = 250) 


        # Create the Entry Widgets
        self.Int_for_Annual = StringVar()
        Entry(frame, textvariable=self.Int_for_Annual, justify=RIGHT).place(x = 300, y = 65) 

        self.period = StringVar()
        Entry(frame, textvariable=self.period, justify=RIGHT).place(x = 300, y = 105) 

        self.mon_payment = StringVar()
        Entry(frame, textvariable=self.mon_payment, justify=RIGHT).place(x = 300, y = 145)
        
        self.principal = StringVar()
        Entry(frame, textvariable=self.principal, justify=RIGHT).place(x = 300, y = 260)
        
         # CREATING BUTTONS
        computation = Button(frame, text='compute',fg="white",bg='green', width=12,command =self.Loan_Amount).place(x = 150, y = 200)
        Clear = Button(frame, text='Clear',fg="white",bg='green', width=12, command=self.delete_all).place(x = 270, y = 200) 
        # clear = Button(frame, text="ClearAll", fg="white",bg='green', width=12, command=self.clear_frame).place(x = 150, y = 320)
        
    def Loan_Amount(self):
        amt = self.Calculate_amount(
        float(self.mon_payment.get()),
        float(self.Int_for_Annual.get()),
        int(self.period.get()))
            
        self.principal.set(format(amt, '10.2f'))
            
    def Calculate_amount(self,amount,anuual_int,period):
        i = anuual_int / 1200
        loan_principal = amount / ((i * (1 + i) ** period) / ((1 + i) ** period - 1))
        return loan_principal
    def clear_frame(self):
        for widgets in frame.winfo_children():
            widgets.destroy()
    def delete_all(self) :
        self.Int_for_Annual.set("")
        self.period.set("")
        self.mon_payment.set("")
        self.principal.set("")

class Period():
    def __init__(self):
        # creating the labels
    
        Label(frame, text='Principal Amount',fg="brown",bg='light blue',font=('Times', 18), borderwidth=8).place(x = 50,y = 50) 

        Label(frame, text='Annual Interest Rate %', fg="brown",bg='light blue',font=('Times', 18),borderwidth=8).place(x = 50, y = 90) 

        Label(frame, text='Monthly Payment', fg="brown",bg='light blue',font=('Times', 18),borderwidth=8).place(x = 50, y = 130) 

        Label(frame, text='Period/Duration',fg="brown",bg='light blue',font=('Times', 18), borderwidth=8).place(x = 50, y = 250) 


        # Create the Entry Widgets
        self.principal = StringVar()
        Entry(frame, textvariable=self.principal, justify=RIGHT).place(x = 300, y = 65) 

        self.anu_interest = StringVar()
        Entry(frame, textvariable=self.anu_interest, justify=RIGHT).place(x = 300, y = 105) 

        self.mon_payment= StringVar()
        Entry(frame, textvariable=self.mon_payment, justify=RIGHT).place(x = 300, y = 145)
        
        self.period = StringVar()
        Entry(frame, textvariable=self.period, width=50,justify=LEFT).place(x = 300, y = 260)
        
         # CREATING BUTTONS
        computation = Button(frame, text='compute',fg="white",bg='green', width=12,command =self.cal_Period).place(x = 150, y = 200)
        Clear = Button(frame, text='Clear',fg="white",bg='green', width=12, command=self.delete_all).place(x = 270, y = 200) 
        #clear = Button(frame, text="ClearAll", fg="white",bg='green', width=12, command=self.clear_frame).place(x = 150, y = 320)
        
    def cal_Period(self):
        amt = self.Calculate_period(
        float(self.mon_payment.get()),
        float(self.anu_interest.get()),
        float(self.principal.get()))
            
        self.period.set(amt)
            
    def Calculate_period(self,mon_payment,anuual_int,principal):
        i = anuual_int / 1200
        n_monthly_payments = math.log(mon_payment / (mon_payment - i * principal),i+1)
        years = (math.ceil(n_monthly_payments)) // 12
        months = (math.ceil(n_monthly_payments)) % 12
        output = f'It will take {years} years and {months} months to repay this loan!'
        if years == 1:
            return output.replace('years', 'year')
        elif years == 0:
            return output.replace(f' {years} years and', '')
        if months == 1:
            return output.replace('months', 'month')
        elif months == 0:
            return output.replace(f' and {months} months', '')
        else:
            return output
    
    def clear_frame(self):
        for widgets in frame.winfo_children():
            widgets.destroy()
    def delete_all(self) :
        self.principal.set("")
        self.period.set("")
        self.mon_payment.set("")
        self.anu_interest.set("")

            
window.mainloop()
        
