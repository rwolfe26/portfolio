package edu.skidmore.cs106.graphics.turtle;

import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.ImageType;
import us.daveread.edu.graphics.surface.MainFrame;
import us.daveread.edu.graphics.tool.Turtle;

public class Step02Turning extends DrawingSurface {
  public Step02Turning() {
    new MainFrame(this, "Turning", 400, 400, false);
  }

  // Challenge 1
  public void draw() {
    Turtle turtle = new Turtle(this);
    turtle.forward(200);
    turtle.left(90);
    turtle.forward(100);
    turtle.left(90);
    turtle.forward(200);
    turtle.left(90);
    turtle.forward(100);
  }

  // Challenge 2
  public void draw2() {
    Turtle turtle = new Turtle(this);
    turtle.forward(125);
    turtle.left(125);
    turtle.forward(115);
    turtle.left(115);
    turtle.forward(85);

  }

  // Challenge 3
  public  void draw3() {
    Turtle turtle = new Turtle(this);

    turtle.forward(100);
    turtle.backward(200);
    turtle.forward(100);
    turtle.right(90);
    turtle.forward(100);
    turtle.backward(200);

  }

  // Challenge 4 I could not get a circle to work, but i got an octagon
  // Feel like a loop is necessary to get a perfect circle, but not sure if i am allowed to use one yet
  public  void draw4() {
    Turtle turtle = new Turtle(this);

    turtle.forward(50); 
    turtle.right(45);
    turtle.forward(50);
    turtle.right(45);
    turtle.forward(50);
    turtle.right(45);
    turtle.forward(50);
    turtle.right(45);
    turtle.forward(50);
    turtle.right(45);
    turtle.forward(50);
    turtle.right(45);
    turtle.forward(50);
    turtle.right(45);
    turtle.forward(50);


  }

  // Just going to make a circle with a loop
  // Stole this from when I made this using python
  public void draw5() {
    Turtle turtle = new Turtle(this);
    int sides = 360;
    double length = 1;
    double angle = 360.0 / sides;

    for (int i = 0; i < sides; i++) {
      turtle.forward((int)length);
      turtle.right((int)angle);
    }
  }
 
  public static void main(String[] args) {
    Step02Turning me = new Step02Turning();
    // me.draw();
    // me.draw2();
    // me.draw3();
    // me.draw4();
    me.draw5();
  }
}
