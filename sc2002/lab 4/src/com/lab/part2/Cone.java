package com.lab.part2;

public class Cone implements Shape {

    private double radius, height;

    public Cone(double radius, double height) {
        this.radius = radius;
        this.height = height;
    }

    @Override
    public double area() {
        return Math.PI * radius * 
            (radius + Math.sqrt(height * height + radius * radius));
    }
}

