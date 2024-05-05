package edu.skidmore.cs106.game.tictactoe;

import java.awt.Point;

import us.daveread.edu.graphics.shape.Drawable;
import us.daveread.edu.graphics.shape.impl.Image;
import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.MainFrame;


public class Step03ClickImage extends DrawingSurface {
  Image top_left;
  Image top_right;
  Image bottom_right;
  Image bottom_left;
  
  int counter = 0;
  public Step03ClickImage() {
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
	  
    if ((image == bottom_right || image == bottom_left) && ((Image) image).getImageFileName().equals("available.png")) {
    	if (((Image) image).getImageFileName().equals("available.png"))
    		counter++;
    		if (image == bottom_right) {
    			((Image) image).setImageFileName(counter % 2 == 0 ? "x.png" : "o.png");
    	
    		}else if (image == bottom_left) {
    			((Image) image).setImageFileName(counter % 2 != 0 ? "o.png": "x.png");
    	}
    }
  }
    
    
  
  public static void main(String[] args) {
    new Step03ClickImage();
  }
}
