package com.example.raspberry_sensor_manager;

import android.widget.EditText;
import android.widget.TextView;

import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.IOException;
import java.net.Socket;

public class Network_Thread extends Thread{
    private EditText IP;
    private TextView DATE;
    private TextView TIME;
    private TextView TEMP;
    private TextView HUMIDITY;

    private String server_ip, msg;
    private String[] data;
    private Socket socket;
    private DataInputStream in;

    Network_Thread(EditText IP, TextView DATE, TextView TIME, TextView TEMP, TextView HUMIDITY){
        this.IP = IP;
        this.DATE = DATE;
        this.TIME = TIME;
        this.TEMP = TEMP;
        this.HUMIDITY = HUMIDITY;
    }

    @Override
    public void run(){
        try{
            server_ip = IP.getText().toString();

            socket = new Socket(server_ip, 5000);
            in = new DataInputStream(new BufferedInputStream(socket.getInputStream()));

            String msg = "";
            String[] data = new String[10];

            while(true){
                msg = in.readLine();
                System.out.println(msg);
                data = msg.split(" ");

                HUMIDITY.setText(data[0] + "%");
                TEMP.setText(data[1] + "C");
                DATE.setText(data[2] + "/" + data[3] + "/" + data[4]);
                TIME.setText(data[5] + ":" + data[6] + ":" + data[7]);
            }
            //in.close();
            //socket.close();
        }
        catch(IOException e){
            DATE.setText(e.toString());
        }
        catch (Exception e){
            DATE.setText(e.toString());
        }
    }
}
