package edu.skidmore.cs106.graphics.turtle;

import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.MainFrame;

public class Step03ChangeBackgroundColor extends DrawingSurface {
  public Step03ChangeBackgroundColor() {
    new MainFrame(this, "Change Background Color", 400, 400, false);
  }

  public void draw() {
    int r = 255;
    int g = 0;
    int b = 124;
    

    setBackground(r,g,b);
  }

  public static void main(String[] args) {
    Step03ChangeBackgroundColor me = new Step03ChangeBackgroundColor();
    me.draw();
  }
}
