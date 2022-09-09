package com.example.pc_server_data;

import android.widget.EditText;
import android.widget.TextView;

import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class Network_Thread extends Thread{
    private EditText S_NO;
    private TextView DATE;
    private TextView TIME;
    private TextView TEMP;
    private TextView HUMIDITY;

    private String sensor_no, msg, server_ip;
    private String[] data;
    private Socket socket;
    private DataInputStream in;
    private DataOutputStream out;

    Network_Thread(EditText S_NO, TextView DATE, TextView TIME, TextView TEMP, TextView HUMIDITY){
        this.S_NO = S_NO;
        this.DATE = DATE;
        this.TIME = TIME;
        this.TEMP = TEMP;
        this.HUMIDITY = HUMIDITY;
        this.server_ip = "192.168.225.254";
        this.msg = "";
        this.data = new String[10];
    }

    @Override
    public void run(){
        try{
            sensor_no = S_NO.getText().toString();

            socket = new Socket(server_ip, 10000);
            in = new DataInputStream(new BufferedInputStream(socket.getInputStream()));
            out = new DataOutputStream(socket.getOutputStream());

            out.writeBytes(sensor_no);
            msg = in.readLine();
            data = msg.split(" ");

            HUMIDITY.setText(data[3] + "%");
            TEMP.setText(data[2] + "C");
            DATE.setText(data[0]);
            TIME.setText(data[1]);

            in.close();
            out.close();
            socket.close();
        }
        catch(IOException e){
            DATE.setText(e.toString());
        }
        catch (Exception e){
            DATE.setText(e.toString());
        }
    }
}
