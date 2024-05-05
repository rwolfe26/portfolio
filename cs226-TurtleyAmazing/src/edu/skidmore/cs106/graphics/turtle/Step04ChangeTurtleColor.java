package edu.skidmore.cs106.graphics.turtle;

// import javafx.scene.paint.Color;
import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.ImageType;
import us.daveread.edu.graphics.surface.MainFrame;
import us.daveread.edu.graphics.tool.Turtle;

// I did the next set of 4 challenges here
public class Step04ChangeTurtleColor extends DrawingSurface {
  public Step04ChangeTurtleColor() {
    new MainFrame(this, "Change Turtle Color", 400, 400, false);
  }

  // Challenge 1
  public void draw() {
    Turtle turtle = new Turtle(this);

    int r = 212;
    int g = 111;
    int b = 73;

    turtle.color(r,g,b);
    turtle.forward(100);
    turtle.right(120);
    turtle.forward(100);
    turtle.right(120);
    turtle.forward(100);
  }
  // Challenge 2
  public void draw2() {
    Turtle turtle = new Turtle(this);
    
   turtle.color(255,200,200);
   turtle.forward(100);
   turtle.right(90);

   turtle.color(255,100,100);
   turtle.forward(50);
   turtle.right(90);

   turtle.color(200,0,0);
   turtle.forward(100);
   turtle.right(90);

   turtle.color(139,0,0);
   turtle.forward(50);

  }

  // Challenge 3
  public void draw3() {
    Turtle turtle = new Turtle(this);

    turtle.color(153,51,255);
    turtle.forward(100);
    turtle.backward(200);
    turtle.forward(100);

    turtle.right(90);
    turtle.color(255,102,178);
    turtle.forward(100);
    turtle.backward(200);
  }

  public static void main(String[] args) {
    Step04ChangeTurtleColor me = new Step04ChangeTurtleColor();
    // me.draw()
    // me.draw1();
    // me.draw2();
    me.draw3();
  }
}
