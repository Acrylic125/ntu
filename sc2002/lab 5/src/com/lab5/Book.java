package com.lab5;

public class Book implements Searchable {
    private String title;
    private String author;
    private int publicationYear;
    private String genre;

    public Book(String title, String author, int publicationYear,  String genre) {
        this.title = title;
        this.author = author;
        this.publicationYear = publicationYear;
        this.genre = genre;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public int getPublicationYear() {
        return publicationYear;
    }

    public String getGenre() {
        return genre;
    }

    @Override
    public String toString() {
        return "Book{" +
                "title='" + title + '\'' +
                ", author='" + author + '\'' +
                ", genre='" + genre + '\'' +
                ", publicationYear=" + publicationYear +
                '}';
    }

    @Override
    public boolean isMatch(String keyword) {
        return title.contains(keyword) || author.contains(keyword);
    }

}
