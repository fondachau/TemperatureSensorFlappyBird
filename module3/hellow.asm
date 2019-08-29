$MODLP52
org 0000H
   ljmp MainProgram

CLK  EQU 22118400
BAUD equ 115200
T2LOAD equ (0x10000-(CLK/(16*BAUD)))

CSEG

; Configure the serial port and baud rate using timer 2
InitSerialPort:
	clr TR2 ; Disable timer 2
	mov T2CON, #30H ; RCLK=1, TCLK=1 
	mov RCAP2H, #high(T2LOAD)  
	mov RCAP2L, #low(T2LOAD)
	setb TR2 ; Enable timer 2
	mov SCON, #52H
	ret

; Send a character using the serial port
putchar:
    JNB TI, putchar
    CLR TI
    MOV SBUF, a
    RET

; Send a constant-zero-terminated string through the serial port
SendString:
    CLR A
    MOVC A, @A+DPTR
    JZ SendStringDone
    LCALL putchar
    INC DPTR
    SJMP SendString
SendStringDone:
    ret
 
Hello_World:
    DB  'Hello, World!', '\r', '\n', 0

MainProgram:
    MOV SP, #7FH ; Set the stack pointer to the begining of idata
    mov PMOD, #0 ; Configure all ports in bidirectional mode
    
    LCALL InitSerialPort
    MOV DPTR, #Hello_World
    LCALL SendString
    
Forever:
    SJMP Forever
END