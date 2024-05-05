package edu.skidmore.cs106.game.tictactoe;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.logging.*;

import java.awt.Color;
import java.awt.Point;

import us.daveread.edu.graphics.shape.Drawable;
import us.daveread.edu.graphics.shape.impl.Image;
import us.daveread.edu.graphics.shape.impl.Text;
import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.MainFrame;
import us.daveread.edu.utilities.Utility;

public class Step08FindWinner extends DrawingSurface {
  Image[][] boardCells;
  Text status;
  boolean isXturn;
  Random random = new Random();

  private static final Logger LOGGER = Logger.getLogger(Step08FindWinner.class.getName());

  public Step08FindWinner() {
	  LOGGER.info("Starting game");
    new MainFrame(this, "Tic-Tac-Toe Game", 650, 650, false);
    

    boardCells = new Image[3][3];
    status = new Text("New Game", new Point(10,550),40,Color.black);
    add(status);
    
    
    for (int column = 0; column < 3; column++) {
    	for (int row = 0; row < 3; row++) {
    		boardCells[column][row] = new Image("available.png",
    				new Point(column * 160, row * 160),0.5,null);
    			add(boardCells[column][row]);
    	}
    }

    setup();
  }

  public void setup() {
	  LOGGER.info("Setting up board");
    for (int column = 0; column < 3; column++) {
    	for (int row = 0; row < 3; row++) {
    		boardCells[column][row].setImageFileName("available.png");
    		boardCells[column][row].setFillColor(null);
    	}
    }
    isXturn = random.nextBoolean();
    nextTurn();
  }

  public void nextTurn() {
    if (!isXturn) {
    	computerMove();
    } else {
        status.setMessage("It is " + (isXturn ? "X" : "O") + "'s turn");

    	
    }
  }

  public void checkForWinner() {
	  LOGGER.info("Checking for a winner");
	  boolean winnerFound = false;
	  boolean tieGame = true;
	  String winnerFile = null;
	  
	  // rows
	  
	  for (int row = 0; row < 3 && !winnerFound; ++row) {
		  if (!boardCells[row][0].getImageFileName().equals("available.png") &&
				  boardCells[row][0].getImageFileName().equals(boardCells[row][1].getImageFileName()) && 
				  boardCells[row][1].getImageFileName().equals(boardCells[row][2].getImageFileName())) {
			  winnerFound = true;
			  winnerFile = boardCells[row][0].getImageFileName().equals("x.png") ? "X" : "O";
			  for (int j =0; j < 3; j++) {
				  boardCells[row][j].setFillColor(Color.green);
			  }
			  break;
		  
		  }
		  
		  // columns
		  if (!boardCells[0][row].getImageFileName().equals("available.png") && 
				  boardCells[0][row].getImageFileName().equals(boardCells[1][row].getImageFileName()) && 
				  boardCells[1][row].getImageFileName().equals(boardCells[2][row].getImageFileName())) {
			  winnerFound = true;
			  winnerFile = boardCells[0][row].getImageFileName().equals("x.png") ? "X" : "O";
			  for (int j = 0; j < 3; j++) {
				  boardCells[j][row].setFillColor(Color.green);
			  }
			  break;
		  }
	  }
	  
	  if (!winnerFound && !boardCells[0][0].getImageFileName().equals("available.png") && 
			  boardCells[0][0].getImageFileName().equals(boardCells[1][1].getImageFileName()) && 
			  boardCells[1][1].getImageFileName().equals(boardCells[2][2].getImageFileName())) {
		  winnerFound = true;
		  winnerFile = boardCells[0][0].getImageFileName();
		  boardCells[0][0].setFillColor(Color.green);
		  boardCells[1][1].setFillColor(Color.green);
		  boardCells[2][2].setFillColor(Color.green);
		  
	  }
	  
	  if (!winnerFound && !boardCells[0][2].getImageFileName().equals("available.png") && 
			  boardCells[0][2].getImageFileName().equals(boardCells[1][1].getImageFileName()) && 
			  boardCells[1][1].getImageFileName().equals(boardCells[2][0].getImageFileName())) {
		  	  winnerFound = true;
		  	  winnerFile = boardCells[0][2].getImageFileName();
		  	  boardCells[0][2].setFillColor(Color.green);
		  	  boardCells[1][1].setFillColor(Color.green);
		  	  boardCells[2][0].setFillColor(Color.green);
		  	  
	  }
	  
	  
		 
	  
	  
	  
	  if (!winnerFound) {
	        for (int col = 0; col < 3; col++) {
	            for (int row = 0; row < 3; row++) {
	                if (boardCells[col][row].getImageFileName().equals("available.png")) {
	                    tieGame = false; 
	                    break;
	                }
	            }
	            if (!tieGame) break;
	        }

	        if (tieGame) {
	            status.setMessage("Tie game!");
	            showErrorMessage("Game Over", "Tie Game");
	            setup(); 
	        } else if (winnerFound) {
	        	status.setMessage("Winner: " + winnerFile);
	        	showErrorMessage("Game Over", "Winner: " + winnerFile);
	        	setup();
	        }
	    } else {
	    	status.setMessage("It is " + (isXturn ? "X" : "O") + "'s turn");

	    }
  }
    
  
    

   
  

  public void drawableMouseClick(Drawable image) {
	  LOGGER.info("Handling mouse clicks");
	  if (!isXturn) return;
	  for (int column = 0; column < 3; column++) {
		  for (int row = 0; row < 3; row ++) {
			  if (image == boardCells[column][row]) {
				  String fileName = boardCells[column][row].getImageFileName();
				  if (fileName.equals("available.png")) {
					  boardCells[column][row].setImageFileName(isXturn ? "x.png" : "o.png");
					  isXturn = false;
					  nextTurn();
					  checkForWinner();
					  if (!isXturn) {
						  computerMove();
					  }
					  return;
	
					  } else {
						  LOGGER.info("Rotating cell at " + column + "," + row);
						  rotateImage(boardCells[column][row]);
					  }
				  	LOGGER.info("Rotating cell at " + column + "," + row);
				  	
				  }
				  
			  }
		  }
	  LOGGER.warning("Click did not correspond to any cell");
	  }
  
  public void rotateImage(Image image) {
	  for (int i = 0; i <= 360; i ++) {
	        image.setRotationDegrees(i);
	        Utility.pause(2);
  }
  }
  
  private void computerMove() {
	  List<Point> available = new ArrayList<>();
	  for (int row = 0; row < 3; row++) {
		  for (int col = 0; col < 3; col++) {
			  if (boardCells[col][row].getImageFileName().equals("available.png")) {
				  available.add(new Point(col,row));
			  }
		  }
		  
	  }
	  if (!available.isEmpty()) {
	  Point choice = available.get(random.nextInt(available.size()));
	  boardCells[choice.x][choice.y].setImageFileName("o.png");
	  isXturn = true;
	  nextTurn();
	  checkForWinner();
	  }
  }

  public static void main(String[] args) {
	  LOGGER.info("Starting game");
    new Step08FindWinner();
  }
}
