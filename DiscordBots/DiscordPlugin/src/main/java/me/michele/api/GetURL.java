package me.michele.api;
import me.michele.api.URL;


public class GetURL {

    public String getUrl(URL url) {
        switch (url) {
            case JAVAURL:
                return URL.JAVAURL.get_url();
            default:
                return "";
        }
    }
}
