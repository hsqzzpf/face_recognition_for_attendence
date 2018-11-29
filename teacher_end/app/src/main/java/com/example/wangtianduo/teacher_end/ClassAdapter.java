package com.example.wangtianduo.teacher_end;

import android.content.Context;
import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;


public class ClassAdapter extends RecyclerView.Adapter<ClassAdapter.ClassViewHolder>{

    LayoutInflater mInflater;
    Context context;
    ClassDbHelper ClassDbHelper;


    //TODO 9.3 Constructor takes in a context object and a ClassDbHelper object
    //TODO 9.3 assign the inputs to instance variables
    public ClassAdapter(Context context, ClassDbHelper ClassDbHelper) {
        mInflater = LayoutInflater.from(context);
        this.context = context;
        this.ClassDbHelper = ClassDbHelper;
    }

    //TODO 9.4 onCreateViewHolder inflates each CardView layout (no coding)
    @NonNull
    @Override
    public ClassViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        View itemView = mInflater.inflate(R.layout.layout, viewGroup, false);
        return new ClassViewHolder(itemView);
    }

    //TODO 9.5 onBindViewHolder binds the data to each card according to its position
    @Override
    public void onBindViewHolder(@NonNull ClassViewHolder ClassViewHolder, int i) {
        ClassDbHelper.ClassData classData = ClassDbHelper.queryOneRow(i);

        ClassViewHolder.textViewName.setText(classData.getName());
        ClassViewHolder.textViewSession.setText(classData.getSession());
        ClassViewHolder.textViewPosition.setText(Integer.toString(i));
        ClassViewHolder.textViewDate.setText(classData.getDate());
        ClassViewHolder.textViewTiming.setText(classData.getTiming());
        ClassViewHolder.textViewVenue.setText(classData.getVenue());
    }

    //TODO 9.6 this method controls the number of cardviews in the recyclerview
    @Override
    public int getItemCount() {

        return (int) ClassDbHelper.queryNumRows();
    }

    //TODO 9.2 Complete the constructor to initialize the widgets
    class ClassViewHolder extends RecyclerView.ViewHolder{

        public TextView textViewName;
        public TextView textViewSession;
        public TextView textViewPosition;
        public TextView textViewDate;
        public TextView textViewTiming;
        public TextView textViewVenue;

        public ClassViewHolder(View view){
            super(view);
            textViewName = view.findViewById(R.id.cardViewTextName);
            textViewSession = view.findViewById(R.id.cardViewTextDescription);
            textViewPosition = view.findViewById(R.id.cardViewTextCount);
            textViewDate = view.findViewById(R.id.cardViewTextDate);
            textViewTiming = view.findViewById(R.id.cardViewTextTiming);
            textViewVenue = view.findViewById(R.id.cardViewTextVenue);

        }

    }
}
