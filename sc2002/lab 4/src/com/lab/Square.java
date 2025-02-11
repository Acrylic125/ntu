package com.lab;

public class Square implements Shape {

    private double width;

    public Square(double width) {
        this.width = width;
    }

    @Override
    public double area() {
        return width * width;
    }
}

