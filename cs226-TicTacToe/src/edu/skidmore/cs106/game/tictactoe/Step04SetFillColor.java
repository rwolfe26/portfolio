package edu.skidmore.cs106.game.tictactoe;

import java.awt.Color;

import java.awt.Point;

import us.daveread.edu.graphics.shape.Drawable;
import us.daveread.edu.graphics.shape.impl.Image;
import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.MainFrame;


public class Step04SetFillColor extends DrawingSurface {
  Image top_left;
  Image top_right;
  Image bottom_left;
  Image bottom_right;
  
  public Step04SetFillColor() {
    new MainFrame(this, "Fill Coloring", 650, 650, false);
    setup();
  }
  
  public void setup() {
    top_left = new Image("x.png", new Point(0, 0), 0.5, null);
    add(top_left);    
    
    top_right = new Image("o.png", new Point(160, 0), 0.5, null);
    add(top_right);
    
    bottom_left = new Image("available.png", new Point(0, 160), 0.5, null);
    add(bottom_left);
    
    bottom_right = new Image("available.png", new Point(160,160),0.5,null);
    add(bottom_right);
  }
  
  public void drawableMouseClick(Drawable image) {
    if (image == bottom_left) {
    	bottom_left.setImageFileName("o.png");
    	top_right.setFillColor(Color.yellow);
    	bottom_left.setFillColor(Color.yellow);
    } else if (image == bottom_right) {
    	bottom_right.setImageFileName("x.png");
    	top_left.setFillColor(Color.blue);
    	bottom_right.setFillColor(Color.blue);
    }
  }
  
  public static void main(String[] args) {
    new Step04SetFillColor();
  }
}
