package com.lab5;

import java.util.List;

public class Borrower {
    private String name;
    private List<Book> borrowedBooks;
    
    public Borrower(String name, List<Book> borrowedBooks) {
        this.name = name;
        this.borrowedBooks = borrowedBooks;
    }

    public String getName() {
        return name;
    }

    public List<Book> getBorrowedBooks() {
        return borrowedBooks;
    }

    public void borrowBook(Book book) {
        borrowedBooks.add(book);
    }

    public void returnBook(Book book) {
        borrowedBooks.remove(book);
    }

    @Override
    public String toString() {
        return "Borrower{" +
                "name='" + name + '\'' +
                ", borrowedBooks=" + borrowedBooks +
                '}';
    }

}
