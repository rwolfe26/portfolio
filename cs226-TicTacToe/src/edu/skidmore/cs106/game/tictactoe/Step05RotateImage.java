package edu.skidmore.cs106.game.tictactoe;

import java.awt.Color;
import java.awt.Point;

import us.daveread.edu.graphics.shape.Drawable;
import us.daveread.edu.graphics.shape.impl.Image;
import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.MainFrame;
import us.daveread.edu.utilities.Utility;

public class Step05RotateImage extends DrawingSurface {
  Image top_left;
  Image top_right;
  Image bottom_right;
  Image bottom_left;
  
  public Step05RotateImage() {
    new MainFrame(this, "Clickable Images", 650, 650, false);
    setup();
  }
  
  public void setup() {
    top_left = new Image("x.png", new Point(0, 0), 0.5, null);
    add(top_left);    
    
    top_right = new Image("o.png", new Point(160, 0), 0.5, null);
    add(top_right);
    
    bottom_right = new Image("available.png", new Point(160, 160), 0.5, null);
    add(bottom_right);  
    
    bottom_left = new Image("available.png", new Point(0,160),0.5,null);
    add(bottom_left);
  }
  
  public void drawableMouseClick(Drawable image) {
    if (!((Image) image).getImageFileName().equals("available.png")) {
    	if (image == bottom_right || image == top_left) {
    		for (int i = 0; i <= 360; i++) {
    			((Image) image).setRotationDegrees(i);
    			Utility.pause(2);
    		}
    	}
    	
    	else if (image == top_right || image == bottom_left) {
    		for (int i = 360; i >= 0; i--) {
    			((Image) image).setRotationDegrees(i);
    			Utility.pause(2);
    	}
    	}
    } else {
    	if (image == bottom_right) {
    		bottom_right.setImageFileName("o.png");
    } else if (image == bottom_left) {
    	bottom_left.setImageFileName("x.png");
    }
   }
  
  }
  
  public static void main(String[] args) {
    new Step05RotateImage();
  }
}
