package com.example.wangtianduo.teacher_end;

import android.content.Intent;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v4.content.ContextCompat;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;

/**
 * Created by zhouwei on 17/4/23.
 */

public class ClassFragment extends Fragment {

    private String mFrom;
    RecyclerView recyclerView;
    ClassDbHelper classDbHelper;
    ClassAdapter classAdapter;

    static ClassFragment newInstance(String from){
        ClassFragment fragment = new ClassFragment();
        Bundle bundle = new Bundle();
        bundle.putString("from",from);
        fragment.setArguments(bundle);
        return fragment;
    }

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if(getArguments()!=null){
            mFrom = getArguments().getString("from");
        }

    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.course_recycle_view,null);

        recyclerView = view.findViewById(R.id.classRecyclerView);
        classDbHelper = ClassDbHelper.createClassDbHelper(getContext());
        classAdapter = new ClassAdapter(getContext(), classDbHelper);


        recyclerView.setAdapter(classAdapter);
        recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));

        classAdapter.setOnItemClickListener(new ClassAdapter.OnItemClickListener() {
            @Override
            public void onItemClick(View view, int position) {
                Intent intent = new Intent(getContext(),TabCardview.class);
                intent.putExtra("position",String.valueOf(position));
                startActivity(intent);

            }
        });
        return view;
    }
}
