package me.michele.events;

import me.michele.api.GetURL;
import me.michele.api.Methods;
import me.michele.api.URL;
import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.MessageBuilder;
import net.dv8tion.jda.api.entities.*;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import org.apache.commons.collections4.Get;

import java.awt.*;

public class EmbedTest extends ListenerAdapter {

    public void onMessageReceived(MessageReceivedEvent e){

        Guild server = e.getGuild();
        Role role = server.getRolesByName("Java", false).get(0);
        System.out.println(role);
        for(Member members : server.getMembers()) {
            if(members.getRoles().contains(role)) {
                Methods.sendPrivateMessage(members.getUser(), "Hello <@!" + members.getId() + ">");
                break;
            }
        }

//        e.getChannel().getHistory().retrievePast(1)
//                .map(messages -> messages.get(0))
//                .queue(message -> {
//                    e.getChannel().sendMessage("Last Message: " + message.getContentRaw()).queue();
//                });

        if (e.getChannel().getName().contains("rules")) {
            MessageChannel channel = e.getChannel();

            if (e.getAuthor().isBot())
                return;

            if (e.getMessage().getContentRaw().startsWith("!setuprules")) {
                EmbedBuilder eb = new EmbedBuilder();
                eb.setTitle("Test Title", null);
                /*
                Set Title
                 */

                eb.setColor(Color.RED);
                eb.setColor(new Color(0xF40C0C));
                eb.setColor(new Color(255, 0, 54));

                eb.setDescription("Test");

                eb.addField("Test Fields", "Test Fields (desc)", false);

                eb.addBlankField(false);

                User member = e.getMember().getUser();
                String url = member.getAvatarUrl();

                GetURL urls = new GetURL();

                MessageBuilder builder = new MessageBuilder();
                builder.append(MessageBuilder.Formatting.ITALICS + "Java's Coffee Discord Rules");
                Message header = builder.build();

                eb.setAuthor(header.toString(), null, urls.getUrl(URL.JAVAURL));
                eb.setFooter("Developed by Java", url);

                eb.setImage(null);

                eb.setThumbnail(null);

                channel.sendMessage(eb.build()).queue();
            }
        }
    }
}
