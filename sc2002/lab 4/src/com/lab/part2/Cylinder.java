package com.lab.part2;

public class Cylinder implements Shape {

    private double radius, height;

    public Cylinder(double radius, double height) {
        this.radius = radius;
        this.height = height;
    }

    @Override
    public double area() {
        double circleBase = Math.PI * radius * radius;
        double sideArea = 2 * Math.PI * radius * height;
        return 2 * circleBase + sideArea;
    }
}

