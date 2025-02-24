package com.lab5;

import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {

    private static void prepopulateLibrary(Library library) {
        library.addBook(new Book("1984", "George Orwell", 1949, "Fiction"));
        library.addBook(new Book("A Brief History of Time", "Stephen Hawking", 1988, "Science"));
    }

    public static void main(String[] args) {
        Library library = new Library();
        
        // Prepopulate library
        prepopulateLibrary(library);

        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            System.out.println("1. Add book");
            System.out.println("2. Remove book");
            System.out.println("3. View books");
            System.out.println("4. Filter by genre");
            System.out.println("5. Filter by author");
            System.out.println("6. Search by keyword");
            System.out.println("7. Borrow Book");
            System.out.println("8. Return Book");
            System.out.println("9. Recommend Book by Category");
            System.out.println("10. Exit");
            choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    scanner.nextLine(); // Consume the leftover newline
                    System.out.println("Enter title: ");
                    String title = scanner.nextLine();
                    System.out.println("Enter author: ");
                    String author = scanner.nextLine();
                    System.out.println("Enter genre: ");
                    String genre = scanner.nextLine();
                    System.out.println("Enter publication year: ");
                    int publicationYear = scanner.nextInt();
                    library.addBook(new Book(title, author, publicationYear, genre));
                    System.out.println("Book added, total books in library: " + library.getBooks().size());
                    break;
                case 2:
                    System.out.println("Enter title: ");
                    scanner.nextLine(); // Consume the leftover newline
                    title = scanner.nextLine();
                    boolean removed = library.removeBookByTitle(title);
                    if (removed) {
                        System.out.println("Book removed, total books in library: " + library.getBooks().size());
                        break;
                    }
                    System.out.println("Book was not removed. It may not exist. Did someone already borrowed it?");
                    break;
                case 3:
                    if (library.getBooks().size() <= 0) {
                        System.out.println("No books in library.");
                        break;
                    }
                    System.out.println("How would you want to view this?");
                    System.out.println("1. Any order");
                    System.out.println("2. Sorted");
                    System.out.println("3. Back");
                    int choice2 = scanner.nextInt();
                    switch (choice2) {
                        case 1:
                            library.displayBooks();
                            break;
                        case 2:
                            library.displayBooksSorted();
                            break;
                        default:
                            continue;
                    }
                    break;
                case 4:
                    System.out.println("Enter genre: ");
                    library.getGenres().forEach(System.out::println);
                    scanner.nextLine(); // Consume the leftover newline
                    genre = scanner.nextLine();
                    List<Book> filtered = library.filter(genre, null);
                    if (filtered.isEmpty()) {
                        System.out.println("No books found");
                    } else {
                        filtered.forEach(System.out::println);
                    }
                    break;
                case 5:
                    System.out.println("Enter author: ");
                    scanner.nextLine(); // Consume the leftover newline
                    author = scanner.nextLine();
                    Map<String, List<Book>> authorBooksMap = library.getAuthorBooksMap();
                    List<Book> books = authorBooksMap.get(author);
                    if (books == null) {
                        System.out.println("No books found.");
                        break;
                    }
                    books.forEach(System.out::println);
                    break;
                case 6:
                    System.out.println("Enter keyword to search: ");
                    scanner.nextLine(); // Consume the leftover newline
                    String keyword = scanner.nextLine();
                    List<Book> found = library.search(keyword);
                    if (found.size() <= 0) {
                        System.out.println("No books found.");
                        break;
                    }
                    found.forEach(System.out::println);
                    break;
                case 7:
                    System.out.println("Enter your name: ");
                    scanner.nextLine(); // Consume the leftover newline
                    String name = scanner.nextLine();
                    Borrower borrower = library.findBorrower(name);
                    System.out.println("Enter book title: ");
                    title = scanner.nextLine();
                    int status = library.borrowBook(borrower, title);
                    if (status == -1) {
                        System.out.println("Book not found.");
                        break;
                    }
                    System.out.println("Book borrowed successfully.");
                    System.out.println("Borrower details: " + borrower);
                    break;
                case 8:
                    System.out.println("Enter your name: ");
                    scanner.nextLine(); // Consume the leftover newline
                    name = scanner.nextLine();
                    System.out.println("Enter book title: ");
                    System.out.println("Currently borrowing the following books:");
                    borrower = library.findBorrower(name);
                    if (borrower.getBorrowedBooks().size() <= 0) {
                        System.out.println("User did not borrow any books.");
                        break;
                    }
                    borrower.getBorrowedBooks().forEach(System.out::println);

                    title = scanner.nextLine();
                    status = library.returnBook(borrower, title);
                    if (status == -1) {
                        System.out.println("Book not found.");
                        break;
                    } 
                    if(status == -2) {
                        System.out.println("User did not borrow any books.");
                        break;
                    }
                    System.out.println("Book returned successfully.");
                    System.out.println("Borrower details: " + borrower);
                    break;
                case 9:
                    System.out.println("How would you like to be recommended by?");
                    System.out.println("1. Genre");
                    System.out.println("2. Back");
                    
                    choice2 = scanner.nextInt();
                    // Switch based recommendation based on what was specified in the lab docs.
                    switch (choice2) {
                        case 1:
                            System.out.println("Enter genre: ");
                            scanner.nextLine(); // Consume the leftover newline
                            genre = scanner.nextLine();
                            List<Book> recommended = library.recommendBooks(genre);
                            if (recommended.size() <= 0) {
                                System.out.println("No books found.");
                                break;
                            }
                            recommended.forEach(System.out::println);
                            break;
                        default:
                            continue;
                    }
                    break;
            }
        } while (choice != 10);

    }
}
