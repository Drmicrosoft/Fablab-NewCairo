 
float bx;
float by;
int boxSize = 75;
boolean overBox = false;
boolean locked = false;
float xOffset = 0.0; 
float yOffset = 0.0;

import processing.serial.*;
Serial myPort;
import processing.net.*; 

Client myClient; 

void setup() {
  size(640, 360);
  bx = width/2.0;
  by = height/2.0;
  rectMode(RADIUS);  
  myClient = new Client(this, "127.0.0.1", 5207);
    
}

void draw() { 
  background(0);
  
  // Test if the cursor is over the box 
  if (mouseX > bx-boxSize && mouseX < bx+boxSize && 
      mouseY > by-boxSize && mouseY < by+boxSize) {
    overBox = true;  
    if(!locked) { 
      stroke(255); 
      fill(153);
    } 
  } else {
    stroke(153);
    fill(153);
    overBox = false;
  }
  
  // Draw the box
  rect(bx, by, boxSize, boxSize);
}

void mousePressed() {
  if(overBox) { 
      myClient.write("click 1");

    locked = true; 
    fill(255, 255, 255);
  } else {
      myClient.write("click 2 ");

    locked = false;
  }
  xOffset = mouseX-bx; 
  yOffset = mouseY-by; 

}

void mouseDragged() {
  if(locked) {
    bx = mouseX-xOffset; 
    by = mouseY-yOffset; 
      myClient.write("X dragged with " + bx);
      myClient.write("Y dragged with " + by);
  }
}

void mouseReleased() {
  locked = false;
  myClient.write("Mouse Released");
}