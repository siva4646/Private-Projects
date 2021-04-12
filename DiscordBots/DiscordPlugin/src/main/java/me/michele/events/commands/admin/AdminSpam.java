package me.michele.events.commands.admin;

import me.michele.api.Methods;
import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.Permission;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.entities.MessageChannel;
import net.dv8tion.jda.api.entities.User;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import java.awt.*;
import java.util.ArrayList;

public class AdminSpam extends ListenerAdapter {

    public void onMessageReceived(MessageReceivedEvent e) {
        User user = e.getMember().getUser();
        Member member = e.getMember();
        MessageChannel channel = e.getChannel();

        if (user.isBot())
            return;

        if (e.getMessage().getContentRaw().startsWith("!spam")) {
            if (member.hasPermission(Permission.ADMINISTRATOR)) {
                if (e.getMessage().getContentRaw().startsWith("!spam")) {
                    for (int i = 0; i < 50; i++) {
                        channel.sendMessage("Spam").queue();

                        try {
                            Thread.sleep(10);
                        } catch (InterruptedException ex) {
                            ex.printStackTrace();
                        }
                    }
                }

            } else {

                ArrayList<String> names = new ArrayList<>();
                ArrayList<Boolean> inLine = new ArrayList<>();
                ArrayList<String> fieldDesc = new ArrayList<>();

                names.add("");
                inLine.add(false);
                fieldDesc.add("");

                EmbedBuilder embed = Methods.createEmbed(0, fieldDesc, inLine, names, false, user, Color.RED, "Insufficient Permissions!", "!spam requires " + Permission.ADMINISTRATOR.toString(), true, "", true, false, user.getAvatarUrl(), "", "", false, false, "", "Permission Error!", true, false);
                user.openPrivateChannel().queue((chan) ->
                {

                    chan.sendMessage(embed.build()).queue();
                });
                return;
            }
        }
    }
}
