//-----------------I2C -----------------

//-----------------M1------------------
#define en1 2
#define in1 3
#define in2 4
#define pwm1 5
//----------------M2--------------------
#define en2 6
#define in3 8
#define in4 7
#define pwm2 9
//-----------------RELAY----------------
#define green 10 //GREEEN LIGHT
#define red 11 //RED N OTHR DC LIGHTS 
#define uv2 12  //UV
#define uv1 13  //UV
int speed1 = 0;
int speed2 = 0;
int inc = 5;

//------------I2C Function----------
void receiveData(char b,char a)
{
  {   {
          speed1=(int)(a- '0')*25;
          speed2=speed1;
          Serial.print("Speed :");
          Serial.print(speed1);
          Serial.println(":");
      }
      {
          
          if (b=='0'){
              stop();
          }
          else if (b=='1'){
                forward();
          }
          else if (b=='2'){
                backward();
          }
          else if (b=='3'){
                left();
          }
          else if (b=='4'){
                right();
          }
          else if (b = '5'){
              uvon();
          }
          else if (b = '6'){
            uvoff();
          }
          else{
              stop();
          }
      }
  }
} 


void setup() {
    // put your setup code here, to run once:
    Serial.begin(9600);
    pinMode(en1,OUTPUT);
    pinMode(in1,OUTPUT);
    pinMode(in2,OUTPUT);
    pinMode(pwm1,OUTPUT);
    pinMode(en2,OUTPUT);
    pinMode(in3,OUTPUT);
    pinMode(in4,OUTPUT);
    pinMode(pwm2,OUTPUT);
    pinMode(green,OUTPUT);
    pinMode(red,OUTPUT);
    pinMode(uv2,OUTPUT);
    pinMode(uv1,OUTPUT);
    speed1=0;
    speed2=0;
    updatespeed();
    digitalWrite(green,LOW);
    digitalWrite(red,LOW);
    digitalWrite(uv1,LOW);
    digitalWrite(uv2,LOW);

}

void forward(){
    updatespeed();
    digitalWrite(en1,HIGH);
    digitalWrite(en2,HIGH);
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
    digitalWrite(in3,HIGH);
    digitalWrite(in4,LOW);
    digitalWrite(red,HIGH);
    Serial.println("forward");
}
void backward(){
    updatespeed();
    digitalWrite(en1,HIGH);
    digitalWrite(en2,HIGH);
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
    digitalWrite(in3,HIGH);
    digitalWrite(in4,LOW);
    digitalWrite(red,HIGH);
    digitalWrite(green,LOW);
    Serial.println("backward");
}
void left(){
    updatespeed();
    digitalWrite(en1,HIGH);
    digitalWrite(en2,HIGH);
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
    digitalWrite(in3,HIGH);
    digitalWrite(in4,LOW);
    digitalWrite(red,HIGH);
    digitalWrite(green,LOW);
    Serial.println("left");
}
void right(){
    updatespeed();
    digitalWrite(en1,HIGH);
    digitalWrite(en2,HIGH);
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
    digitalWrite(in3,HIGH);
    digitalWrite(in4,LOW);
    digitalWrite(red,HIGH);
    digitalWrite(green,LOW);
    Serial.println("right");
}
void stop(){
    speed1=0;
    speed2=0;
    updatespeed();
    digitalWrite(en1,HIGH);
    digitalWrite(en2,HIGH);
    digitalWrite(in1,LOW);
    digitalWrite(in2,LOW);
    digitalWrite(in3,LOW);
    digitalWrite(in4,LOW);
    digitalWrite(red,LOW);
    digitalWrite(green,HIGH);
    Serial.println("stop");
}
void updatespeed(){
    analogWrite(pwm1, speed1);
    analogWrite(pwm2, speed2);    
    Serial.print("Speed:");  
    Serial.print(speed1); 
    Serial.print(",");
    Serial.println(speed2);
}
void uvon(){
  digitalWrite(uv1,HIGH);
  digitalWrite(uv2,HIGH);
  digitalWrite(red,HIGH);
}
void uvoff(){
  digitalWrite(uv1,LOW);
  digitalWrite(uv2,LOW);
  digitalWrite(red,LOW);
}
void loop() {
   
    while(Serial.available() > 0 ){
        String str = Serial.readString();
        if(str.length()> 1){
            receiveData(str.charAt(0),str.charAt(1));
            Serial.print("data received##");
            Serial.print(str.charAt(0));
            Serial.print("##");
            Serial.print(str.charAt(1));
            Serial.println("##");
            

            
            delay(3000);
        } 
        else{
            stop();
        }
    }
                                                                                                                                                                               
}
