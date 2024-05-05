package edu.skidmore.cs106.game.tictactoe;

import java.awt.Point;

import us.daveread.edu.graphics.shape.impl.Image;
import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.MainFrame;


public class Step02ScaleImage extends DrawingSurface {
  Image top_left;
  Image top_right;
  Image bottom_left;
  Image bottom_right;
  Image top_middle;
  Image middle_left;
  Image middle_middle;
  Image middle_right;
  Image bottom_middle;
  
  public Step02ScaleImage() {
    new MainFrame(this, "Scaled Images", 650, 650, false);
//    setup();
    setup1();
  }
  
  public void setup() {
    top_left = new Image("x.png", new Point(0,0),0.5,null);
    add(top_left);
    
    top_right = new Image("x.png", new Point(0,310),0.8,null);
    add(top_right);
    
    bottom_left = new Image("x.png", new Point(0,310),1,null);
    add(bottom_left);
    
    bottom_right = new Image("x.png", new Point(310,310),1.5,null);
    add(bottom_right);
  }
  
  public void setup1() {
	  top_left = new Image("x.png",new Point(0,0),0.8, null);
	  add(top_left);
	  
	  top_middle = new Image("x.png", new Point(225,25),0.5,null);
	  add(top_middle);
	  
	  top_right = new Image("x.png", new Point(450,50), 0.2,null);
	  add(top_right);
	  
	  middle_left = new Image("o.png", new Point(25,175), 0.8,null);
	  add(middle_left);
	  
	  middle_middle = new Image("o.png", new Point(250,255), 0.4,null);
	  add(middle_middle);
	  
	  middle_right = new Image("o.png", new Point(355,235), 0.6,null);
	  add(middle_right);
	  
	  bottom_left = new Image("available.png", new Point(25,400), 0.4,null);
	  add(bottom_left);
	  
	  bottom_middle = new Image("available.png", new Point(250,400),0.4,null);
	  add(bottom_middle);
	  
	  bottom_right = new Image("available.png", new Point(450,400), 0.4, null);
	  add(bottom_right);
  }
   
  public static void main(String[] args) {
    new Step02ScaleImage();
  }
}
