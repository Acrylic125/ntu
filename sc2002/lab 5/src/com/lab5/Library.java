package com.lab5;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Library<T extends Book> {

    private List<T> books;
    private List<String> genres;
    private Map<String, T> authorBooksMap;

    public Library(List<T> books) {
        this.books = books;
    }

    public void addBook(T book) {
        books.add(book);
    }

    public void removeBook(T book) {
        books.remove(book);
    }

    public List<T> getBooks() {
        return books;
    }

    public List<String> getGenres() {
        return genres;
    }

    public Map<String, T> getAuthorBooksMap() {
        return authorBooksMap;
    }

    public List<T> filter(String genre, String author) {
        return this.books.stream()
            .filter(book -> 
                    (genre == null || book.getGenre().equals(genre)) &&
                    (author == null || book.getAuthor().equals(author)))
            .collect(Collectors.toList());
    }

    public List<T> search(String keyword) {
        return this.books.stream()
            .filter(book -> book.isMatch(keyword))
            .collect(Collectors.toList());
    }
    
    public void displayBooks() {
        books.forEach(System.out::println);
    }

    public List<T> recommendBooks(String genre) {
        return this.books.stream()
            .filter(book -> book.getGenre().equals(genre))
            .collect(Collectors.toList());
    }

}
