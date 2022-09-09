package com.example.clouddatacollection;

import android.widget.EditText;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Network_Thread extends Thread{
    private EditText S_NO;
    private TextView DATE;
    private TextView TIME;
    private TextView TEMP;
    private TextView HUMIDITY;

    private String sensor_no;

    Network_Thread(EditText S_NO, TextView DATE, TextView TIME, TextView TEMP, TextView HUMIDITY){
        this.S_NO = S_NO;
        this.DATE = DATE;
        this.TIME = TIME;
        this.TEMP = TEMP;
        this.HUMIDITY = HUMIDITY;
    }

    @Override
    public void run(){
        try{
            sensor_no = S_NO.getText().toString();

            URL url = new URL("https://temphumiditystation.000webhostapp.com/get_data.php?S_NO=" + sensor_no);
            HttpURLConnection conn = (HttpURLConnection)url.openConnection();
            conn.setRequestMethod("GET");

            InputStreamReader is = new InputStreamReader(conn.getInputStream());
            BufferedReader in = new BufferedReader(is);

            String s = "";
            String inputLine;

            while ((inputLine = in.readLine()) != null) {
                s += inputLine;
            }
            in.close();

            String[] data;
            data = s.split(" ");

            DATE.setText(data[1]);
            TIME.setText(data[2]);
            TEMP.setText(data[3]);
            HUMIDITY.setText(data[4]);
        }
        catch (Exception e){
            DATE.setText(e.toString());
        }
    }
}
