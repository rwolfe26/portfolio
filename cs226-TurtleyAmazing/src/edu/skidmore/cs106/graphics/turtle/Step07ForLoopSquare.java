package edu.skidmore.cs106.graphics.turtle;

import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.ImageType;
import us.daveread.edu.graphics.surface.MainFrame;
import us.daveread.edu.graphics.tool.Turtle;

public class Step07ForLoopSquare extends DrawingSurface {
  public Step07ForLoopSquare() {
    new MainFrame(this, "For Loop Square", 400, 400, false);
  }

  public void draw() {
    // Insert code here
  }

  public static void main(String[] args) {
    Step07ForLoopSquare me = new Step07ForLoopSquare();
    me.draw();
  }
}
