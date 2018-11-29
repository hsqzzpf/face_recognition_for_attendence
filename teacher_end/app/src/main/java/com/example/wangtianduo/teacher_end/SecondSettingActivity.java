package com.example.wangtianduo.teacher_end;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;

public class SecondSettingActivity extends AppCompatActivity {

    RecyclerView recyclerView;
    ClassAdapter charaAdapter;
    ClassDbHelper charaDbHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.course_recycle_view);

        //TODO 9.7 The standard code to fill the recyclerview with data
        recyclerView = findViewById(R.id.classRecyclerView);
        charaDbHelper = ClassDbHelper.createClassDbHelper(this);
        charaAdapter = new ClassAdapter(this, charaDbHelper);
        recyclerView.setAdapter(charaAdapter);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        //TODO 9.8 Put in code to allow each recyclerview item to be deleted when swiped

        //TODO 9.9 attach the recyclerView to helper


    }
}
