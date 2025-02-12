package com.lab.part2;

public class Pyramid implements Shape {

    private double baseWidth, height;

    public Pyramid(double baseWidth, double height) {
        this.baseWidth = baseWidth;
        this.height = height;
    }

    @Override
    public double area() {
        double squareBase = baseWidth * baseWidth;
        double sideHeight = Math.sqrt(
                (baseWidth / 2) * (baseWidth / 2) + height * height);
        double sideArea = baseWidth * sideHeight / 2;

        return squareBase + 4 * sideArea;
    }
}

