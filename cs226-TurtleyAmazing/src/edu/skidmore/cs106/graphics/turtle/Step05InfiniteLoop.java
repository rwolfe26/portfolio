package edu.skidmore.cs106.graphics.turtle;

import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.MainFrame;
import us.daveread.edu.graphics.tool.Turtle;
import us.daveread.edu.utilities.Utility;

public class Step05InfiniteLoop extends DrawingSurface {
  public Step05InfiniteLoop() {
    new MainFrame(this, "Infinite While Loop", 400, 400, false);
  }

  public void draw() {
    Turtle turtle = new Turtle(this);
    turtle.speed(9);
    
    for (int x = 0; x < 30; ++x) {
      for (int i = 0; i < 4; i++) {
        turtle.forward(100);
        turtle.left(90);
      }
    }
  }

  // Not really what I was going for, but looks cool!
  public void draw2() {
    Turtle turtle = new Turtle(this);
    turtle.speed(9);
    int sides = 360;
    double length = 1;
    double angle = 360.0 / sides;

    for (int i = 0; i < sides; i++) {
      for (int x = 0; x < 30; x++) {
        for (int y = 0; y < 4; y++) {
      }
      turtle.forward((int)length);
      turtle.right(90);

      length -= 1;
      turtle.right(25);
    }
  }
}

public void draw3() {
  Turtle turtle = new Turtle(this);
  turtle.speed(8);
  int sides = 360;
  double length = 1;
  double angle = 360.0 / sides;

  for (int i = 0; i < sides; i++) {
    if (i % 60 == 0) {
      turtle.color(255,0,0); //red
    } else if (i % 60 == 10) {
      turtle.color(255,127,0); //ornge
    } else if (i % 60 == 20) {
      turtle.color(255,255,0); //yellow
    } else if (i % 60 == 30) {
      turtle.color(0,255,0); //green
    } else if (i % 60 == 40) {
      turtle.color(0,0,255); //blue
    } else if (i % 60 == 50) {
      turtle.color(75,0,130); //indigo
    }
    for (int y = 0; y < 4; y++) {
      
    }
    // for (int x = 0; x < 30; x++) {
     

    turtle.forward((int)length);
    turtle.right(90);

    length -= 1;
    turtle.right(25);
  }
}



  public static void main(String[] args) {
    Step05InfiniteLoop me = new Step05InfiniteLoop();
    // me.draw();
    // me.draw2();
    me.draw3();
  }
}
