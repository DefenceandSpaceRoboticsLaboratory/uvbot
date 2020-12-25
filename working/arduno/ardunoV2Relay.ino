//-----------------I2C -----------------

//-----------------M1------------------
#define in1 2
#define in2 3
//----------------M2--------------------
#define in3 4 
#define in4 5
//-----------------UV----------------
#define uv1 8  //UV
#define uv2 9  //UV
//-----------------LED----------------
#define green 10 //GREEEN LIGHT
#define red 11 //RED N OTHR DC LIGHTS 


//int speed1 = 0;
//int speed2 = 0;


//------------I2C Function----------
void receiveData(char b,char a,char c)//a=speed,b=direction,c=uv status
{
  int fl=0;
  int fl2=0;
  { 
      {
          
          if (b=='0'){
              stop();
              fl2=fl2+1;
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
          else{fl=1;}
          if ( c=='1'){
              uvon();
          }
          else if (c=='0'){
            uvoff();
            fl2=fl2+1;
          }
          else{fl=1;}
          
          if(fl>0){
            stop();
            uvoff();
            fl2=fl2+2;  
          
          }
          if(fl2>1){
            greenL();  
          }
          else{
            redL();  
          }

          
      }
  }
} 


void setup() {
    // put your setup code here, to run once:
    Serial.begin(9600);
    pinMode(in1,OUTPUT);
    pinMode(in2,OUTPUT);
    pinMode(in3,OUTPUT);
    pinMode(in4,OUTPUT);
    pinMode(green,OUTPUT);
    pinMode(red,OUTPUT);
    pinMode(uv2,OUTPUT);
    pinMode(uv1,OUTPUT);
    digitalWrite(green,LOW);
    digitalWrite(red,LOW);
    digitalWrite(uv1,LOW);
    digitalWrite(uv2,LOW);
    digitalWrite(in1,LOW);
    digitalWrite(in2,LOW);
    digitalWrite(in3,LOW);
    digitalWrite(in4,LOW);

}

void forward(){
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
    digitalWrite(in3,HIGH);
    digitalWrite(in4,LOW);

    Serial.println("forward");
}
void backward(){
    digitalWrite(in2,HIGH);
    digitalWrite(in1,LOW);
    digitalWrite(in4,HIGH);
    digitalWrite(in3,LOW);

    Serial.println("backward");
}
void left(){
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
    digitalWrite(in4,HIGH);
    digitalWrite(in3,LOW);
    Serial.println("left");
}
void right(){
    digitalWrite(in2,HIGH);
    digitalWrite(in1,LOW);
    digitalWrite(in3,HIGH);
    digitalWrite(in4,LOW);
    Serial.println("right");
}
void stop(){
    digitalWrite(in1,LOW);
    digitalWrite(in2,LOW);
    digitalWrite(in3,LOW);
    digitalWrite(in4,LOW);
    Serial.println("stop");
}



void redL(){
  digitalWrite(red,HIGH);
  digitalWrite(green,LOW);
}


void greenL(){
  digitalWrite(red,LOW);
  digitalWrite(green,HIGH);
}
void uvon(){
  digitalWrite(uv1,HIGH);
  digitalWrite(uv2,HIGH);

}
void uvoff(){
  digitalWrite(uv1,LOW);
  digitalWrite(uv2,LOW);
}
void loop() {
   
    while(Serial.available() > 0 ){
        String str = Serial.readString();
        if(str.length()> 3){
            receiveData(str.charAt(0),str.charAt(1),str.charAt(2));
            Serial.print("data received##");
            Serial.print(str.charAt(0));
            Serial.print("##");
            Serial.print(str.charAt(1));
            Serial.print("##");
            Serial.print(str.charAt(2));
            Serial.println("##");
            

            
            delay(1000);
        } 
        else{
            stop();
        }
    }
                                                                                                                                                                               
}
