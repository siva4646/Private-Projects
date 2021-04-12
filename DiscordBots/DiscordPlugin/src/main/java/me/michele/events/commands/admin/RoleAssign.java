package me.michele.events.commands.admin;

import me.michele.api.Methods;
import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.Permission;
import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.entities.Message;
import net.dv8tion.jda.api.entities.MessageChannel;
import net.dv8tion.jda.api.entities.User;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

public class RoleAssign extends ListenerAdapter {

    public void onMessageReceived(MessageReceivedEvent e) {
        User user = e.getMember().getUser();
        Member member = e.getMember();
        Message message = e.getMessage();
        MessageChannel channel = e.getChannel();

        if (channel.getName().equalsIgnoreCase("role-assign")) {
            if (message.getContentRaw().startsWith("!sra")) {
                if (!member.hasPermission(Permission.ADMINISTRATOR)) {
                    EmbedBuilder builder = Methods.createPermissionError("!sra");

                    user.openPrivateChannel().queue((chan) -> {
                        chan.sendMessage(builder.build()).queue();
                    });

                    return;
                }
            }
        }
    }
}
