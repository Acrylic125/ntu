package com.lab.part2;

public class Cuboid implements Shape {

    private double width, breadth, height;

    public Cuboid(double width, double breadth, double height) {
        this.width = width;
        this.breadth = breadth;
        this.height = height;
    }

    @Override
    public double area() {
        return width * breadth * 2 + breadth * height * 2 + height * width * 2;
    }

}

