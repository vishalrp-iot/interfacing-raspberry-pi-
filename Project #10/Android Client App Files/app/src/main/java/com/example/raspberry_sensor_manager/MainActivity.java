package com.example.raspberry_sensor_manager;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }


    public void onStartClick(View v){
        EditText IP = (EditText)findViewById(R.id.editText3);
        TextView DATE = (TextView)findViewById(R.id.textView2);
        TextView TIME = (TextView)findViewById(R.id.textView3);
        TextView TEMP = (TextView)findViewById(R.id.textView6);
        TextView HUMIDITY = (TextView)findViewById(R.id.textView7);

        Network_Thread nt = new Network_Thread(IP, DATE, TIME, TEMP, HUMIDITY);
        nt.start();
    }

    public void onStopClick(View v) throws InterruptedException{
        //nt.interrupt();
        TextView DATE = (TextView)findViewById(R.id.textView2);
        TextView TIME = (TextView)findViewById(R.id.textView3);
        TextView TEMP = (TextView)findViewById(R.id.textView6);
        TextView HUMIDITY = (TextView)findViewById(R.id.textView7);

        DATE.setText("");
        TIME.setText("");
        TEMP.setText("");
        HUMIDITY.setText("");
    }
}
