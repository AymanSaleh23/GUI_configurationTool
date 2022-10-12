"""
Created on Wed Oct 12 20:05:04 2022

@author: as292
"""
import tkinter 
from tkinter import *
from tkinter import ttk


#   Create Frame named mainFrame
#mainFrame = tkinter.Tk()
#mainFrame.title("System Clock configuration")

#   Create Frame named peripheralFrame
peripheralFrame = tkinter.Tk()
peripheralFrame .title("Peripheral configuration")


#   Set dimentions for the Frames
#mainFrame.geometry('400x300')
peripheralFrame.geometry('1080x720')


peripheralNotebook = ttk.Notebook( peripheralFrame )
peripheralNotebook.pack(pady=10)

AHPFrame  = Frame(peripheralNotebook, width = '400', height = '300', bg= "green")
APB1Frame = Frame(peripheralNotebook, width = '400', height = '300', bg= "blue")
APB2Frame = Frame(peripheralNotebook, width = '400', height = '300', bg= "purple")
Finish    = Frame(peripheralNotebook, width = '400', height = '300', bg= "white")

AHPFrame.pack (fill = 'both', expand = True)
APB1Frame.pack(fill = 'both', expand = True)
APB2Frame.pack(fill = 'both', expand = True)
Finish.pack(fill='both', expand= True)

peripheralNotebook.add(AHPFrame, text='AHP config')
peripheralNotebook.add(APB1Frame, text='APB1 config')
peripheralNotebook.add(APB2Frame, text='APB2 config')
peripheralNotebook.add(Finish, text='Summary And Generate')


    
    
