package edu.skidmore.cs106.game.tictactoe;

import java.awt.Point;

import us.daveread.edu.graphics.shape.Drawable;
import us.daveread.edu.graphics.shape.impl.Image;
import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.MainFrame;
import us.daveread.edu.utilities.Utility;


public class Step06ArrayLayout extends DrawingSurface {
  Image[][]boardCells;
  
  public Step06ArrayLayout() {
    new MainFrame(this, "Using 2-D Array", 650, 650, false);
    setup();
  }
  
  public void setup() {
    boardCells = new Image[3][3];
    for (int column = 0;column < 3; column++) {
    	for (int row = 0; row < 3; row++) {
    		boardCells[column][row] = new Image("available.png",
    									new Point(column * 160, row * 160),0.5,null);
    		add(boardCells[column][row]);
    	}
    	
    }
  }
  
  public void drawableMouseClick(Drawable image) {
	  int countO = 0, countX = 0;
  
	  for (int column = 0; column < 3; column++) {
	    	for (int row = 0; row < 3; row++) {
	    		if (boardCells[column][row].getImageFileName().equals("o.png")) {
	    			countO++;
	    		} else if (boardCells[column][row].getImageFileName().equals("x.png")) {
	    			countX++;
	    		}
	    	}
	  }
	    		 
    for (int column = 0; column < 3; column++) {
    	for (int row = 0; row < 3; row++) {
    		if (image == boardCells[column][row]) {
    			if (boardCells[column][row].getImageFileName().equals("available.png")) {
    				 boardCells[column][row].setImageFileName(countO <= countX ? "o.png" : "x.png");
    				} else {
    					for (int i = 0; i <= 360; i++) {
        	    			((Image) image).setRotationDegrees(i);
        	    			Utility.pause(2);
    					
    				}
    				
    	    		}
    				return;
    	    	} 
    		}
    	}
    }
  
  
  public static void main(String[] args) {
    new Step06ArrayLayout();
  }
}
