package edu.skidmore.cs106.graphics.turtle;

import java.awt.Color;
import java.util.ArrayList;
import java.util.List;

public class Step13GenerateColors {
  public static void main(String[] args) {
    List<Color> colors = new ArrayList<>();
    int r = 255;
    int g = 0;
    int b = 0;

    // while (g < 255) {
    //   colors.add(new Color(r,g,b));
    //   g += 5;
    // }
    
    // while (r >= 0) {
    //   colors.add(new Color(r,g,b));
    //   r -= 5;
    // }

    while (b <= 255) {
      colors.add(new Color(r,g,b));
        b += 5;
      
    }
  
  System.out.println(colors);
}
}
