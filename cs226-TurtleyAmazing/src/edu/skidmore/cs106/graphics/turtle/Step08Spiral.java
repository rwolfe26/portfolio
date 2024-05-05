package edu.skidmore.cs106.graphics.turtle;

import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.ImageType;
import us.daveread.edu.graphics.surface.MainFrame;
import us.daveread.edu.graphics.tool.Turtle;

public class Step08Spiral extends DrawingSurface {
  public Step08Spiral() {
    new MainFrame(this, "For Loop Spiral", 400, 400, false);
  }

  public void draw() {
    Turtle turtle = new Turtle(this);
    int rgb = 0;

    while (true) {
      turtle.forward(1);
      turtle.right(1);
      rgb = (rgb + 1) % 256;
      turtle.color(rgb,rgb,rgb);
      // Utility.pause(10);

    }
  }

  public static void main(String[] args) {
    Step08Spiral me = new Step08Spiral();
    me.draw();
  }
}
