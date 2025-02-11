package com.lab;

public class Triangle implements Shape {

    private double width, height;

    public Triangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    @Override
    public double area() {
        return width * height * 0.5;
    }
}

