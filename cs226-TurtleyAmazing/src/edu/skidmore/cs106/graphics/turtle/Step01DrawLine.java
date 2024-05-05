package edu.skidmore.cs106.graphics.turtle;



import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.ImageType;
import us.daveread.edu.graphics.surface.MainFrame;
import us.daveread.edu.graphics.tool.Turtle;

public class Step01DrawLine extends DrawingSurface {
  public Step01DrawLine() {
    new MainFrame(this, "Draw a Line", 400, 400, false);
  }

  public void draw() {
    Turtle turtle = new Turtle(this);
    turtle.forward(100);
  }

  public static void main(String[] args) {
    Step01DrawLine me = new Step01DrawLine();
    me.draw();
  }
}
