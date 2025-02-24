package com.lab5;

public interface Searchable {

    default boolean isMatch(String keyword) {
        return false;
    }

}
