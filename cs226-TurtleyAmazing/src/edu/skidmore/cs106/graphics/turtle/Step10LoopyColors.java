package edu.skidmore.cs106.graphics.turtle;

import us.daveread.edu.graphics.surface.DrawingSurface;
import us.daveread.edu.graphics.surface.MainFrame;
import us.daveread.edu.graphics.tool.Turtle;

// Doing the two challenges here on page 8
public class Step10LoopyColors extends DrawingSurface {
  public Step10LoopyColors() {
    new MainFrame(this, "Loopy Color Spiraling", 400, 400, false);
  }

  public void draw() {
    Turtle turtle = new Turtle(this);
    int [][] colors = { { 85,211,136}, {197, 196, 126},
    {235, 233, 166 },
    { 25, 135, 222}, { 211, 64, 159}, { 159, 165, 106},
    { 63, 203, 219} };
    
    setBackground(96,96,96);

    for (int i = 0; i < 20; i++) {
      turtle.color(colors[i]);
      turtle.forward(10);
    }
  }
  

  public static void main(String[] args) {
    Step10LoopyColors me = new Step10LoopyColors();
    me.draw();
  }
}
