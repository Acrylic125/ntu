package com.lab5;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

public class Library {

    private List<Book> books = new ArrayList<>();
    private List<String> genres = new ArrayList<>();
    private Map<String, List<Book>> authorBooksMap = new HashMap<>();
    private List<Borrower> borrowers = new ArrayList<>();

    public void addBook(Book book) {
        books.add(book);
        List<Book> authorBooks = authorBooksMap.getOrDefault(book.getAuthor(), new ArrayList<>());
        authorBooks.add(book);
        authorBooksMap.put(book.getAuthor(), authorBooks);
    }

    public boolean removeBookByTitle(String title) {
        Optional<Book> b = books.stream()
            .filter(book -> book.getTitle().equals(title))
            .findFirst();
        if (b.isPresent()) {
            return removeBook(b.get());
        }
        return false;
    }

    // DOES NOT REMOVE FROM BORROWED!
    public boolean removeBook(Book book) {
        boolean removed = books.remove(book);
        List<Book> authorBooks = authorBooksMap.get(book.getAuthor());
        authorBooks.remove(book);
        authorBooksMap.put(book.getAuthor(), authorBooks);
        return removed;
    }

    public List<Book> getBooks() {
        return books;
    }

    public List<String> getGenres() {
        return genres;
    }

    public Map<String, List<Book>> getAuthorBooksMap() {
        return authorBooksMap;
    }

    public List<Book> filter(String genre, String author) {
        return this.books.stream()
            .filter(book -> 
                    (genre == null || book.getGenre().equals(genre)) &&
                    (author == null || book.getAuthor().equals(author)))
            .collect(Collectors.toList());
    }

    public List<Book> search(String keyword) {
        return this.books.stream()
            .filter(book -> book.isMatch(keyword))
            .collect(Collectors.toList());
    }
    
    public void displayBooks() {
        books.forEach(System.out::println);
    }

    public void displayBooksSorted() {
        List<Book> copy = new ArrayList<>(books);
        copy.sort((a, b) -> a.getTitle().compareTo(b.getTitle()));
        copy.forEach(System.out::println);
    }

    public List<Book> recommendBooks(String genre) {
        return this.books.stream()
            .filter(book -> book.getGenre().equals(genre))
            .collect(Collectors.toList());
    }

    public List<Borrower> getBorrowers() {
        return borrowers;
    }

    public Borrower findBorrower(String name) {
        Borrower borrower = this.borrowers.stream()
            .filter(b -> b.getName().equals(name))
            .findFirst()
            .orElse(null);
        if (borrower == null) {
            borrower = new Borrower(name, new ArrayList<>());
            this.borrowers.add(borrower);
        }
        return borrower;
    }

    // -1 if book not found, 0 if successful
    public int borrowBook(Borrower borrower, String bookName) {
        Book book = this.books.stream()
            .filter(b -> b.getTitle().equals(bookName))
            .findFirst()
            .orElse(null);
        if (book == null) {
            return -1;
        }
        borrower.borrowBook(book);
        this.removeBook(book);
        return 0;
    }

    // -1 if book not found,  0 if successful
    public int returnBook(Borrower borrower, String bookName) {
        Book book = borrower.getBorrowedBooks().stream()
            .filter(b -> b.getTitle().equals(bookName))
            .findFirst()
            .orElse(null);
        if (book == null) {
            return -1;
        }
        borrower.returnBook(book);
        this.addBook(book);
        return 0;
    }

}
