package me.michele.events;


import net.dv8tion.jda.api.entities.Member;
import net.dv8tion.jda.api.entities.Message;
import net.dv8tion.jda.api.entities.User;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Log extends ListenerAdapter {

    public void onMessageReceived(MessageReceivedEvent e) {

        Message m = e.getMessage();
        User user = e.getMember().getUser();
        Member member = e.getMember();

        if (user.isBot())
            return;

        try {

            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");
            LocalDateTime now = LocalDateTime.now();

            FileWriter fw = new FileWriter("src/main/resources/logs.txt", true);
            BufferedWriter bw = new BufferedWriter(fw);
            PrintWriter out = new PrintWriter(bw);
            out.println("User Nickname: " + member.getNickname());
            out.println("User Name: " + member.getUser().getName());
            out.println("Message: " + m.getContentRaw());
            out.println("Date: " + formatter.format(now));
            out.println("\n");
            out.close();

//            System.out.println("Current dir: " + System.getProperty("user.dir"));
//            FileWriter writer = new FileWriter("src/main/resources/logs.txt");
//
//            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");
//            LocalDateTime now = LocalDateTime.now();
//
//            writer.write("User Nickname: " + member.getNickname() + "\nUser Name: " + member.getUser().getName() + "\nMessage: " + m.getContentRaw() + "\nDate: " + formatter.format(now) + "\n");
//            writer.close();
              System.out.println("Wrote to file");

        } catch (IOException ex) {
            ex.printStackTrace();
        }

        System.out.println();
    }
    
}
