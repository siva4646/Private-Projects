package me.michele;

import me.michele.api.Config;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.utils.cache.CacheFlag;

import javax.security.auth.login.LoginException;
import java.util.Scanner;

public class Bot {

    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);
        String playing = s.nextLine();

        Config config = new Config();
        JDABuilder builder = config.setup(s.nextLine(), CacheFlag.ACTIVITY, playing);

        try {
            builder.build();
        } catch (LoginException e) {
            e.printStackTrace();
        }

        System.out.println("Discord Bot Loaded.");
    }

}
