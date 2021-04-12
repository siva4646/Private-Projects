package me.michele;

import me.michele.api.Config;
import me.michele.events.EmbedTest;
import me.michele.events.Log;
import me.michele.events.commands.admin.AdminSpam;
import me.michele.events.commands.admin.Purge;
import me.michele.events.commands.admin.RoleAssign;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.utils.cache.CacheFlag;

import javax.security.auth.login.LoginException;
import java.util.Scanner;

public class Bot {

    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);
        System.out.print("Playing Status: ");
        String playing = s.nextLine();
        s.close();

        Config config = new Config();
        JDABuilder builder = config.setup("token", CacheFlag.ACTIVITY, playing);

        builder.addEventListeners(new EmbedTest());
        builder.addEventListeners(new Purge());
        builder.addEventListeners(new AdminSpam());
        builder.addEventListeners(new Log());
        builder.addEventListeners(new RoleAssign());

        try {
            builder.build();
        } catch (LoginException e) {
            e.printStackTrace();
        }

        System.out.println("Discord Bot Loaded.");
    }

}