def lableInit ():
    #   Create AHP peripheral Labels
    FSMC_label       = Label (AHPFrame, text= "FSMC").grid      (row=0, column=1)
    USB_OTG_FS_label = Label (AHPFrame, text= "USB OTG FS").grid(row=1, column=1)
    CRC_label   = Label (AHPFrame, text= "CRC").grid            (row=2, column=1)
    FINTF_label   = Label (AHPFrame, text= "Flach Interface").grid  (row=3, column=1)
    RCC_label   = Label (AHPFrame, text= "RCC").grid            (row=4, column=1)
    DMA2_label   = Label (AHPFrame, text= "DMA2").grid          (row=5, column=1)
    DMA1_label   = Label (AHPFrame, text= "DMA1").grid          (row=6, column=1)
    SDIO_label   = Label (AHPFrame, text= "SDIO").grid          (row=7, column=1)
    
    
    #   Create APB1 peripheral Labels
    DAC_label   = Label (APB1Frame, text= "DAC").grid  (row=0, column=1)
    PWR_label   = Label (APB1Frame, text= "PWR").grid  (row=1, column=1)
    BKP_label   = Label (APB1Frame, text= "BKP").grid  (row=2, column=1)
    
    CAN1_label   = Label (APB1Frame, text= "CAN 1").grid  (row=3, column=1)
    CAN2_label   = Label (APB1Frame, text= "CAN 2").grid  (row=4, column=1)
    
    SHARED_USB_CAN_SRAM_label   = Label (APB1Frame, text= "Shared USB/CAN SRAM").grid  (row=5, column=1)
    
    USB_label   = Label (APB1Frame, text= "USB").grid  (row=6, column=1)
    
    I2C1_label   = Label (APB1Frame, text= "I2C 1").grid  (row=7, column=1)
    I2C2_label   = Label (APB1Frame, text= "I2C 2").grid  (row=8, column=1)
    
    USART2_label   = Label (APB1Frame, text= "USART 2").grid  (row=9, column=1)
    USART3_label   = Label (APB1Frame, text= "USART 3").grid  (row=10, column=1)
    USART4_label   = Label (APB1Frame, text= "USART 4").grid  (row=11, column=1)
    USART5_label   = Label (APB1Frame, text= "USART 5").grid  (row=12, column=1)
    
    SPI2_label   = Label (APB1Frame, text= "SPI 2").grid  (row=13, column=1)
    SPI3_label   = Label (APB1Frame, text= "SPI 3").grid  (row=14, column=1)
    
    IWDT_label   = Label (APB1Frame, text= "Independent WDT").grid  (row=15, column=1)
    WDT_label   = Label (APB1Frame, text= "WDT A").grid  (row=16, column=1)
    
    RTC_label   = Label (APB1Frame, text= "RTC").grid  (row=17, column=1)
    TIM2_label   = Label (APB1Frame, text= "Timer 2").grid  (row=18, column=1)
    TIM3_label   = Label (APB1Frame, text= "Timer 3").grid  (row=19, column=1)
    TIM4_label   = Label (APB1Frame, text= "Timer 4").grid  (row=20, column=1)
    TIM5_label   = Label (APB1Frame, text= "Timer 5").grid  (row=21, column=1)
    TIM6_label   = Label (APB1Frame, text= "Timer 6").grid  (row=22, column=1)
    TIM7_label   = Label (APB1Frame, text= "Timer 7").grid  (row=23, column=1)
    TIM12_label   = Label (APB1Frame, text= "Timer 12").grid  (row=24, column=1)
    TIM13_label   = Label (APB1Frame, text= "Timer 13").grid  (row=25, column=1)
    TIM14_label   = Label (APB1Frame, text= "Timer 14").grid  (row=26, column=1)
    
    #   Create APB2 peripheral Labels
    GPIO_A_label   = Label (APB2Frame, text= "GPIO A").grid  (row=0, column=1)
    GPIO_B_label   = Label (APB2Frame, text= "GPIO B").grid  (row=1, column=1)
    GPIO_C_label   = Label (APB2Frame, text= "GPIO C").grid  (row=2, column=1)
    GPIO_D_label   = Label (APB2Frame, text= "GPIO D").grid  (row=3, column=1)
    GPIO_E_label   = Label (APB2Frame, text= "GPIO E").grid  (row=4, column=1)
    GPIO_F_label   = Label (APB2Frame, text= "GPIO F").grid  (row=5, column=1)
    GPIO_G_label   = Label (APB2Frame, text= "GPIO G").grid  (row=6, column=1)
    
    ADC2_label   = Label (APB2Frame, text= "ADC2").grid  (row=7, column=1)
    ADC3_label   = Label (APB2Frame, text= "ADC3").grid  (row=8, column=1)
    
    TIM1_label   = Label (APB2Frame, text= "Timer 1").grid  (row=9, column=1)
    TIM8_label   = Label (APB2Frame, text= "Timer 8").grid  (row=10, column=1)
    TIM9_label   = Label (APB2Frame, text= "Timer 9").grid  (row=11, column=1)
    TIM10_label   = Label (APB2Frame, text= "Timer 10").grid  (row=12, column=1)
    TIM11_label   = Label (APB2Frame, text= "Timer 11").grid  (row=13, column=1)
    
    USART1_label   = Label (APB2Frame, text= "USART 1").grid  (row=14, column=1)
    
    SPI1_label   = Label (APB2Frame, text= "SPI 1").grid  (row=15, column=1)
    
    AFIO_label   = Label (APB2Frame, text= "AFIO").grid  (row=16, column=1)
    
    
    
#Init labels to be displayed
lableInit()

#   List of Live Receiveing Value from Checkbuttons consists of 3 elements
busPeripherals = [IntVar()]*3

#   List of Live Receiveing Value from Checkbuttons consists of 8 elements
busPeripherals[0] = [IntVar()]*8
#   List of Live Receiveing Value from Checkbuttons consists of 27 elements
busPeripherals[1] = [IntVar()]*27
#   List of Live Receiveing Value from Checkbuttons consists of 17 elements
busPeripherals[2] = [IntVar()]*17

#   List of Checkbuttons consists of 3 elements
EN_peripherals_Checkbutton= [IntVar()]*3

#   List of Checkbuttons consists of 8 elements
EN_peripherals_Checkbutton[0] = [IntVar()]*8
#   List of Checkbuttons consists of 17 elements
EN_peripherals_Checkbutton[1] = [IntVar()]*27
#   List of Checkbuttons consists of 27 elements
EN_peripherals_Checkbutton[2] = [IntVar()]*17


#   List to save the last Check Button State consist of 3 elements
EN_peripherals_Checkbutton= [0]*3

#   List to save the last Check Button State consist of 8 elements
EN_peripherals_Checkbutton[0] = [0]*8
#   List to save the last Check Button State consist of 27 elements
EN_peripherals_Checkbutton[1] = [0]*27
#   List to save the last Check Button State consist of 17 elements
EN_peripherals_Checkbutton[2] = [0]*17

