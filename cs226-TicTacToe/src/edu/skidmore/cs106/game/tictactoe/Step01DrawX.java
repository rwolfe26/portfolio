package edu.skidmore.cs106.game.tictactoe;

import java.awt.Point;
import us.daveread.edu.graphics.shape.impl.Image;
import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.MainFrame;

public class Step01DrawX extends DrawingSurface { 
  public Step01DrawX() {
    new MainFrame(this, "Draw an Image", 650, 650, false);
  }
  
  public void setup() {
    Image top_left = new Image("x.png", new Point(50,100),null);
    Image bottom_left = new Image("o.png", new Point(25,450),null);
    Image top_right = new Image("available.png", new Point(100,100), null);
    add(top_left);
    add(bottom_left);
    add(top_right);
  }
  
  public static void main(String[] args) {
    Step01DrawX me = new Step01DrawX();
    me.setup();
  }
}
