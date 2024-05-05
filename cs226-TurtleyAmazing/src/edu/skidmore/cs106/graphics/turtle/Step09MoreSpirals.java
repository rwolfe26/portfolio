package edu.skidmore.cs106.graphics.turtle;

import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.MainFrame;
import us.daveread.edu.graphics.tool.Turtle;

public class Step09MoreSpirals extends DrawingSurface {
  public Step09MoreSpirals() {
    new MainFrame(this, "For Loop Spiraling", 400, 400, false);
  }

  public void draw() {
    Turtle turtle = new Turtle(this);
    turtle.penUp();
    for (int i = 0; i < 8; i++) {
      turtle.write(i);
      turtle.forward(i);
    }
  }

  public static void main(String[] args) {
    Step09MoreSpirals me = new Step09MoreSpirals();
    me.draw();
  }
}
