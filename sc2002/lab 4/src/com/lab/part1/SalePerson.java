package com.lab.part1;

public class SalePerson implements Comparable {
    private String firstName, lastName;
    private int totalSales;

    public SalePerson(String firstName, String lastName, int totalSales) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.totalSales = totalSales;
    }

    @Override
    public int compareTo(Object o) {
        if (!(o instanceof SalePerson)) {
            return 0;
        } 
        SalePerson _obj = (SalePerson) o;
        int diff = this.totalSales - _obj.totalSales;
        if (diff != 0) {
            return diff;
        }
        
        return _obj.lastName.compareTo(lastName);
        // System.out.println(diff + " : " + this + " vs " + _obj);
        // return (firstName + lastName).compareTo(_obj.firstName + _obj.lastName);
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof SalePerson)) {
            return false;
        } 
        SalePerson _obj = (SalePerson) obj;
        return firstName == _obj.firstName && lastName == _obj.lastName;
    }

    @Override
    public String toString() {
        return this.lastName + " , " + this.firstName + " : " + this.totalSales;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public int getTotalSales() {
        return totalSales;
    }

}
