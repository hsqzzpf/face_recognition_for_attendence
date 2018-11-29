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


public class CharaAdapter extends RecyclerView.Adapter<CharaAdapter.CharaViewHolder>{

    LayoutInflater mInflater;
    Context context;
    CharaDbHelper charaDbHelper;


    //TODO 9.3 Constructor takes in a context object and a CharaDbHelper object
    //TODO 9.3 assign the inputs to instance variables
    public CharaAdapter(Context context, CharaDbHelper charaDbHelper) {
        mInflater = LayoutInflater.from(context);
        this.context = context;
        this.charaDbHelper = charaDbHelper;
    }

    //TODO 9.4 onCreateViewHolder inflates each CardView layout (no coding)
    @NonNull
    @Override
    public CharaViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        View itemView = mInflater.inflate(R.layout.layout, viewGroup, false);
        return new CharaViewHolder(itemView);
    }

    //TODO 9.5 onBindViewHolder binds the data to each card according to its position
    @Override
    public void onBindViewHolder(@NonNull CharaViewHolder charaViewHolder, int i) {
        CharaDbHelper.CharaData charaData = charaDbHelper.queryOneRow(i);

        charaViewHolder.textViewName.setText(charaData.getName());
        charaViewHolder.textViewDescription.setText(charaData.getDescription());
        charaViewHolder.textViewPosition.setText(Integer.toString(i));
        charaViewHolder.imageViewChara.setImageBitmap(charaData.getBitmap());
    }

    //TODO 9.6 this method controls the number of cardviews in the recyclerview
    @Override
    public int getItemCount() {

        return (int) charaDbHelper.queryNumRows();
    }

    //TODO 9.2 Complete the constructor to initialize the widgets
    class CharaViewHolder extends RecyclerView.ViewHolder{

        public TextView textViewName;
        public TextView textViewDescription;
        public TextView textViewPosition;
        public ImageView imageViewChara;

        public CharaViewHolder(View view){
            super(view);
            textViewName = view.findViewById(R.id.cardViewTextName);
            textViewDescription = view.findViewById(R.id.cardViewTextDescription);
            textViewPosition = view.findViewById(R.id.cardViewTextCount);
            imageViewChara = view.findViewById(R.id.cardViewImage);

        }



    }
}
