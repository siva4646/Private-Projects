package me.michele.api;

import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.entities.User;

import java.awt.*;
import java.util.ArrayList;

public class Methods {


    public static void sendPrivateMessage(User user, String content) {
        user.openPrivateChannel()
                .flatMap(channel -> channel.sendMessage(content))
                .queue();
    }

    public static EmbedBuilder createEmbed(int numOfFields, ArrayList<String> fieldDesc, ArrayList<Boolean> inLine
                                           , ArrayList<String> names, boolean fields
                                           , User user, Color color, String title, String description
                                           , boolean footer, String footerStr, boolean image, boolean thumbnail
                                           , String imageUrl, String thumbnailUrl
                                           , String titleUrl, boolean titleHasUrl
                                           , boolean footerUrl, String footerUrlStr, String author, boolean hasTitle, boolean hasDescription
                                          )
    {

        EmbedBuilder embed = new EmbedBuilder();
        embed.setAuthor(author, null, URL.JAVAURL.get_url());

        if (hasTitle) { // If there is a title
            if (titleHasUrl) { // If the title has an image
                embed.setTitle(title, titleUrl); // Set the title to title and the url to titleUrl
            } else {
                embed.setTitle(title, null); // Set the title to title and the url to null
            }
        }

        embed.setColor(color);

        if (hasDescription)
            embed.setDescription(description);

        String url = user.getAvatarUrl();

        if (fields) { // If the user wants fields
            for (int i = 0; i != numOfFields; i++) { // Iterate until it has reached the number of fields
                embed.addField(names.get(i), fieldDesc.get(i), inLine.get(i)); // Adds fields by grabbing the i value from names, fieldDesc, and inLine
            }
        }


        if (footer) {
            if (footerUrl) {
                embed.setFooter(footerStr, footerUrlStr);
            } else {
                embed.setFooter(footerStr, null);
            }
        }

        if (image)
            embed.setImage(imageUrl);

        if (thumbnail)
            embed.setImage(thumbnailUrl);

        return embed;
    }

    public static EmbedBuilder createPermissionError(String title) {
        EmbedBuilder builder = new EmbedBuilder();

        builder.setAuthor(title, null, URL.JAVAURL.get_url()); // Sets title to title var, with the Java logo.
        builder.setTitle("Insufficient Permissions!");
        builder.setColor(Color.RED);
        builder.setDescription("Developed by Michele#0002");
        builder.setFooter("Permission Error!");

        return builder;
    }
}
