package me.michele.events.commands.admin;

import me.michele.api.Methods;
import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.Permission;
import net.dv8tion.jda.api.entities.*;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class Purge extends ListenerAdapter {


    public void onMessageReceived(MessageReceivedEvent e) {

        ArrayList<String> names = new ArrayList<>();
        ArrayList<Boolean> inLine = new ArrayList<>();
        ArrayList<String> fieldDesc = new ArrayList<>();

        names.add("");
        inLine.add(false);
        fieldDesc.add("");

        User user = e.getMember().getUser();
        Member member = e.getMember();
        TextChannel channel = e.getTextChannel();
        Guild server = e.getGuild();
        MessageHistory history = channel.getHistory();
        String[] args = e.getMessage().getContentRaw().split(" ");


        if (user.isBot())
            return;

        if (args[0].toLowerCase().equalsIgnoreCase("!purge") || args[0].toLowerCase().equalsIgnoreCase("!massremove") || args[0].toLowerCase().equalsIgnoreCase("!mr")) {

            if (!member.hasPermission(Permission.MESSAGE_MANAGE)) {
                user.openPrivateChannel().queue((chan) -> {
                    EmbedBuilder embed = Methods.createEmbed(0, fieldDesc, inLine, names, false, user, Color.RED, "Insufficient Permissions!", "Permission Error!", true, "Developed by Java", false, false, "", "", "", false, true, user.getAvatarUrl(), "!purge", true, true);
                    chan.sendMessage(embed.build()).queue();
                });

                return;
            }

            if(args.length <= 1) {

                EmbedBuilder eb = Methods.createEmbed(0, fieldDesc, inLine, names,false, user, Color.GREEN, "Java's Coffee House", "Usage: !purge <message count>", true, "Developed by Java", false, false, "", "", "", false, true, user.getAvatarUrl(), "!purge documentation", true, true);

                channel.sendMessage(eb.build()).queue(message -> message.delete().queueAfter(10, TimeUnit.SECONDS));
            } else {
                try {
                    int messages = Integer.parseInt(args[1]);

                    List<Message> pastMsgs = history.retrievePast(messages).complete();
                    channel.deleteMessages(pastMsgs).queue();

                    EmbedBuilder eb = Methods.createEmbed(0, fieldDesc, inLine, names, false, user, Color.GREEN, "Java's Coffee House", "Usage: !purge <message count>", true, "Purging " + messages + " messages..", false, false, "", "", "", false, true, user.getAvatarUrl(), "Purging...", true, true);
                    channel.sendMessage(eb.build()).queue(message -> message.delete().queueAfter(10, TimeUnit.SECONDS));

                } catch (Exception ex) {
                    // TODO
                }
            }
        } else {
            return;
        }

    }
}
