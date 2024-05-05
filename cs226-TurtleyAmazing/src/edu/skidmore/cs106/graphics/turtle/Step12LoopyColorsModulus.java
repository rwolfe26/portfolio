package edu.skidmore.cs106.graphics.turtle;

import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.MainFrame;
import us.daveread.edu.graphics.tool.Turtle;

public class Step12LoopyColorsModulus extends DrawingSurface {
  public Step12LoopyColorsModulus() {
    new MainFrame(this, "Loopy Color Modulus Spiraling", 400, 400, false);
  }

  public void draw() {
    // Insert code here
  }

  public static void main(String[] args) {
    Step12LoopyColorsModulus me = new Step12LoopyColorsModulus();
    me.draw();
  }
}
