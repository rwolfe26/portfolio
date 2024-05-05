package edu.skidmore.cs106.game.tictactoe;

import java.awt.Color;
import java.awt.Point;

import us.daveread.edu.graphics.shape.Drawable;
import us.daveread.edu.graphics.shape.impl.Image;
import us.daveread.edu.graphics.shape.impl.Text;
import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.MainFrame;
import us.daveread.edu.utilities.Utility;

public class Step07DisplayingText extends DrawingSurface {
  Image[][] boardCells;
  Text status;
  boolean isXTurn;
  
 

  public Step07DisplayingText() {
    new MainFrame(this, "Taking Turns", 650, 650, false);
    setup();
  }

  public void setup() {
    boardCells = new Image[3][3];
    for (int column = 0; column < 3; column++) {
      for (int row = 0; row < 3; row++) {
        boardCells[column][row] = new Image("available.png",
            new Point(column * 160, row * 160), 0.5, null);
        add(boardCells[column][row]);
      }
    }
    
    status = new Text("New Game", new Point(10,550),40,Color.black);
    add(status);
    nextTurn();
  }

  public void nextTurn() {
    isXTurn = !isXTurn;
    status.setMessage("it is " + (isXTurn ? "X" : "O") + "'s turn" );
  }

  public void drawableMouseClick(Drawable image) {
    for (int column = 0; column < 3; column++) {
      for (int row = 0; row < 3; row++) {
        if (image == boardCells[column][row]) {
        	String fileName = boardCells[column][row].getImageFileName();
        	if (fileName.equals("available.png")) {
        		boardCells[column][row].setImageFileName(isXTurn ? "X.png" : "O.png");
        		nextTurn();
        	} else if (fileName.equals("X.png") || fileName.equals("O.png")) {
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
    new Step07DisplayingText();
  }
}