#   List of Buttons to branch to advanced peripheral configuration consist of 3 elements
EN_peripherals_advancedConfigButton= [0]*3

#   List of Buttons to branch to advanced peripheral configuration consist of 8 elements
EN_peripherals_advancedConfigButton[0] = [0]*8
#   List of Buttons to branch to advanced peripheral configuration consist of 27 elements
EN_peripherals_advancedConfigButton[1] = [0]*27
#   List of Buttons to branch to advanced peripheral configuration consist of 17 elements
EN_peripherals_advancedConfigButton[2] = [0]*17

#   List of Frames to GUI configuration for peripherals consists of 3 elements
listOfConfigFramesPeripherals = [0]*3
#   List of Frames to GUI configuration for peripherals consists of 8 elements
listOfConfigFramesPeripherals = [0]*8
#   List of Frames to GUI configuration for peripherals consists of 27 elements
listOfConfigFramesPeripherals = [0]*27
#   List of Frames to GUI configuration for peripherals consists of 17 elements
listOfConfigFramesPeripherals = [0]*17

#   Function to Get the data from the GUI
def updateData():
    
    #   Loop to get data from AHP tab
    for i in range(8):
        EN_peripherals_Checkbutton[0][i] = busPeripherals[0][i].get()
    
    #   Loop to get data from APB1 tab
    for i in range(27):
        EN_peripherals_Checkbutton[1][i] = busPeripherals[1][i].get()
        
    #   Loop to get data from APB2 tab
    for i in range(17):
        EN_peripherals_Checkbutton[2][i] = busPeripherals[2][i].get()
    
    
def viewData():
    print(EN_peripherals_Checkbutton[0])
    print(EN_peripherals_Checkbutton[1])
    print(EN_peripherals_Checkbutton[2])
    
    
#   Function to reset the Check Buttons
def resetSelection():
    for i in range(8):
        busPeripherals[0][i]= IntVar()
    
    for i in range(27):
        busPeripherals[1][i]= IntVar()
    
    for i in range(17):
        busPeripherals[2][i]= IntVar()
        
#   Function to create Check Buttons
def createEnableSelector():
    for i in range(8):
        EN_peripherals_Checkbutton[0][i] = ttk.Checkbutton(AHPFrame, text='EN', onvalue=1, offvalue=0, variable=busPeripherals[0][i] ,command=updateData).grid(row=i, column=0)
    
    for i in range(27):
        EN_peripherals_Checkbutton[1][i] = ttk.Checkbutton(APB1Frame, text='EN', onvalue=1, offvalue=0, variable=busPeripherals[1][i] ,command=updateData).grid(row=i, column=0)
    
    for i in range(17):
        EN_peripherals_Checkbutton[2][i] = ttk.Checkbutton(APB2Frame, text='EN', onvalue=1, offvalue=0, variable=busPeripherals[2][i] ,command=updateData).grid(row=i, column=0)


def initFinishFrame():
    Generate_label = Label(Finish, text = "Generate Code"). grid(row=0, column=0)
    Generate_btn = Button(Finish, text = "Press", command = updateData). grid(row=0, column=1)
    
    Generate_label = Label(Finish, text = "Get Summary "). grid(row=1, column=0)
    Generate_btn = Button(Finish, text = "Press", command = viewData). grid(row=1, column=1)
    
    
def initateFrames():
    print("initFrames")
    
def createAdvancedConfigBtn():
    for i in range(8):
        EN_peripherals_advancedConfigButton[0][i] = Button(AHPFrame, text='Advanced Config', command=initFinishFrame).grid(row=i, column=2)
    
    for i in range(27):
        EN_peripherals_advancedConfigButton[1][i] = Button(APB1Frame, text='Advanced Config', command=initFinishFrame).grid(row=i, column=2)
    
    for i in range(17):
        EN_peripherals_advancedConfigButton[2][i] = Button(APB2Frame, text='Advanced Config', command=initFinishFrame).grid(row=i, column=2)
   
resetSelection()
createEnableSelector()
createAdvancedConfigBtn()
initFinishFrame()


peripheralFrame.mainloop()
