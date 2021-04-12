package me.michele.api;

public enum URL {


    JAVAURL("https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Java_programming_language_logo.svg/468px-Java_programming_language_logo.svg.png");

    private final String url;

    URL(final String url) {
        this.url = url;
    }

    public String get_url() {
        return this.url;
    }
}
