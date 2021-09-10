# 树莓派-U型光电传感器实验

## 原理图
![原理图](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210910231511.png)

## 接线图
![接线图](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210910231609.jpg)

## 树莓派管脚图
![树莓派管脚图](https://blog-1258402410.cos.ap-chengdu.myqcloud.com/blog0803/20210902230444.png)

## 代码
### C
```c
#include <wiringPi.h>
#include <stdio.h>

#define LBPin		0  // light break pin set to GPIO0
#define Gpin		1
#define Rpin		2

void LED(int color)
{
	pinMode(Gpin, OUTPUT);
	pinMode(Rpin, OUTPUT);
	if (color == 0){
		digitalWrite(Rpin, HIGH);
		digitalWrite(Gpin, LOW);
	}
	else if (color == 1){
		digitalWrite(Rpin, LOW);
		digitalWrite(Gpin, HIGH);
	}
}

void Print(int x){
	if ( x == 0 ){
		printf("Light was blocked\n");
	}
}

int main(void){

	if(wiringPiSetup() == -1){ //when initialize wiring failed,print messageto screen
		printf("setup wiringPi failed !");
		return 1; 
	}

	pinMode(LBPin, INPUT);
	int temp;
	while(1){
		//Reverse the input of LBPin
		if ( digitalRead(LBPin) == 0 ){  
			temp = 1;
		}
		if ( digitalRead(LBPin) == 1 ){
			temp = 0;
		}

		LED(temp);
		Print(temp);
	}
	return 0;
}
```

编译命令：`gcc photo_interrupter.c -o photo_interrupter -lwiringPi`

### Python
```python
#!/usr/bin/env python
import RPi.GPIO as GPIO

PIPin  = 11
Gpin   = 12
Rpin   = 13

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(Gpin, GPIO.OUT)     # Set Green Led Pin mode to output
	GPIO.setup(Rpin, GPIO.OUT)     # Set Red Led Pin mode to output
	GPIO.setup(PIPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.add_event_detect(PIPin, GPIO.BOTH, callback=detect, bouncetime=200)

def Led(x):
	if x == 0:
		GPIO.output(Rpin, 1)
		GPIO.output(Gpin, 0)
	if x == 1:
		GPIO.output(Rpin, 0)
		GPIO.output(Gpin, 1)

def Print(x):
	if x == 1:
		print '    *************************'
		print '    *   Light was blocked   *'
		print '    *************************'

def detect(chn):
	Led(GPIO.input(PIPin))
	Print(GPIO.input(PIPin))

def loop():
	while True:
		pass

def destroy():
	GPIO.output(Gpin, GPIO.HIGH)       # Green led off
	GPIO.output(Rpin, GPIO.HIGH)       # Red led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
```
