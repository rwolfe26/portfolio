package edu.skidmore.cs106.graphics.turtle;

import java.awt.Color;
import java.util.ArrayList;
import java.util.List;

import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.ImageType;
import us.daveread.edu.graphics.surface.MainFrame;
import us.daveread.edu.graphics.tool.Turtle;

public class Step14LoopyGeneratedColors extends DrawingSurface {
  public Step14LoopyGeneratedColors() {
    new MainFrame(this, "Generated Coloring Spiraling", 400, 400, false);
  }
  // Challenge 1
  public void draw() {
    Turtle turtle = new Turtle(this);
    int [][] colors = {
      {255,0,0},
      {0,255,0},
      {0,0,255}
    };

    int index = 0;
    int total = 600;
    int angleChange = 1;

    for (int i = 0; i < total; i++) {
      if (i % 10 == 0) {
        int[] color = colors[index % colors.length];
        turtle.color(color[0],color[1],color[2]);
        index++;
      }
      int size = 50 + (i / 10);
      int angle = 90 +(i * angleChange);

      turtle.speed(9);
      turtle.forward(size);
      turtle.right(angle);
    }

  }

  public void draw2() {
    Turtle turtle = new Turtle(this);

    int size = 5;
    int increase = 2;
    int total = 120;
    int changeShape = 20;
    int index = 0;

    int [][] colors = {
      {255,0,0},
      {0,255,0},
      {0,0,255}
    };

    for (int i = 0; i < total; i++) {
      int[] color = colors[index % colors.length];
      if (i % changeShape == 0) {
        turtle.color(color[0], color[1], color[2]);
        index++;
      }

      // circle
      if (i % (2 * changeShape) < changeShape) {
      int sides = 36;
      double length = size / 10.0;
      double angle = 360.0 / sides;

      
        for (int j = 0; j < sides; j++) {
          turtle.forward((int)length);
          turtle.right((int)angle);
        }
      
    } else {
      for (int j = 0; j < 2; j++) {
        turtle.forward(size);
        turtle.right(90);
        turtle.forward(size/2);
        turtle.right(90);
      }
      }

      turtle.forward(size);
      turtle.right(20);

      size += increase;
    
        
      }
    }


  public static void main(String[] args) {
    Step14LoopyGeneratedColors me = new Step14LoopyGeneratedColors();
    me.draw2();
  }
}
